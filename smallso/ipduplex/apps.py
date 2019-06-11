# smallso.ipduplex.apps.py is python-3.7.3 source file

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

from smallso.ipduplex.service import *
from smallso.ipduplex.resource import *
from smallso.ipduplex.errors import *
from smallso.ipduplex.types import *
from smallso.ipduplex.version import *

# define AppService class

class AppService(Service):
    '''
    AppService is a dynamic class. 
    This class indicates an IP Duplex API application service client.
    '''

    # define insights function

    def insights(self, 
        ip_address: str = None
    ) -> Collections.Insights:
        '''
        insights is a member method. 
        This method initializes an object instance of the collection resource Insights.
        '''

        try:
            
            # Initializes an instance of the Resource.Collections.Insights object.

            return Collections.Insights(
                service_client = self, 
                ip_address = ip_address
            )

        except Exception as exception_context:
            
            print('{MODULE_NAME}.py::AppService.insights -> {EXCEPTION_TEXT}'.format(
                MODULE_NAME = __name__, 
                EXCEPTION_TEXT = str(exception_context)
            ))

            raise UnexpectedError(exception_context)
