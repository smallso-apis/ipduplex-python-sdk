# tests.tests.py is python-3.7.3 source file

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

from smallso.ipduplex.version import *
from smallso.ipduplex.accessor import *
from smallso.ipduplex.apps import *
from smallso.ipduplex.types import *

# define main function

def main():
    
    service_client: AppService = AppService(None)
    collection: Collections.Insights = service_client.insights(None)

    try:
        property_result: Types.RegionResult = collection.region().get()

        print((
            ' country name: {COUNTRY_NANE}\n'
            ' province name: {PROVINCE_NAME}\n'
            ' city name: {CITY_NAME}\n'
            ' county name: {COUNTY_NAME}'
        ).format(
            COUNTRY_NANE = property_result.country_name, 
            PROVINCE_NAME = property_result.province_name, 
            CITY_NAME = property_result.city_name, 
            COUNTY_NAME = property_result.province_name
        ), end = '\n\n')
    except NotFoundError:
        print(' (!) region unknown', end = '\n\n')

    try:
        property_result: Types.LocationResult = collection.location().get()

        print((
            ' timezone name: {TIMEZONE_NAME}\n'
            ' longitude number: {LONGITUDE_NUMBER}\n'
            ' latitude number: {LATITUDE_NUMBER}'
        ).format(
            TIMEZONE_NAME = property_result.timezone_name, 
            LONGITUDE_NUMBER = property_result.longitude_number, 
            LATITUDE_NUMBER = property_result.latitude_number
        ), end = '\n\n')
    except NotFoundError:
        print(' (!) location unknown', end = '\n\n')

    try:
        property_result: Types.ProviderResult = collection.provider().get()

        if property_result.isp_names:
            print(' isp names: ', end = '')

            for isp_name in property_result.isp_names:
                print('{ISP_NAME}\t'.format(
                        ISP_NAME = isp_name
                    ), end = '')
            else:
                print(end = '\n')
        else:
            print(' isp names: None')

        if property_result.isp_types:
            print(' isp types: ', end = '')

            for isp_type in property_result.isp_types:
                print('{ISP_TYPE}\t'.format(
                        ISP_TYPE = isp_type
                    ), end = '')
            else:
                print(end = '\n')
        else:
            print(' isp types: None')

        print((
            ' autonomous system number: {AS_NUMBER}\n'
            ' autonomous system name: {AS_NAME}'
        ).format(
            AS_NUMBER = property_result.as_number, 
            AS_NAME = property_result.as_name
        ), end = '\n\n')
    except NotFoundError:
        print(' (!) provider unknown', end = '\n\n')

    try:
        property_result: Types.ThreatResult = collection.threat().get()

        print((
            ' timestamp: {TIMESTAMP}\n'
            ' exponent: {EXPONENT}\n'
        ).format(
            TIMESTAMP = property_result.timestamp, 
            EXPONENT = property_result.exponent
        ), end = '')

        if property_result.tags:
            print(' tags: ', end = '')

            for tag in property_result.tags:
                print('{TAG}\t'.format(
                        TAG = tag
                    ), end = '')
            else:
                print(end = '\n\n')
        else:
            print(' tags: None', end = '\n\n')
    except NotFoundError:
        print(' (!) threat unknown', end = '\n\n')

    try:
        property_result: Types.OtherResultEx = collection.other().get()

        print((
            ' ipv4: \n\n'
                ' \tquery ip address: \n\n'
                    ' \t\tdecimal: {IPV4_QUERY_DECIMAL}\n'
                    ' \t\taddress: {IPV4_QUERY_ADDRESS}\n\n'
                ' \tsource ip address: \n\n'
                    ' \t\tdecimal: {IPV4_SOURCE_DECIMAL}\n'
                    ' \t\taddress: {IPV4_SOURCE_ADDRESS}\n\n'
            ' ipv6: \n\n'
                ' \tquery ip address: \n\n'
                    ' \t\tdecimal: {IPV6_QUERY_DECIMAL}\n'
                    ' \t\taddress: {IPV6_QUERY_ADDRESS}\n\n'
                ' \tsource ip address: \n\n'
                    ' \t\tdecimal: {IPV6_SOURCE_DECIMAL}\n'
                    ' \t\taddress: {IPV6_SOURCE_ADDRESS}'
        ).format(
            IPV4_QUERY_DECIMAL = property_result.ipv4.query_ip.decimal, 
            IPV4_QUERY_ADDRESS = property_result.ipv4.query_ip.address, 
            IPV4_SOURCE_DECIMAL = property_result.ipv4.source_ip.decimal, 
            IPV4_SOURCE_ADDRESS = property_result.ipv4.source_ip.address, 
            IPV6_QUERY_DECIMAL = property_result.ipv6.query_ip.decimal, 
            IPV6_QUERY_ADDRESS = property_result.ipv6.query_ip.address, 
            IPV6_SOURCE_DECIMAL = property_result.ipv6.source_ip.decimal, 
            IPV6_SOURCE_ADDRESS = property_result.ipv6.source_ip.address
        ), end = '\n\n')
    except NotFoundError:
        print(' (!) other unknown', end = '\n\n')

    try:
        property_result: Types.OverviewResult = collection.get()

        print(' Currently in: {COUNTRY_NAME} {PROVINCE_NAME} {CITY_NAME} {COUNTY_NAME} / {ISP_NAME}'.format(
            COUNTRY_NAME = property_result.region.country_name, 
            PROVINCE_NAME = property_result.region.province_name, 
            CITY_NAME = property_result.region.city_name, 
            COUNTY_NAME = property_result.region.county_name, 
            ISP_NAME = (property_result.provider.isp_names[0] if property_result.provider.isp_names and 
                len(property_result.provider.isp_names) > 0 else None)
        ), end = '\n\n')

    except NotFoundError:
        print(' (!) overview unknown', end = '\n\n')
