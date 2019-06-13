# setup.py is python-3.7.3 source file

import setuptools

from smallso.ipduplex.version import *

# define install package

setuptools.setup(
    name = 'ipduplex', 
    version = '{MAJOR_NUMBER}.{MINOR_NUMBER}.{REVISION_NUMBER}'.format(
        MAJOR_NUMBER = Version.major_number, 
        MINOR_NUMBER = Version.minor_number, 
        REVISION_NUMBER = Version.revision_number
    ), 
    url = 'https://scp.gitbook.io/api/cloud-api/ipduplex', 
    license = 'Apache License 2.0', 
    author = 'SmallSO Labs.', 
    author_email = 'support@xiaoyy.org', 
    description = 'The official Python SDK for IP Duplex.', 
    packages = [
        'smallso.ipduplex'
    ],
    python_requires = '>=3.4', 
    install_requires = [
        'requests>=2.21.0', 
        'retrying>=1.3.3'
    ], 
    zip_safe = False
)
