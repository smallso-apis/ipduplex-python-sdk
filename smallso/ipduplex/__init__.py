# smallso.ipduplex.__init__.py is python-3.7.3 source file

# Copyright 2019 SmallSO Labs.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
    This package is the Python SDK for the IP Duplex API. 
    If you have any questions, please refer to the online 
    documentation: https://scp.gitbook.io/api/cloud-api/ipduplex

    thank you very much!

    --------

    Sincerely, King
    2019/6/6 15:51
'''

from smallso.ipduplex.version import Version
from smallso.ipduplex.version import VersionType

from smallso.ipduplex.version import VERSION_TYPE_NAMES

# initialize package __version__ string

__version__ = '{MAJOR_NUMBER}.{MINOR_NUMBER}.{REVISION_NUMBER} {TYPE_NAME}'.format(
    MAJOR_NUMBER = Version.major_number, 
    MINOR_NUMBER = Version.minor_number, 
    REVISION_NUMBER = Version.revision_number, 
    TYPE_NAME = VERSION_TYPE_NAMES[Version.type_number]
)
