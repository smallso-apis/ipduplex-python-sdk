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

        def get(self) -> OverviewAccessor:
            '''
            Get is a member method. 
            This method retrieves an overview attribute for a specified IPv4 or IPv6 address, 
            including data for area, location, carrier, threat assessment, and more.

            REST API: /insights/:ipAddress
            '''

            try:
                
                response_result: dict = self.service_client.request_rest_api(
                    request_type = Enums.HttpRequestType.Get, 
                    request_url = '/insights/{IP_ADDRESS}'.format(
                        IP_ADDRESS = self.ip_address if self.ip_address else '0.0.0.0'
                    )
                )

                self.code = response_result['code']
                self.message = response_result['message']
                self.request_id = response_result['requestId']

                self.property.region.country_name = response_result['result']['region']['countryName']
                self.property.region.province_name = response_result['result']['region']['provinceName']
                self.property.region.city_name = response_result['result']['region']['cityName']
                self.property.region.county_name = response_result['result']['region']['countyName']

                self.property.location.timezone_name = response_result['result']['location']['timezoneName']
                self.property.location.longitude_number = response_result['result']['location']['longitudeNumber']
                self.property.location.latitude_number = response_result['result']['location']['latitudeNumber']

                self.property.provider.isp_names = (list(response_result['result']['provider']['ispNames']) 
                    if response_result['result']['provider']['ispNames'] else None)
                self.property.provider.isp_types = (list(response_result['result']['provider']['ispTypes']) 
                    if response_result['result']['provider']['ispTypes'] else None)
                self.property.provider.as_number = response_result['result']['provider']['asNumber']
                self.property.provider.as_name = response_result['result']['provider']['asName']

                self.property.threat.timestamp = response_result['result']['threat']['timestamp']
                self.property.threat.exponent = response_result['result']['threat']['exponent']
                self.property.threat.tags = (list(response_result['result']['threat']['tags']) 
                    if response_result['result']['threat']['tags'] else None)
                
                self.property.other.source_ip.ipv4 = response_result['other']['sourceIp']['ipv4']
                self.property.other.source_ip.ipv6 = response_result['other']['sourceIp']['ipv6']
                self.property.other.ip_version = response_result['other']['ipVersion']

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

                response_result: dict = self.service_client.request_rest_api(
                    request_type = Enums.HttpRequestType.Get, 
                    request_url = '/insights/{IP_ADDRESS}/region'.format(
                        IP_ADDRESS = self.ip_address if self.ip_address else '0.0.0.0'
                    )
                )

                accessor_context: RegionAccessor = RegionAccessor()
                
                accessor_context.code = response_result['code']
                accessor_context.message = response_result['message']
                accessor_context.request_id = response_result['requestId']

                accessor_context.property.country_name = response_result['result']['countryName']
                accessor_context.property.province_name = response_result['result']['provinceName']
                accessor_context.property.city_name = response_result['result']['cityName']
                accessor_context.property.county_name = response_result['result']['countyName']

                return accessor_context

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

                response_result: dict = self.service_client.request_rest_api(
                    request_type = Enums.HttpRequestType.Get, 
                    request_url = '/insights/{IP_ADDRESS}/location'.format(
                        IP_ADDRESS = self.ip_address if self.ip_address else '0.0.0.0'
                    )
                )

                accessor_context: LocationAccessor = LocationAccessor()
                
                accessor_context.code = response_result['code']
                accessor_context.message = response_result['message']
                accessor_context.request_id = response_result['requestId']

                accessor_context.property.timezone_name = response_result['result']['timezoneName']
                accessor_context.property.longitude_number = response_result['result']['longitudeNumber']
                accessor_context.property.latitude_number = response_result['result']['latitudeNumber']

                return accessor_context

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

                response_result: dict = self.service_client.request_rest_api(
                    request_type = Enums.HttpRequestType.Get, 
                    request_url = '/insights/{IP_ADDRESS}/provider'.format(
                        IP_ADDRESS = self.ip_address if self.ip_address else '0.0.0.0'
                    )
                )

                accessor_context: ProviderAccessor = ProviderAccessor()
                
                accessor_context.code = response_result['code']
                accessor_context.message = response_result['message']
                accessor_context.request_id = response_result['requestId']

                accessor_context.property.isp_names = (list(response_result['result']['ispNames']) 
                    if response_result['result']['ispNames'] else None)
                accessor_context.property.isp_types = (list(response_result['result']['ispTypes']) 
                    if response_result['result']['ispTypes'] else None)
                accessor_context.property.as_number = response_result['result']['asNumber']
                accessor_context.property.as_name = response_result['result']['asName']

                return accessor_context

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

                response_result: dict = self.service_client.request_rest_api(
                    request_type = Enums.HttpRequestType.Get, 
                    request_url = '/insights/{IP_ADDRESS}/threat'.format(
                        IP_ADDRESS = self.ip_address if self.ip_address else '0.0.0.0'
                    )
                )

                accessor_context: ThreatAccessor = ThreatAccessor()
                
                accessor_context.code = response_result['code']
                accessor_context.message = response_result['message']
                accessor_context.request_id = response_result['requestId']

                accessor_context.property.timestamp = response_result['result']['timestamp']
                accessor_context.property.exponent = response_result['result']['exponent']
                accessor_context.property.tags = (list(response_result['result']['tags']) 
                    if response_result['result']['tags'] else None)

                return accessor_context

            except Exception as exception_context:

                print('{MODULE_NAME}.py::Collections.Insights.threat -> {EXCEPTION_TEXT}'.format(
                    MODULE_NAME = __name__, 
                    EXCEPTION_TEXT = str(exception_context)
                ))

                raise UnexpectedError(exception_context)
