import operations.cumulus_operations as cumulus
import models.data.chq_test_data as data
import operations.my_operations as myops

import logging
logging.basicConfig(level=logging.DEBUG)

# Data Map for Resource Group
location = data.my_location
GROUP_NAME = data.GROUP_NAME

# Data for Virtual Network
VNET_NAME = data.VNET_NAME
VNET_PREFIXES = data.VNET_PREFIXES
DNS_SERVERS = data.DNS_SERVERS

# Data for Subnet
SUBNET_NAME = data.GW_SUBNET_NAME
SUBNET_PREFIX = data.GW_SUBNET_PREFIX

# Data for Public IP Address
GW_IP_NAME = data.GW_IP_NAME

# Data for Local Network Gateway
LN_GW_IP = data.LN_GW_IP
LN_ASN = data.LN_ASN
BGP_PEER_IP = data.BGP_PEER_IP
LN_GW_NAME = data.LN_GW_NAME
LN_GW_PREFIXES = data.LN_GW_PREFIXES

# Data for Virtual Network Gateway
VNET_ASN = data.VNET_ASN
GW_NAME = data.GW_NAME

# Data for Virtual Network Gateway Connection
SHARED_KEY = data.SHARED_KEY
CONNECTION = data.CONNECTION

resource_set = []


# Create Resource Group
#**********************

print("Creating resource group...")

rg_parameters = {'location': location}

# cumulus.create_update_resource_group(
#     GROUP_NAME,
#     rg_parameters
# )

# resource_set.append(
#     cumulus.get_resource_group(
#         GROUP_NAME
#     )
# )


# Create Virtual Network
#***********************

print("Creating virtual network...")

vnet_parameters = {'location': location,
                   'address_space':
                       {'address_prefixes': VNET_PREFIXES},
                   'dhcp_options':
                       {'dns_servers': DNS_SERVERS}
                   }

# cumulus.create_update_virtual_networks(
#     GROUP_NAME,
#     VNET_NAME,
#     vnet_parameters
# )

resource_set.append(
    cumulus.get_virtual_networks(
        GROUP_NAME,
        VNET_NAME
    )
)


# Create Virtual Network Gateway
#*******************************

print("Creating virtual network gateway...")

subnet_info = cumulus.get_subnets(
    GROUP_NAME,
    VNET_NAME,
    SUBNET_NAME
)

public_ip_address_info = cumulus.get_public_ip_addresses(
    GROUP_NAME,
    GW_IP_NAME
)

vng_parameters = {'location': location,
                  'ip_configurations': [
                      {'name': 'Default',
                       'subnet': {
                           'id': subnet_info.id},
                        'public_ip_address': {
                            'id': public_ip_address_info.id}
                       }
                  ],
                  'gateway_type': 'Vpn',
                  'vpn_type': 'RouteBased',
                  'enable_bgp': True,
                  'bgp_settings': {
                      'asn': VNET_ASN},
                  'sku': {
                      'name': 'HighPerformance',
                      'tier': 'HighPerformance'}
                  }

# cumulus.create_update_virtual_network_gateways(
#     GROUP_NAME,
#     GW_NAME,
#     vng_parameters
# )

resource_set.append(
    cumulus.get_virtual_network_gateways(
        GROUP_NAME,
        GW_NAME
    )
)


# Create Virtual Network Gateway Connection
#******************************************

print("Creating virtual network gateway connection...")

virtual_network_gateway_info = cumulus.get_virtual_network_gateways(
    GROUP_NAME,
    GW_NAME
)

local_network_gateway_info = cumulus.get_local_network_gateways(
    'CHQ_Core_BGP_RG',
    LN_GW_NAME
)

vngc_parameters = {'location': location,
                   'virtual_network_gateway1': {
                       'id': virtual_network_gateway_info.id},
                   'local_network_gateway2': {
                       'id': local_network_gateway_info.id},
                   'connection_type': 'IPSec',
                   'shared_key': SHARED_KEY,
                   'enable_bgp': True
                   }

# cumulus.create_update_virtual_network_gateway_connections(
#     GROUP_NAME,
#     CONNECTION,
#     vngc_parameters
# )

resource_set.append(
    cumulus.get_virtual_network_gateway_connections(
        GROUP_NAME,
        CONNECTION
    )
)

# Summary Report of Resource Parameters
myops.workflow_summary(resource_set)


# Cascading deletes for debugging purposes
# cumulus.delete_virtual_network_gateway_connections(
#     GROUP_NAME,
#     CONNECTION
# )
#
# cumulus.delete_virtual_network_gateways(
#     GROUP_NAME,
#     GW_NAME
# )
#
# cumulus.delete_local_network_gateways(
#     GROUP_NAME,
#     LN_GW_NAME
# )


#************************* end of gateway_workflow.py *************************