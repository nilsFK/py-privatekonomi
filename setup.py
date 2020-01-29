from setuptools import setup, find_packages

setup(name='pyprivatekonomi',
    version='0.0.1a1',
    description='Parse and format bank transactions',
    url='https://github.com/nilsFK/py-privatekonomi',
    author='Nils F. Karlsson',
    author_email='nils@tibiahof.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.7'
    ])