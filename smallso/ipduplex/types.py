# smallso.ipduplex.types.py is python-3.7.3 source file

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

# define Types static class

class Types:
    '''
    Types is a static class. 
    This class contains multiple data structure member static classes.
    '''

    # define RegionResult class

    class RegionResult:
        '''
        RegionResult is a dynamic class. Members of this class 
        indicate the properties of the geographic location.

        member str country_name: Indicate the country name. 
            If it is unknown, the value of this property will be set to None.
        
        member str province_name: Indicate the name of the province or state. 
            If it is unknown, the value of this property will be set to None.
        
        member str city_name: Indicate the city name. 
            If it is unknown, the value of this property will be set to None.
        
        member str county_name: Indicate the district name. 
            If it is unknown, the value of this property will be set to None.
        '''

        # define __init__ function

        def __init__(self):

            self.country_name: str = None
            self.province_name: str = None
            self.city_name: str = None
            self.county_name: str = None

    # define LocationResult class

    class LocationResult:
        '''
        A LocationResult is a dynamic class whose members indicate the 
        properties of the location.

        member str timezone_name: Indicates the name of the time zone in the location. 
            If it is unknown, the value of this property will be set to None.

        member float longitude_number: Indicates that the location accuracy is city-level longitude. 
            If it is unknown, the value of this property will be set to None.

        member float latitude_number: Indicates that the location accuracy is city-level latitude. 
            If it is unknown, the value of this property will be set to None.
        '''

        # define __init__ function

        def __init__(self):

            self.timezone_name: str = None
            self.longitude_number: float = None
            self.latitude_number: float = None

    # define ProviderResult class

    class ProviderResult:
        '''
        ProviderResult is a dynamic class. 
        Members of this class indicate the attributes of the carrier.

        member list isp_names: Contains array objects that indicate multiple carrier names. 
            For example, Tencent and Tencent Cloud are different carrier names because 
            Tencent Cloud's carrier is Tencent. Therefore, 2 members are generated in the 
            value of this attribute. If it is unknown, the value of this property will be set to None.

        member list isp_types: Contains array objects that indicate multiple carrier types. 
            Members of this attribute may be, for example, Data Center, Internet Cafe, 
            Family Broadband, and so on. Currently this property is pre-reserved and 
            its value will be unconditionally set to None.

        member int as_number: Indicates the carrier's Autonomous System number (abbreviation: ASN). 
            If it is unknown, the value of this property will be set to None.

        member str as_name: Indicates the carrier's Autonomous System name (abbreviation: ASN). 
            Typically, the value of this property contains the owner name of the property asNumber . 
            If it is unknown, the value of this property will be set to None.
        '''

        # define __init__ function

        def __init__(self):

            self.isp_names: list = None
            self.isp_types: list = None
            self.as_number: int = None
            self.as_name: str = None

    # define ThreatResult class

    class ThreatResult:
        '''
        ThreatResult is a dynamic class. 
        Members of this class indicate the attributes of the threat assessment.

        member int timestamp: Indicates the creation of a UNIX timestamp for the threat definition. 
            If it is unknown, the value of this property will be set to None.

        member str exponent: Indicates the threat assessment level. 
            This property has the following values:

                Trusted: trusted
                Low: low threat level
                Middle: medium threat level
                High: high threat level

            If it is unknown, the value of this property will be set to NULL.

        member list tags: Contains an array object indicating the threat assessment tag. 
            The value of this attribute (including but not limited to) may be:

                C2: C&C server
                Ransomware: ransomware server
                Proxy: proxy server
                Tor:Tor anonymous web server
                Botnet: botnet server
                Web_scan: web scanning
                ......

            If it is unknown, the value of this property will be set to None.
        '''

        # define __init__ function

        def __init__(self):

            self.timestamp: int = None
            self.exponent: str = None
            self.tags: list = None

    # define OtherResult class

    class OtherResult:
        '''
        OtherResult is a dynamic class. 
        Members of this class indicate properties for extra extensions.

        member OtherResult.SourceIp source_ip: Contains a OtherResult.SourceIp object 
            that indicates the source property of the API call.

        member str ip_version: Indicates the IP protocol version to which the retrieved 
            IP address belongs. If the IP address type is IPv4, the value of this attribute 
            will be set to IPv4; if the IP address type is IPv6, the value of this attribute 
            will be set to IPv6; if the IP address type is unknown, the value of this attribute 
            will be set to None.
        '''

        # define SourceIp class

        class SourceIp:
            '''
            Contains a OtherResult.SourceIp object 
            that indicates the source property of the API call.

            member str ipv4: Indicates the IPv4 address of the source of the API call. 
                If an API call request is made over an IPv6 network, the value of this property will be set to None.
            
            member str ipv6: Indicates the IPv6 address of the source of the API call. 
                If an invocation request is made over an IPv4 network, the value of this attribute will be set to 
                its IPv4 IPv6 mapped address ::ffff:.
            '''
            
            # define __init__ function

            def __init__(self):

                self.ipv4: str = None
                self.ipv6: str = None

        # define __init__ function

        def __init__(self):

            self.source_ip: OtherResult.SourceIp = Types.OtherResult.SourceIp()
            self.ip_version: str = None

    # define OtherResultEx class

    class OtherResultEx:
        '''
        OtherResultEx is a dynamic class. 
        Members of this class indicate properties for extra extensions.

        The OtherResultEx class is an extension of OtherResult.

        member Types.OtherResultEx.AnyIPVersion ipv4: Contains Types.OtherResultEx.AnyIPVersion objects 
            that indicate IPv4 related properties.

        member Types.OtherResultEx.AnyIPVersion ipv6: Contains Types.OtherResultEx.AnyIPVersion objects 
            that indicate IPv6 related properties.
        '''

        # define AnyIP class

        class AnyIP:
            '''
            member int decimal: 
                When the current IP version is IPv4:

                    When the IP type is Query IP:

                        Indicates the decimal value of the retrieved IPv4 address. 
                            If the retrieved IP address is IPv6, the value of this attribute will be set to None.
                    
                    When the IP type is Source IP:

                        Indicates the decimal value of the API call request source IPv4 address. 
                            If an API call request is made over an IPv6 network, the value of this property will be set to None.
                
                When the current IP version is IPv6:

                    When the IP type is Query IP:

                        Indicates the decimal value of the IPv6 address being retrieved. 
                            If the retrieved IP address is IPv4, the value of this attribute will be set to 
                            the decimal value of the IPv6 mapped address ::ffff: of the IPv4 address.
                    
                    When the IP type is Source IP:

                        Indicates the IPv4 address of the source of the API call request. 
                        If an API call request is made over an IPv6 network, the value of this property will be set to None.
            
            member str address:
                When the current IP version is IPv4:

                    When the IP type is Query IP:

                        Indicates the IPv4 address being retrieved. 
                            If the retrieved IP address is IPv6, the value of this attribute will be set to None.
                    
                    When the IP type is Source IP:

                        Indicates the IPv4 address of the source of the API call request. 
                            If an API call request is made over an IPv6 network, the value of this property will be set to None.

                When the current IP version is IPv6:
                    
                    When the IP type is Query IP:

                        Indicates the IPv6 address being retrieved. 
                            If the retrieved IP address is IPv4, the value of this attribute will be set to the 
                            IPv6 mapped address of the IPv4 address: ::ffff:.

                    When the IP type is Source IP:

                        Indicates the IPv6 address of the source of the API call request. 
                            If an API call request is initiated over an IPv4 network, the value of this attribute will 
                            be set to the IPv6 mapped address of the IPv4 address: ::ffff:.
            '''

            # define __init__ functuon

            def __init__(self):

                self.decimal: int = None
                self.address: str = None
        
        # define AnyIPVersion class

        class AnyIPVersion:
            '''
            member Types.OtherResultEx.AnyIP query_ip: 

                When the current IP version is IPv4:

                    Contains IPv4 related attributes that indicate the IP address being retrieved.

                When the current IP version is IPv6:

                    Contains IPv6 related attributes that indicate the IP address being retrieved.

            member Types.OtherResultEx.AnyIP source_ip:

                When the current IP version is IPv4:

                    Contains IPv4 related attributes that indicate the source IP address of the API call request.

                When the current IP version is IPv6:

                    Contains IPv6-related attributes that indicate the source IP address of the API call request.
            '''

            # define __init__ function

            def __init__(self):

                self.query_ip: Types.OtherResultEx.AnyIP = Types.OtherResultEx.AnyIP()
                self.source_ip: Types.OtherResultEx.AnyIP = Types.OtherResultEx.AnyIP()

        # define __init__ function

        def __init__(self):

            self.ipv4: Types.OtherResultEx.AnyIPVersion = Types.OtherResultEx.AnyIPVersion()
            self.ipv6: Types.OtherResultEx.AnyIPVersion = Types.OtherResultEx.AnyIPVersion()

    # define OverviewResult class

    class OverviewResult:
        '''
        OverviewResult is a dynamic class. 
        This class contains data objects that indicate geographic location, 
        location, carrier, threat assessment, and other additional extended attributes.

        member RegionResult region: Contains a regionResult object indicating that the geographic 
            location property of the IPv4 or IPv6 address is retrieved.

        member LocationResult location: Contains a locationResult object indicating the property 
            at which the IPv4 or IPv6 address is retrieved.

        member ProviderResult provider: Contains a providerResult object indicating that the IPv4 
            or IPv6 address operator attribute was retrieved.

        member ThreatResult threat: Contains a threatResult object indicating that the IPv4 or IPv6 
            address threat assessment attribute was retrieved.

        member OtherResult other: Contains a otherResult object indicating that additional extra 
            extended attributes are being retrieved for the IPv4 or IPv6 address.
        '''

        # define __init__ function

        def __init__(self):

            self.region: Types.RegionResult = Types.RegionResult()
            self.location: Types.LocationResult = Types.LocationResult()
            self.provider: Types.ProviderResult = Types.ProviderResult()
            self.threat: Types.ThreatResult = Types.ThreatResult()
            self.other: Types.OtherResult = Types.OtherResult()

    # define HeaderResult class

    class HeaderResult:
        '''
        HeaderResult is a dynamic class. 
        This class indicates the HTTP response headers that are available for use.

        member str version: Indicates the version of the Cloud API service that was invoked this time.

        member str time_spend: Indicates the processing time of this API call request Cloud API. 
            If the processing time is undetermined, the value of this header will be set to not-sure.
        '''

        # define __init__ function

        def __init__(self):

            self.version: str = None
            self.time_spend: str = None

    # define AnyResult class

    class AnyResult:
        '''
        AnyResult is a dynamic class. 
        Members of this class indicate the shared properties of all IP Duplex API request responses.
        '''

        # define __init__ function

        def __init__(self):

            self.code: int = None
            self.message: str = None
            self.request_id: str = None


# define Enums static class

class Enums:
    '''
    Enums is a static class. 
    All subclasses of this class indicate an enumerator.
    '''

    # define HttpRequestType enum class

    class HttpRequestType:
        '''
        HttpRequestType is an enumerator. 
        This enumerator indicates the type of HTTP request method.
        '''

        Get: int = 1
        Head: int = 2
        Post: int = 3
        Put: int = 4
        Delete: int = 5
