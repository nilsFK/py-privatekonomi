from __future__ import absolute_import
from __future__ import unicode_literals
from py_privatekonomi.utilities.common import as_dict, as_obj, time_now
import copy

class TransactionManager(object):
    """ TransactionManager keeps track of individual Transactions and persists to database """
    def __init__(self, models, buffer_ = 100):
        self.buffer = buffer_
        self.models = models
        self.transactions = []

    def addTransaction(self, transaction):
        self.transactions.append(transaction.getFullTransaction())

    def debuffer(self):
        """ persist transactions once the allowed buffer is exceeded """
        if len(self.transactions) >= self.buffer:
            return self.__persist()
        return False

    def forceDebuffer(self):
        """ force persist transactions independent of the buffer """
        return self.__persist()

    def __persist(self):
        if len(self.transactions) > 0:
            base_transactions = []
            for transaction in self.transactions:
                if 'TransactionData' in transaction:
                    transaction_data_id = self.models.TransactionData.create(transaction['TransactionData'])
                    transaction['Transaction']['transaction_data_id'] = transaction_data_id
                base_transactions.append(transaction['Transaction'])
            self.models.Transaction.createMany(base_transactions)
            self.transactions = []
            return True
        else:
            return False

class Transaction(object):
    """ Transaction represents a single transaction in the database and
    whose main purpose is to build and validate the transaction.
    The Transaction in and of itself is pretty useless, it should be subclassed
    and have the subclass implement callback methods, valid callback methods are:

    * on_missing_field(missing_field, model_name)
        the transaction field does not exist in the transaction data. params includes:
                * missing_field - the name of the field which is missing a value
                * model_name - the name of the model whose field is missing
        expected return: None
    * on_entity_unknown(entity_unknown, model_name, model_identifier, transaction_field)
        the field DOES EXIST in the transaction data, but not in the database however. params includes:
                * entity_unknown - entity data as dict.
                * model_name - name of the model which is associated with entity.
                * model_identifier - the field which we attempted to identify the model with.
                * transaction_field - the transaction field which we attempted to set.
        expected return: None
    * on_retrieve_id(model_name, identifier_field, identifier)
        If callback is not defined the Transaction class will attempt to retrieve the ID by looking
        at the identifier. Implementing this callback will override this behaviour and let the subclass
        decide which ID should be picked. Params includes:
                * model_name - name of the model which we want to retrieve the ID for
                * identifier_field - The field name (column name) of the given model
                * identifier - The string by which we want to retrieve the ID by
        expected return: ID of the model by which we want to save by. If None or False is returned, Transaction will default by attempting to lookup the ID by itself.
    """
    def __init__(self, transaction, transaction_group, models):
        self.transaction = transaction
        self.transaction_group = transaction_group
        self.models = as_dict(models)

    def buildTransaction(self):
        self.__buildTransaction()
        self.__validateTransaction()

    def getTransaction(self):
        """ Retrieves only the transaction model associated with the transaction """
        return self.transaction['Transaction']

    def getFullTransaction(self):
        """ Retrieves all models associated with transaction """
        return self.transaction

    def getModels(self):
        return as_obj(self.models)

    def setTransactionField(self, field, value):
        """ This method should be used to set customized fields but could also be used to set any fields on a particular Transaction
        """
        self.transaction['Transaction'][field] = value

    def __build(self, model_name, identifier_field, set_transaction_field):
        if model_name in self.transaction and identifier_field in self.transaction[model_name]:
            identifier = self.transaction[model_name][identifier_field]
            id_ = None
            if self.__has_callback("on_retrieve_id"):
                id_ = self.__callback("on_retrieve_id", params={
                    'model_name' : model_name,
                    'identifier_field' : identifier_field,
                    'identifier' : identifier
                })
            if id_ is None or id_ is False:
                id_ = self.models[model_name].getValue("id", identifier_field, identifier)

            if id_ is False:
                if self.__has_callback("on_entity_unknown"):
                    self.__callback("on_entity_unknown", params={
                        'entity_unknown' : self.transaction[model_name],
                        'model_name' : model_name,
                        'model_identifier' : identifier_field,
                        'transaction_field' : set_transaction_field
                    })
            else:
                self.transaction['Transaction'][set_transaction_field] = id_
        else:
            if self.__has_callback("on_missing_field"):
                self.__callback("on_missing_field", params={
                    'missing_field' : set_transaction_field,
                    'model_name' : model_name
                })

    def __buildTransaction(self):
        self.transaction['Transaction']['group'] = self.transaction_group
        if 'created' not in self.transaction['Transaction']:
            self.transaction['Transaction']['created'] = time_now()
        self.__build("Currency", "code", "currency_id")
        self.__build("Account", "name", "account_id")
        self.__build("TransactionCategory", "name", "transaction_category_id")
        self.__build("TransactionType", "name", "transaction_type_id")
        self.__build("SecurityProvider", "name", "security_provider_id")

    def __validateTransaction(self):
        required_fields = ['account_id', 'transaction_category_id', 'transaction_type_id', 'currency_id']
        for rf in required_fields:
            if rf not in self.transaction['Transaction']:
                raise Exception("Transaction is missing field: %s, detected during processing of transaction: %s" % (rf, repr(self.transaction)))
            elif self.transaction['Transaction'][rf] is False:
                    raise Exception("Transaction field %s is False" % (rf))

    def __has_callback(self, name):
        return name in dir(self)

    def __callback(self, method_name, params):
        return getattr(self, method_name)(params)

class CustomTransaction(Transaction):
    """ A CustomTransaction implements the callbacks:
            * on_missing_field
            * on_entity_unknown
        Note that it does NOT implement on_retrieve_id - this should be implemented
        in subclasses of this class.
        This class is specialized in setting default values when no values are available
    """
    def __init__(self, transaction, transaction_group, models):
        self.defaults = {}
        super(CustomTransaction, self).__init__(transaction, transaction_group, models)

    def setDefault(self, field, id_val):
        if field == 'transaction_data_id':
            raise Exception("Invalid default: unable to set default for field %s" % (field))
        self.defaults[field] = id_val

    def on_missing_field(self, params):
        if params['missing_field'] == 'transaction_category_id':
            self.transaction['Transaction']['transaction_category_id'] = self.defaults['transaction_category_id']
        elif params['missing_field'] == 'currency_id':
            self.transaction['Transaction']['currency_id'] = self.defaults['currency_id']
        elif params['missing_field'] == 'account_id':
            self.transaction['Transaction']['account_id'] = self.defaults['account_id']
        elif params['missing_field'] == 'transaction_type_id':
            self.transaction['Transaction']['transaction_type_id'] = self.defaults['transaction_type_id']
        elif params['missing_field'] == 'security_provider_id':
            self.transaction['Transaction']['security_provider_id'] = self.defaults['security_provider_id']
        else:
            raise Exception("Untreated missing field: %s" % (params['missing_field']))

    def on_entity_unknown(self, params):
        save_data = copy.deepcopy(params['entity_unknown'])
        if params['model_name'] == 'Account':
            save_data['account_category_id'] = self.defaults['account_category_id']
            save_data['organization_id'] = self.defaults['organization_id']
            if 'provider_id' in self.defaults:
                save_data['provider_id'] = self.defaults['provider_id']
        id_ = self.models[params['model_name']].create(save_data)
        self.transaction['Transaction'][params['transaction_field']] = id_

class TransactionHelper(object):
    @staticmethod
    def createTransactionGroup(models):
        return models.TransactionGroup.allocate()

