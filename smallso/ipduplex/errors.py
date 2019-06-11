# smallso.ipduplex.errors.py is python-3.7.3 source file

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

# define UnexpectedError exception class

class UnexpectedError(Exception):
    '''
    UnexpectedError is an exception class. 
    This exception indicates an unexpected runtime error.
    '''

    pass

# define AccessorError exception class

class AccessorError(UnexpectedError):
    '''
    AccessorError is an exception class. 
    This exception indicates an accessor error.
    '''

    pass

# define RequestError exception class

class RequestError(UnexpectedError):
    '''
    RequestError is an exception class. 
    This exception indicates that the sending of the API call request failed.
    '''
    
    pass

# define ResponseError exception class

class ResponseError(UnexpectedError):
    '''
    ResponseError is an exception class. 
    This exception indicates any API call errors.

    member int error_code: Indicates the error code for this API call. 
        If this API call is successful, the value of this property will be set to 0.

    member str error_message: Indicates an error description for this API call. 
        If this API call is successful, the value of this property will be set to success.

    member int status_code: Instructs the API to call the HTTP response status code. 
        If it is unknown, the value of this property will be set to None.
    '''

    # define __init__ function

    def __init__(self, 
        error_code: int = None, 
        error_message: str = None, 
        status_code: int = None
    ):
        self.error_code: int = error_code
        self.error_message: str = error_message
        self.status_code: int = status_code

        UnexpectedError.__init__(self, 'response error: error_code = {ERROR_CODE}; error_message = {ERROR_MESSAGE}; status_code = {STATUS_CODE}'.format(
            ERROR_CODE = self.error_code, 
            ERROR_MESSAGE = self.error_message, 
            STATUS_CODE = self.status_code
        ))

# define InternalError exception class

class InternalError(ResponseError):
    '''
    InternalError is an exception class. 
    This exception indicates an internal server error. 
    Typically this error indicates that the Cloud API server encountered an unexpected 
    internal error while processing this API call request, including but not limited to 
    internal server unresponsive, application unhandled exception, and so on.
    '''

    pass

# define ParameterError exception class

class ParameterError(ResponseError):
    '''
    ParameterError is an exception class. 
    This exception indicates that the parameter is incorrect. 
    This error indicates that the parameters passed to the API method in this API call 
    request do not meet the expected requirements or are missing.
    '''

    pass

# define NotFoundError exception class

class NotFoundError(ResponseError):
    '''
    NotFoundError is an exception class. 
    This exception indicates that the specified resource could not be found. 
    Usually this error indicates that the API method called by this API call request does 
    not exist or that the API method did not retrieve the eligible data.
    '''

    pass

# define QuotaError exception class

class QuotaError(ResponseError):
    '''
    QuotaError is an exception class. 
    This exception indicates a quota error. 
    This error indicates that the service quota is insufficient or exceeds the rate quota limit.
    '''

    pass

# define AuthenticationError exception class

class AuthenticationError(ResponseError):
    '''
    AuthenticationError is an exception class. 
    This exception indicates an authentication error. 
    This error indicates that the Token is not provided for this API call request. If a Token is 
    provided, the Token is invalid, expired, or insufficient.
    '''

    pass

# define UnavailableError exception class

class UnavailableError(ResponseError):
    '''
    UnavailableError is an exception class. 
    This exception indicates that the service is not available. 
    This error indicates that the Cloud API service, API method requested by this API call request 
    is not available. Usually the server that provides the corresponding service is down.
    '''

    pass

# define TimedOutError exception class

class TimedOutError(ResponseError):
    '''
    TimedOutError is an exception class. 
    This exception indicates that the request has timed out. 
    This error indicates that this API call request timed out due to an internal server or third-party 
    resource not responding within the time limit.
    '''

    pass

# define RedirectError exception class

class RedirectError(ResponseError):
    '''
    RedirectError is an exception class. 
    This exception indicates that the request requires a redirect. 
    This error indicates that this API call request needs to be redirected to the new server. Usually 
    because the requested Cloud API service or API method has been migrated.
    '''

    pass

# define FilterError exception class

class FilterError(ResponseError):
    '''
    FilterError is an exception class. 
    This exception indicates a filter error. 
    This error indicates that an unhandled exception occurred in the Cloud API Internet middleware. 
    Usually this error does not occur.
    '''

    pass

# define RejectError exception class

class RejectError(ResponseError):
    '''
    RejectError is an exception class. 
    This exception indicates that the API call request was denied. 
    This error indicates that there are non-conforming behaviors or security risks in this API call request, 
    but this is not absolute. Usually this error does not occur....
    '''

    pass

# define CancelledError exception class

class CancelledError(ResponseError):
    '''
    CancelledError is an exception class. 
    This exception indicates that the request has been canceled. 
    This error indicates that this API call request has been canceled by the client. Often this error can occur 
    in asynchronous API methods.
    '''

    pass

# define AbortedError exception class

class AbortedError(ResponseError):
    '''
    AbortedError is an exception class. 
    This exception indicates a concurrency violation error. 
    This error indicates that this API call request failed due to conflict with other ongoing API call requests. 
    Often this error can occur in API methods that use PUT requests.
    '''

    pass

# define NotImplementedError exception class

class _NotImplementedError(ResponseError):
    '''
    NotImplementedError is an exception class. 
    This exception indicates that the requested API method is not implemented. 
    This error indicates that the API method called by this API call request does not exist on the current server 
    (not implemented).
    '''

    pass

# define ExistedError exception class

class ExistedError(ResponseError):
    '''
    ExistedError is an exception class. 
    This exception indicates that the resource you are trying to create already exists. 
    This error indicates that the resource that the API call request was attempting to create already exists. 
    Often this error can occur in API methods that use PUT requests.
    '''

    pass

# define ResourceError exception class

class ResourceError(ResponseError):
    '''
    ResourceError is an exception class. 
    This exception indicates that the server providing the service does not have enough resources to process 
    this API call request. Normally this error can occur when a burst high concurrent API call request occurs, 
    and the client should immediately retry the API call request using the exponential backoff algorithm.
    '''

    pass

# define ERROR_EXCEPTIONS mapping dict

ERROR_EXCEPTIONS: dict = {
    100: InternalError, 
    101: ParameterError, 
    102: NotFoundError, 
    103: QuotaError, 
    104: AuthenticationError, 
    105: UnavailableError, 
    106: TimedOutError, 
    107: RedirectError, 
    108: FilterError, 
    109: RejectError, 
    110: CancelledError, 
    111: AbortedError, 
    112: _NotImplementedError, 
    113: ExistedError, 
    114: ResourceError
}
