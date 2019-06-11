# ipduplex.service.py is python-3.7.3 source file

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

import json

from smallso.ipduplex.common import requests
from smallso.ipduplex.common import retrying

from smallso.ipduplex.version import Version
from smallso.ipduplex.errors import *
from smallso.ipduplex.types import *

# define retry_exception_handler function

def retry_exception_handler( 
    exception_context: Exception
) -> bool:

    return (isinstance(exception_context, QuotaError) 
        or isinstance(exception_context, ResourceError) 
        or isinstance(exception_context, TimedOutError) 
        or isinstance(exception_context, RequestError) 
    )

# define Service class

class Service:
    '''
    Service is a dynamic class. 
    This class indicates an IP Duplex API service client. 
    The service client provides quick access to a wide range of IP Duplex resources and methods.
    '''

    # define __init__ function

    def __init__(self, 
        auth_token: str = None
    ):
        '''
        __init__ is the default constructor for this class. 
        This method will perform basic initialization work on the service client.

        parameter str auth_token: Instructs the API to request an authentication token.
        '''

        try:

            # Verify that the value type of the parameter <auth_token> is string.

            if auth_token is not None and not isinstance(auth_token, str):
                raise ValueError('<auth_token> value type is not str')
            
            # Define the class member auth_token and set the value to the value of the parameter <auth_token>.

            self.auth_token: str = auth_token

            # Create a reusable request client object.

            self.request_client: requests.Session = requests.session()

            # Initialize API authentication details.

            if self.auth_token:
                self.request_client.headers['Authorization'] = 'Bearer {AUTH_TOKEN}'.format(
                    AUTH_TOKEN = self.auth_token
                )

            # Enable HTTP SSL authentication to ensure that API calls request security for data exchange.

            self.request_client.verify = True

            # Set the API request response HOOK function

            self.request_client.hooks = {
                'response': self.__response_hook_handler
            }

            # Add a User-Agent request header indicating the client type and version of the current API call request.

            self.request_client.headers['User-Agent'] = 'ipduplex-python-sdk/{SDK_VERSION}'.format(
                SDK_VERSION = '{MAJOR_NUMBER}.{MINOR_NUMBER}.{REVISION_NUMBER}'.format(
                    MAJOR_NUMBER = Version.major_number, 
                    MINOR_NUMBER = Version.minor_number, 
                    REVISION_NUMBER = Version.revision_number
                )
            )

            # Define and initialize the class member endpoint, which indicates the API endpoint.

            self.endpoint: str = 'https://api.ipduplex.com/v1'

        except Exception as exception_context:
            print('{MODULE_NAME}.py::Service.__init__ -> {EXCEPTION_TEXT}'.format(
                MODULE_NAME = __name__, 
                EXCEPTION_TEXT = str(exception_context)
            ))

            raise UnexpectedError(exception_context)

    # define __del__ function

    def __del__(self):
        '''
        __del__ is the default destructor for this class.
        '''

        self.request_client.close()

    # define __response_hook_handler function

    def __response_hook_handler(self, 
        response_context: requests.Response, *args, **kwargs
    ) -> object:
        '''
        __response_hook_handler is a private method of this class. 
        This method handles error handling for any API calls to self.request_client .
        '''

        try:

            # Check that the value and type of the parameter <response_context> is as expected.

            if response_context is None or not isinstance(response_context, requests.Response):
                raise ValueError('<response_context> value invalid')
            
            # If the API response status code is HTTP 200, no error handling is done.

            if response_context.status_code != 200:
                response_exception_context: ResponseError = None

                # Trying to parse the response's JSON object.

                try:
                    response_result: dict = json.loads(response_context.text)

                    if 'code' not in response_result or 'message' not in response_result:
                        raise UnexpectedError('response_result value invalid')

                    # Throws an exception of the corresponding type based on the error code in the JSON object.

                    response_exception_context = (ERROR_EXCEPTIONS[response_result['code']] 
                        if response_result['code'] in ERROR_EXCEPTIONS else ResponseError)(
                            error_code = response_result['code'], 
                            error_message = response_result['message'], 
                            status_code = response_context.status_code
                        )
                except:

                    # The JSON object parsing the response failed, throwing a ResponseError exception.
                    
                    response_exception_context = ResponseError(
                        error_code = None, 
                        error_message = None, 
                        status_code = response_context.status_code
                    )
                
                raise response_exception_context

        except UnexpectedError as exception_context:
            raise exception_context

        except Exception as exception_context:
            print('{MODULE_NAME}.py::Service.__response_hook_handler -> {EXCEPTION_TEXT}'.format(
                MODULE_NAME = __name__, 
                EXCEPTION_TEXT = str(exception_context)
            ))

            raise UnexpectedError(exception_context)

    # define request_rest_api function

    @retrying.retry(
        stop_max_attempt_number = 3, 
        stop_max_delay = 30000, 
        wait_exponential_multiplier = 3000, 
        wait_exponential_max = 30000, 
        retry_on_exception = retry_exception_handler
    )
    def request_rest_api(self, 
        request_type: int, # Types.Enums.HttpRequestType enum
        request_url: str, 
        request_headers: dict = None, 
        request_jsons: dict = None, 
        request_query_params: dict = None, 
    ) -> dict:
        '''
        request_rest_api is a member method of this class. 
        This method implements the basic handling of HTTP requests and responses to the specified REST API.

        parameter int request_type: Indicates the type of HTTP request. 
            The value of this parameter should be set to the member value in the Types.Enums.HttpRequestType enumerator.

        parameter str request_url: Indicates the REST API resource path for the request.

        parameter dict request_headers: Indicates the HTTP request header required by the requested REST API. 
            If not, the value of this parameter should be set to None.

        parameter dict request_jsons: The JSON object required to indicate the requested REST API. 
            If not, the value of this parameter should be set to None.

        parameter dict request_query_params: Indicates the HTTP query parameters required by the requested REST API. 
            If not, the value of this parameter should be set to None.

        
        return dict: If the HTTP request completes successfully, the method returns a dictionary object instance that 
            is parsed by the JSON object in response to the REST API. Otherwise, the method will throw a RequestError 
            or ResponseError exception.
        '''

        try:
            
            # Check that the values and types of the parameters are as expected.

            if not request_type or not isinstance(request_type, int):
                raise ValueError('<request_type> value invalid')
            
            if not request_url or not isinstance(request_url, str):
                raise ValueError('<request_url> value invalid')
            
            if request_headers and not isinstance(request_headers, dict):
                raise TypeError('<request_headers> value type invalid')
            
            if request_jsons and not isinstance(request_jsons, dict):
                raise TypeError('<request_jsons> value type invalid')
            
            if request_query_params and not isinstance(request_query_params, dict):
                raise TypeError('<request_query_params> value type invalid')
            
            # Initialize the value of request_uri.

            request_uri: str = '{END_POINT}{REQUEST_URL}'.format(
                END_POINT = self.endpoint, 
                REQUEST_URL = request_url
            )

            # Initiate an HTTPS invocation request for the REST API.

            response_context: requests.Response = None

            try:
                if request_type == Enums.HttpRequestType.Get:
                    response_context = self.request_client.get(
                        url = request_uri, 
                        params = request_query_params, 
                        headers = request_headers
                    )
                else:
                    raise RequestError('<request_type> value invalid')

            except UnexpectedError as exception_context:
                raise exception_context

            except Exception as exception_context:
                raise RequestError(str(exception_context))
            
            if not response_context or not isinstance(response_context, requests.Response):
                raise RequestError('response_context value invalid')
            
            response_result: dict = None

            try:
                response_result = json.loads(response_context.text)

                if 'code' not in response_result or 'message' not in response_result:
                    raise Exception('response json object invalid')

            except Exception:

                raise ResponseError(
                    status_code = response_context.status_code
                )
            
            return response_result

        except UnexpectedError as exception_context:
            raise exception_context

        except Exception as exception_context:

            print('{MODULE_NAME}.py::Service.request_rest_api -> {EXCEPTION_TEXT}'.format(
                MODULE_NAME = __name__, 
                EXCEPTION_TEXT = str(exception_context)
            ))

            raise UnexpectedError(exception_context)
