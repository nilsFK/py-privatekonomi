#!/usr/bin/env python
# -*- coding: utf-8 -*-
import types
from pprint import pformat

# http://code.activestate.com/recipes/366254-generic-proxy-object-with-beforeafter-method-hooks/
class ProxyMethodWrapper:
    """
    Wrapper object for a method to be called.
    """
    def __init__(self, obj, func, name):
        self.obj, self.func, self.name = obj, func, name
        assert obj is not None
        assert func is not None
        assert name is not None

    def __call__(self, *args, **kwargs):
        return self.obj._method_call(self.name, self.func, *args, **kwargs)

# http://code.activestate.com/recipes/366254-generic-proxy-object-with-beforeafter-method-hooks/
class HookProxy(object):
    """
    Proxy object that delegates methods and attributes that don't start with _.
    You can derive from this and add appropriate hooks where needed.
    Override _pre/_post to do something before/afer all method calls.
    Override _pre_<name>/_post_<name> to hook before/after a specific call.
    """

    def getObj(self):
        return self._obj

    def __init__(self, objname, obj):
        self._objname, self._obj = objname, obj

    def __getattribute__(self, name):
        """
        Return a proxy wrapper object if this is a method call.
        """
        if name.startswith('_'):
            return object.__getattribute__(self, name)
        else:
            attr = getattr(self._obj, name)
            if type(attr) is types.MethodType:
                return ProxyMethodWrapper(self, attr, name)
            else:
                return attr

    def __setitem__(self, key, value):
        """
        Delegate [] syntax.
        """
        name = '__setitem__'
        attr = getattr(self._obj, name)
        pmeth = ProxyMethodWrapper(self, attr, name)
        pmeth(key, value)

    def _call_str(self, name, *args, **kwargs):
        """
        Returns a printable version of the call.
        This can be used for tracing.
        """
        pargs = [pformat(x) for x in args]
        for k, v in kwargs.iteritems():
            pargs.append('%s=%s' % (k, pformat(v)))
        return '%s.%s(%s)' % (self._objname, name, ', '.join(pargs))

    def _method_call(self, name, func, *args, **kwargs):
        """
        This method gets called before a method is called.
        """
        # pre-call hook for all calls.
        try:
            prefunc = getattr(self, '_pre')
        except AttributeError:
            pass
        else:
            prefunc(name, *args, **kwargs)

        # pre-call hook for specific method.
        try:
            prefunc = getattr(self, '_pre_%s' % name)
        except AttributeError:
            pass
        else:
            prefunc(*args, **kwargs)

        # get real method to call and call it
        rval = func(*args, **kwargs)

        # post-call hook for specific method.
        try:
            postfunc = getattr(self, '_post_%s' % name)
        except AttributeError:
            pass
        else:
            postfunc(*args, **kwargs)

        # post-call hook for all calls.
        try:
            postfunc = getattr(self, '_post')
        except AttributeError:
            pass
        else:
            postfunc(name, *args, **kwargs)
        return rval
