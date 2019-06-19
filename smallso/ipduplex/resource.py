# smallso.ipduplex.resource.py is python-3.7.3 source file

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

from smallso.ipduplex.errors import *
from smallso.ipduplex.service import *
from smallso.ipduplex.accessor import *

# define Collections static class

class Collections:
    '''
    Collections is a static class. 
    This class contains multiple collection resources.
    '''

    # define Insights class

    class Insights(OverviewAccessor):
        '''
        Insights is a dynamic class. 
        This class represents a collection resource called Insights that inherits from AnyResource.
        '''

        # define __init__ function

        def __init__(self, 
            service_client: Service, 
            ip_address: str = None
        ):
            '''
            __init__ is the constructor of the current class.
            '''

            try:
                
                # Check that the type and value of the parameter are as expected.

                if not service_client or not isinstance(service_client, Service):
                    raise ValueError('<service_client> value invalid')

                if ip_address and not isinstance(ip_address, str):
                    raise ValueError('<ip_address> value type is not str')

                # initialize the value of the class member ip_address.

                self.ip_address: str = ip_address

                # Initializes the value of the class member service_client.

                self.service_client: Service = service_client

                # Initialize accessor

                OverviewAccessor.__init__(self)

            except Exception as exception_context:

                print('{MODULE_NAME}.py::Collections.Insights.__init__ -> {EXCEPTION_TEXT}'.format(
                    MODULE_NAME = __name__, 
                    EXCEPTION_TEXT = str(exception_context)
                ))

                raise UnexpectedError(exception_context)

        # overwrite get function

        def get(self) -> Types.OverviewResult:
            '''
            Get is a member method. 
            This method retrieves an overview attribute for a specified IPv4 or IPv6 address, 
            including data for area, location, carrier, threat assessment, and more.
            '''

            try:
                
                response_body, response_headers = self.service_client.request_rest_api(
                    request_type = Enums.HttpRequestType.Get, 
                    request_url = '/insights/{IP_ADDRESS}'.format(
                        IP_ADDRESS = self.ip_address if self.ip_address else '0.0.0.0'
                    )
                )

                self.code = response_body['code']
                self.message = response_body['message']
                self.request_id = response_body['requestId']

                self.property.region.country_name = response_body['result']['region']['countryName']
                self.property.region.province_name = response_body['result']['region']['provinceName']
                self.property.region.city_name = response_body['result']['region']['cityName']
                self.property.region.county_name = response_body['result']['region']['countyName']

                self.property.location.timezone_name = response_body['result']['location']['timezoneName']
                self.property.location.longitude_number = response_body['result']['location']['longitudeNumber']
                self.property.location.latitude_number = response_body['result']['location']['latitudeNumber']

                self.property.provider.isp_names = (list(response_body['result']['provider']['ispNames']) 
                    if response_body['result']['provider']['ispNames'] else None)
                self.property.provider.isp_types = (list(response_body['result']['provider']['ispTypes']) 
                    if response_body['result']['provider']['ispTypes'] else None)
                self.property.provider.as_number = response_body['result']['provider']['asNumber']
                self.property.provider.as_name = response_body['result']['provider']['asName']

                self.property.threat.timestamp = response_body['result']['threat']['timestamp']
                self.property.threat.exponent = response_body['result']['threat']['exponent']
                self.property.threat.tags = (list(response_body['result']['threat']['tags']) 
                    if response_body['result']['threat']['tags'] else None)
                
                self.property.other.source_ip.ipv4 = response_body['result']['other']['sourceIp']['ipv4']
                self.property.other.source_ip.ipv6 = response_body['result']['other']['sourceIp']['ipv6']
                self.property.other.ip_version = response_body['result']['other']['ipVersion']

                self.headers.version = response_headers['X-Api-Version']
                self.headers.time_spend = response_headers['X-Api-Time-Spend']

                return self.property
            
            except UnexpectedError as exception_context:
                raise exception_context

            except Exception as exception_context:
                
                print('{MODULE_NAME}.py::Collections.Insights.get -> {EXCEPTION_TEXT}'.format(
                    MODULE_NAME = __name__, 
                    EXCEPTION_TEXT = str(exception_context)
                ))

                raise UnexpectedError(exception_context)

        
        # define region function

        def region(self) -> RegionAccessor:
            '''
            A region is a member method. 
            This method retrieves the geographic location attribute for the specified IPv4 or IPv6 address.
            '''

            try:

                response_body, response_headers = self.service_client.request_rest_api(
                    request_type = Enums.HttpRequestType.Get, 
                    request_url = '/insights/{IP_ADDRESS}/region'.format(
                        IP_ADDRESS = self.ip_address if self.ip_address else '0.0.0.0'
                    )
                )

                accessor_context: RegionAccessor = RegionAccessor()
                
                accessor_context.code = response_body['code']
                accessor_context.message = response_body['message']
                accessor_context.request_id = response_body['requestId']

                accessor_context.property.country_name = response_body['result']['countryName']
                accessor_context.property.province_name = response_body['result']['provinceName']
                accessor_context.property.city_name = response_body['result']['cityName']
                accessor_context.property.county_name = response_body['result']['countyName']

                accessor_context.headers.version = response_headers['X-Api-Version']
                accessor_context.headers.time_spend = response_headers['X-Api-Time-Spend']

                return accessor_context

            except UnexpectedError as exception_context:
                raise exception_context

            except Exception as exception_context:

                print('{MODULE_NAME}.py::Collections.Insights.region -> {EXCEPTION_TEXT}'.format(
                    MODULE_NAME = __name__, 
                    EXCEPTION_TEXT = str(exception_context)
                ))

                raise UnexpectedError(exception_context)

        # define location function

        def location(self):
            '''
            Location is a member method. 
            This method is used to retrieve the location attribute of a specified IPv4 or IPv6 address.
            '''

            try:

                response_body, response_headers = self.service_client.request_rest_api(
                    request_type = Enums.HttpRequestType.Get, 
                    request_url = '/insights/{IP_ADDRESS}/location'.format(
                        IP_ADDRESS = self.ip_address if self.ip_address else '0.0.0.0'
                    )
                )

                accessor_context: LocationAccessor = LocationAccessor()
                
                accessor_context.code = response_body['code']
                accessor_context.message = response_body['message']
                accessor_context.request_id = response_body['requestId']

                accessor_context.property.timezone_name = response_body['result']['timezoneName']
                accessor_context.property.longitude_number = response_body['result']['longitudeNumber']
                accessor_context.property.latitude_number = response_body['result']['latitudeNumber']

                accessor_context.headers.version = response_headers['X-Api-Version']
                accessor_context.headers.time_spend = response_headers['X-Api-Time-Spend']

                return accessor_context

            except UnexpectedError as exception_context:
                raise exception_context

            except Exception as exception_context:

                print('{MODULE_NAME}.py::Collections.Insights.location -> {EXCEPTION_TEXT}'.format(
                    MODULE_NAME = __name__, 
                    EXCEPTION_TEXT = str(exception_context)
                ))

                raise UnexpectedError(exception_context)

        # define provider function

        def provider(self):
            '''
            provider is a member method. 
            This method is used to retrieve carrier attributes for a specified IPv4 or IPv6 address.
            '''

            try:

                response_body, response_headers = self.service_client.request_rest_api(
                    request_type = Enums.HttpRequestType.Get, 
                    request_url = '/insights/{IP_ADDRESS}/provider'.format(
                        IP_ADDRESS = self.ip_address if self.ip_address else '0.0.0.0'
                    )
                )

                accessor_context: ProviderAccessor = ProviderAccessor()
                
                accessor_context.code = response_body['code']
                accessor_context.message = response_body['message']
                accessor_context.request_id = response_body['requestId']

                accessor_context.property.isp_names = (list(response_body['result']['ispNames']) 
                    if response_body['result']['ispNames'] else None)
                accessor_context.property.isp_types = (list(response_body['result']['ispTypes']) 
                    if response_body['result']['ispTypes'] else None)
                accessor_context.property.as_number = response_body['result']['asNumber']
                accessor_context.property.as_name = response_body['result']['asName']

                accessor_context.headers.version = response_headers['X-Api-Version']
                accessor_context.headers.time_spend = response_headers['X-Api-Time-Spend']

                return accessor_context

            except UnexpectedError as exception_context:
                raise exception_context

            except Exception as exception_context:

                print('{MODULE_NAME}.py::Collections.Insights.provider -> {EXCEPTION_TEXT}'.format(
                    MODULE_NAME = __name__, 
                    EXCEPTION_TEXT = str(exception_context)
                ))

                raise UnexpectedError(exception_context)

        # define provider function

        def threat(self):
            '''
            threat is a member method. 
            This method is used to retrieve threat assessment properties for a specified IPv4 or IPv6 address.
            '''

            try:

                response_body, response_headers = self.service_client.request_rest_api(
                    request_type = Enums.HttpRequestType.Get, 
                    request_url = '/insights/{IP_ADDRESS}/threat'.format(
                        IP_ADDRESS = self.ip_address if self.ip_address else '0.0.0.0'
                    )
                )

                accessor_context: ThreatAccessor = ThreatAccessor()
                
                accessor_context.code = response_body['code']
                accessor_context.message = response_body['message']
                accessor_context.request_id = response_body['requestId']

                accessor_context.property.timestamp = response_body['result']['timestamp']
                accessor_context.property.exponent = response_body['result']['exponent']
                accessor_context.property.tags = (list(response_body['result']['tags']) 
                    if response_body['result']['tags'] else None)

                accessor_context.headers.version = response_headers['X-Api-Version']
                accessor_context.headers.time_spend = response_headers['X-Api-Time-Spend']

                return accessor_context

            except UnexpectedError as exception_context:
                raise exception_context

            except Exception as exception_context:

                print('{MODULE_NAME}.py::Collections.Insights.threat -> {EXCEPTION_TEXT}'.format(
                    MODULE_NAME = __name__, 
                    EXCEPTION_TEXT = str(exception_context)
                ))

                raise UnexpectedError(exception_context)

        # define other function

        def other(self):
            '''
            other is a member method. 
            This method is used to retrieve additional additional attributes for a specified IPv4 or IPv6 address.
            '''

            try:

                response_body, response_headers = self.service_client.request_rest_api(
                    request_type = Enums.HttpRequestType.Get, 
                    request_url = '/insights/{IP_ADDRESS}/other'.format(
                        IP_ADDRESS = self.ip_address if self.ip_address else '0.0.0.0'
                    )
                )

                accessor_context: OtherAccessor = OtherAccessor()
                
                accessor_context.code = response_body['code']
                accessor_context.message = response_body['message']
                accessor_context.request_id = response_body['requestId']

                accessor_context.property.ipv4.query_ip.decimal = response_body['result']['ipv4']['queryIp']['decimal']
                accessor_context.property.ipv4.query_ip.address = response_body['result']['ipv4']['queryIp']['address']
                accessor_context.property.ipv4.source_ip.decimal = response_body['result']['ipv4']['sourceIp']['decimal']
                accessor_context.property.ipv4.source_ip.address = response_body['result']['ipv4']['sourceIp']['address']

                accessor_context.property.ipv6.query_ip.decimal = response_body['result']['ipv6']['queryIp']['decimal']
                accessor_context.property.ipv6.query_ip.address = response_body['result']['ipv6']['queryIp']['address']
                accessor_context.property.ipv6.source_ip.decimal = response_body['result']['ipv6']['sourceIp']['decimal']
                accessor_context.property.ipv6.source_ip.address = response_body['result']['ipv6']['sourceIp']['address']

                accessor_context.headers.version = response_headers['X-Api-Version']
                accessor_context.headers.time_spend = response_headers['X-Api-Time-Spend']

                return accessor_context

            except UnexpectedError as exception_context:
                raise exception_context

            except Exception as exception_context:

                print('{MODULE_NAME}.py::Collections.Insights.other -> {EXCEPTION_TEXT}'.format(
                    MODULE_NAME = __name__, 
                    EXCEPTION_TEXT = str(exception_context)
                ))

                raise UnexpectedError(exception_context)
