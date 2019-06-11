# smallso.ipduplex.accessor.py is python-3.7.3 source file

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

from smallso.ipduplex.types import *
from smallso.ipduplex.errors import AccessorError

# define AnyAccessor class

class AnyAccessor(Types.AnyResult):
    '''
    AnyAccessor is a dynamic class. 
    This class indicates an accessor object for a simple resource or collection resource.
    '''

    # define __init__ function

    def __init__(self, 
        property_value: object
    ):

        self.property: object = property_value

    # define get function

    def get(self) -> object:
        '''
        Get is the standard method of the accessor and is used to get the value of the corresponding resource. 
        If not, the method will throw an AccessorError exception.
        '''

        try:

            # Try to get and return the private member of the current accessor: property

            return self.property

        except Exception as exception_context:
            raise AccessorError(str(exception_context))
    
# define RegionAccessor class

class RegionAccessor(AnyAccessor):
    '''
    RegionAccessor is a dynamic class. 
    This class indicates the accessor of the RegionResult data structure.
    '''

    # define __init__ function

    def __init__(self):

        self.property: Types.RegionResult = Types.RegionResult()

    # overwrite get function

    def get(self) -> Types.RegionResult:
        '''
        get is a standard method for accessors that gets a RegionResult object 
        that contains a property that indicates a geographic location.
        '''

        return AnyAccessor.get(self)

# define LocationAccessor class

class LocationAccessor(AnyAccessor):
    '''
    LocationAccessor is a dynamic class. 
    This class indicates the accessor of the LocationResult data object.
    '''

    # define __init__ function

    def __init__(self):

        self.property: Types.LocationResult = Types.LocationResult()

    # overwrite get function

    def get(self) -> Types.LocationResult:
        '''
        get is the standard method for accessors to get a LocationResult object 
        containing the properties of the location.
        '''

        return AnyAccessor.get(self)

# define ProviderAccessor class

class ProviderAccessor(AnyAccessor):
    '''
    ProviderAccessor is a dynamic class.
    This class indicates the accessor of the ProviderResult data object.
    '''

    # define __init__ function

    def __init__(self):

        self.property: Types.ProviderResult = Types.ProviderResult()

    # overwrite get function

    def get(self) -> Types.ProviderResult:
        '''
        Get is the standard method for accessors to get a ProviderResult object 
        containing the operator's properties.
        '''

        return AnyAccessor.get(self)

# define ThreatAccessor class

class ThreatAccessor(AnyAccessor):
    '''
    ThreatAccessor is a dynamic class.
    This class indicates the accessor of the ThreatResult data object.
    '''

    # define __init__ function

    def __init__(self):

        self.property: Types.ThreatResult = Types.ThreatResult()

    # overwrite get function

    def get(self) -> Types.ThreatResult:
        '''
        Get is the standard method for accessors to get a ThreatResult object 
        that contains threat assessment properties.
        '''

        return AnyAccessor.get(self)

# define OtherAccessor class

class OtherAccessor(AnyAccessor):
    '''
    OtherAccessor is a dynamic class.
    This class indicates the accessor of the OtherResultEx object.
    '''

    # define __init__ function

    def __init__(self):

        self.property: Types.OtherResultEx = Types.OtherResultEx()

    # overwrite get function

    def get(self) -> Types.OtherResultEx:
        '''
        Get is an accessor standard method for getting a OtherResultEx object 
        with other extra extension properties.
        '''

        return AnyAccessor.get(self)

# define InsightsAccessor class

class OverviewAccessor(AnyAccessor):
    '''
    OverviewAccessor is a dynamic class.
    This class indicates the accessor of the OverviewResult object.
    '''

    # define __init__ function

    def __init__(self):

        self.property: Types.OverviewResult = Types.OverviewResult()

    # overwrite get function

    def get(self) -> Types.OverviewResult:
        '''
        Get is the standard method for accessors to get an OverviewResult object 
        containing geographic location, time zone and latitude and longitude, carrier, 
        threat assessment, and other extra extended attributes.
        '''

        return AnyAccessor.get(self)
