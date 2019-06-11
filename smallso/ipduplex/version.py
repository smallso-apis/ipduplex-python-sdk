# smallso.ipduplex.version.py is python-3.7.3 source file

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

# define VersionType enum class

class VersionType:
    '''
    VersionType is an enumerator. Members in this 
    enumerator indicate a specific version type.
    '''

    Release: int = 1
    Developer: int = 2
    Insider: int = 3

# define Version static class

class Version:
    '''
    Version is a static class. The members included in this class indicate 
    the version number and version type of the current Python SDK.

    member int major_number: indicates the current major version number.
    member int minor_number: indicates the current minor version number.
    member int revision_number: indicates the current revision number.
    member VersionType type_number: indicates the current version type.
    '''

    major_number: int = 0
    minor_number: int = 1
    revision_number: int = 1

    type_number: int = VersionType.Developer

# define VersionType to VersionTypeName mapping dict

VERSION_TYPE_NAMES: dict = {
    VersionType.Release: 'Release', 
    VersionType.Developer: 'Developer', 
    VersionType.Insider: 'Insider'
}
