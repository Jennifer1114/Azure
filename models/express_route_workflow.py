import operations.cumulus_operations as cumulus
import models.data.pgm_test_data as test_data
import operations.my_operations as resource

# import logging
# logging.basicConfig(level=logging.DEBUG)

# Build the Data Map
#*******************

# Data for Resource Group
location = test_data.my_location
GROUP_NAME = test_data.GROUP_NAME

# Data for Express Route Circuit
CIRCUIT_NAME = test_data.CIRCUIT_NAME
SERVICE_PROVIDER_NAME = test_data.SERVICE_PROVIDER_NAME
PEERING_LOCATION = test_data.PEERING_LOCATION
ERC_BANDWIDTH = test_data.ERC_BANDWIDTH

CIRCUIT_PEERING_NAME = test_data.CIRCUIT_PEERING_NAME
PEER_ASN = test_data.PEER_ASN
PEER_VLAN_ID = test_data.PEER_VLAN_ID
PRIMARY_PEER_PREFIX = test_data.PRIMARY_PEER_PREFIX
SECONDARY_PEER_PREFIX = test_data.SECONDARY_PEER_PREFIX

CIRCUIT_AUTHORIZATION_NAME = test_data.CIRCUIT_AUTHORIZATION_NAME

# Data for Virtual Network
VNET_NAME = test_data.VNET_NAME
VNET_PREFIXES = test_data.VNET_PREFIXES
DNS_SERVERS = test_data.DNS_SERVERS

# Data for Subnet
SUBNET_NAME = test_data.FE_SUBNET_NAME
SUBNET_PREFIX = test_data.FE_SUBNET_PREFIX

GW_SUBNET_NAME = test_data.GW_SUBNET_NAME
GW_SUBNET_PREFIX = test_data.GW_SUBNET_PREFIX

# Data for Public IP Address
GW_IP_NAME = test_data.GW_IP_NAME

# Data for Virtual Network Gateway and Connection
PEER_GW_NAME = test_data.PEER_GW_NAME
CONNECTION = test_data.CONNECTION

resource_set = []


# Create Resource Group
#**********************

print("Creating resource group...")

rg_parameters = {'location': location}

# cumulus.create_update_resource_group(
#     GROUP_NAME,
#     rg_parameters)


# Create Express Route Circuit
#*****************************

print("Creating express route circuit...")

erc_parameters = {'location': location,
                  'service_provider_properties':
                      {'service_provider_name': SERVICE_PROVIDER_NAME,
                       'peering_location': PEERING_LOCATION,
                       'bandwidth_in_mbps': ERC_BANDWIDTH},
                  'sku':
                      {'name': 'Premium_MeteredData',
                       'tier': 'Premium',
                       'family': 'MeteredData'}}

# cumulus.create_update_express_route_circuits(
#     GROUP_NAME,
#     CIRCUIT_NAME,
#     erc_parameters)


resource_set.append(
    cumulus.get_express_route_circuits(
        GROUP_NAME,
        CIRCUIT_NAME))


# Create Express Route Circuit Peering
#*************************************

print("Creating express route circuit azure private peering...")

ercp_parameters = {'peering_type': 'AzurePrivatePeering',
                   'peer_asn': PEER_ASN,
                   'primary_peer_address_prefix': PRIMARY_PEER_PREFIX,
                   'secondary_peer_address_prefix': SECONDARY_PEER_PREFIX,
                   'vlan_id': PEER_VLAN_ID}

# cumulus.create_update_express_route_circuit_peerings(
#     GROUP_NAME,
#     CIRCUIT_NAME,
#     CIRCUIT_PEERING_NAME,
#     ercp_parameters)


resource_set.append(
    cumulus.get_express_route_circuit_peerings(
        GROUP_NAME,
        CIRCUIT_NAME,
        CIRCUIT_PEERING_NAME))


# Create Express Route Circuit Authorization
#*******************************************

print("Creating express route circuit authorization...")

erca_parameters = {}

# cumulus.create_update_express_route_circuit_authorizations(
#     GROUP_NAME,
#     CIRCUIT_NAME,
#     CIRCUIT_AUTHORIZATION_NAME,
#     erca_parameters)


resource_set.append(
    cumulus.get_express_route_circuit_authorizations(
        GROUP_NAME,
        CIRCUIT_NAME,
        CIRCUIT_AUTHORIZATION_NAME))


# Create Virtual Network
#***********************

print("Creating virtual network...")

vnet_parameters = {'location': location,
                   'address_space':
                       {'address_prefixes': VNET_PREFIXES}}

# cumulus.create_update_virtual_networks(
#     GROUP_NAME,
#     VNET_NAME,
#     vnet_parameters)


resource_set.append(
    cumulus.get_virtual_networks(
        GROUP_NAME,
        VNET_NAME))


# Create Subnet
#**************

print("Creating gateway subnet...")

subnet_parameters = {'address_prefix': GW_SUBNET_PREFIX}

# cumulus.create_update_subnets(
#     GROUP_NAME,
#     VNET_NAME,
#     GW_SUBNET_NAME,
#     subnet_parameters)


resource_set.append(
    cumulus.get_subnets(
        GROUP_NAME,
        VNET_NAME,
        GW_SUBNET_NAME))

print("Creating front end subnet...")

subnet_parameters = {'address_prefix': SUBNET_PREFIX}

# cumulus.create_update_subnets(
#     GROUP_NAME,
#     VNET_NAME,
#     SUBNET_NAME,
#     subnet_parameters)


resource_set.append(
    cumulus.get_subnets(
        GROUP_NAME,
        VNET_NAME,
        SUBNET_NAME))


# Create Public IP Address
#*************************

print("Creating Public IP Address...")

pip_parameters = {'location': location,
                  'public_ip_allocation_method': 'Dynamic'}

# cumulus.create_update_public_ip_addresses(
#     GROUP_NAME,
#     GW_IP_NAME,
#     pip_parameters)


resource_set.append(
    cumulus.get_public_ip_addresses(
        GROUP_NAME,
        GW_IP_NAME))


# Create Virtual Network Gateway
#*******************************

print("Creating virtual network gateway...")

gw_subnet_info = cumulus.get_subnets(
    GROUP_NAME,
    VNET_NAME,
    SUBNET_NAME)

public_ip_address_info = cumulus.get_public_ip_addresses(
    GROUP_NAME,
    GW_IP_NAME)

vng_parameters = {'location': location,
                  'ip_configurations': [
                      {'name': 'gwipconf',
                       'subnet': {
                           'id': gw_subnet_info.id},
                        'public_ip_address': {
                            'id': public_ip_address_info.id}}],
                  'gateway_type': 'ExpressRoute',
                  'sku': {
                      'name': 'Standard',
                      'tier': 'Standard'}}

# cumulus.create_update_virtual_network_gateways(
#     GROUP_NAME,
#     PEER_GW_NAME,
#     vng_parameters)


resource_set.append(
    cumulus.get_virtual_network_gateways(
        GROUP_NAME,
        PEER_GW_NAME))


# Create Virtual Network Gateway Connection
#******************************************

print("Creating virtual network gateway connection...")

virtual_network_gateway_info = cumulus.get_virtual_network_gateways(
    GROUP_NAME,
    PEER_GW_NAME)

express_route_circuit_peering_info = cumulus.get_express_route_circuits(
    GROUP_NAME,
    CIRCUIT_NAME)

vngc_parameters = {'location': location,
                   'virtual_network_gateway1': {
                       'id': virtual_network_gateway_info.id},
                   'connection_type': 'ExpressRoute',
                   'peer': {
                       'id': express_route_circuit_peering_info.id}
                   }

# cumulus.create_update_virtual_network_gateway_connections(
#     GROUP_NAME,
#     CONNECTION,
#     vngc_parameters)


resource_set.append(
    cumulus.get_virtual_network_gateway_connections(
        GROUP_NAME,
        CONNECTION))


print("Summary of resources created in the express route workflow...")

resource.workflow_summary(resource_set)


# ------------------------- END OF EXPRESS_ROUTE_WORKFLOW.PY -----------------