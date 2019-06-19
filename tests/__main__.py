# tests.__main__.py is python-3.7.3 source file

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

import platform
import traceback

from . import tests

from smallso.ipduplex.version import *
from smallso.ipduplex.accessor import *
from smallso.ipduplex.apps import *

# initialize __version__ value

__version__: str = '0.1.1'

# define print_traceback function

def print_traceback():

    print('\n---------- Stack Trace Start ----------', end = '\n\n')
    
    print(traceback.format_exc())

    print('\n=========== Stack Trace End ===========', end = '\n\n')

# define virtual main function

if __name__ == '__main__':
    
    print('IP Duplex SDK for Python Tests [Version {VERSION_NUMBER}]'.format(
        VERSION_NUMBER = __version__
    ))
    print('(c) 2019 SmallSO Labs. All rights reserved.', end = '\n\n')
    
    print(' > Python Version: {VERSION_NUMBER}'.format(
        VERSION_NUMBER = platform.python_version()
    ))

    print(' > SDK Version: {MAJOR_NUMBER}.{MINOR_NUMBER}.{REVISION_NUMBER} {TYPE_NAME}'.format(
        MAJOR_NUMBER = Version.major_number, 
        MINOR_NUMBER = Version.minor_number, 
        REVISION_NUMBER = Version.revision_number, 
        TYPE_NAME = VERSION_TYPE_NAMES[Version.type_number]
    ), end = '\n\n')

    print('---------- Application Test Start ----------\n')

    try:
        tests.main()
    except ResponseError as exception_context:
        print(' (×) ResponseError: StatusCode = {STATUS_CODE}, ErrorCode = {ERROR_CODE}, ErrorMessage = {ERROR_MESSAGE}'.format(
            STATUS_CODE = exception_context.status_code, 
            ERROR_CODE = exception_context.error_code, 
            ERROR_MESSAGE = exception_context.error_message
        ))
    except Exception as exception_context:
        print(' (×) {EXCEPTION_TYPE_NAME}: {EXCEPTION_TEXT}'.format(
            EXCEPTION_TYPE_NAME = type(exception_context).__name__, 
            EXCEPTION_TEXT = str(exception_context)
        ))

        print_traceback()
    else:
        print(' (√) The application test completed successfully.')

    print('\n=========== Application Test End ===========', end = '\n\n')
