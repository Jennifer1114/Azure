import operations.cumulus_operations as cumulus
import operations.my_operations as resource
import models.data.pgm_core_data as data

# Using sample from AZURE Documentation
# https://github.com/Azure-Samples/network-python-manage-loadbalancer/blob/master/example.py

# import logging
# logging.basicConfig(level=logging.DEBUG)

# Build the Data Map
#*******************

# Data for Resource Group
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
PIP_NAME = data.STATIC_IP_NAME

# Data for Load Balancer
LOAD_BALANCER_NAME = data.LOAD_BALANCER_NAME

FE_IP_NAME = data.FE_IP_NAME

ADDRESS_POOL_NAME = data.ADDRESS_POOL_NAME

PROBE_NAME = data.PROBE_NAME

LOAD_BALANCER_RULE_NAME = data.LOAD_BALANCER_RULE_NAME

NETRULE_NAME_1 = data.NETRULE_NAME_1
NETRULE_NAME_2 = data.NETRULE_NAME_2

FRONTEND_PORT_1 = data.FRONTEND_PORT_1
FRONTEND_PORT_2 = data.FRONTEND_PORT_2
BACKEND_PORT = data.BACKEND_PORT

resource_set = []

# Create Resource Group
#**********************

print("Creating resource group...")

rg_parameters = {'location': location}

cumulus.create_update_resource_group(
    GROUP_NAME,
    rg_parameters)

resource_set.append(
    cumulus.get_resource_group(
        GROUP_NAME))


# Create Public IP Address
#*************************

print("Creating Public IP Address...")

pip_parameters = {'location': location,
                  'public_ip_allocation_method': 'Static'}

cumulus.create_update_public_ip_addresses(
    GROUP_NAME,
    PIP_NAME,
    pip_parameters)

resource_set.append(
    cumulus.get_public_ip_addresses(
        GROUP_NAME,
        PIP_NAME))


# Create Load Balancer Configurations
# ***********************************

# FrontEndIpPool
public_ip_info = cumulus.get_public_ip_addresses(
    GROUP_NAME,
    PIP_NAME)

frontend_ip_configurations = [{
    'name': FE_IP_NAME,
    'private_ip_allocation_method': 'Dynamic',
    'public_ip_address': {
        'id': public_ip_info.id}}]


# BackEndAddressPool
backend_ip_configurations = [{
    'name': ADDRESS_POOL_NAME}]


# HealthProbe
probe_configurations = [{
    'name': PROBE_NAME,
    'protocol': 'Http',
    'port': 80,
    'interval_in_seconds': 15,
    'number_of_probes': 4,
    'request_path': 'healthprobe.aspx'}]


# LoadBalancerRule
load_balancer_rule_configurations = [{
    'name': LOAD_BALANCER_RULE_NAME,
    'protocol': 'tcp',
    'frontend_port': 80,
    'backend_port': 80,
    'idle_timeout_in_minutes': 4,
    'enable_floating_ip': False,
    'load_distribution': 'Default',
    'frontend_ip_configuration': {
        'id': resource.construct_fip_id(data.subscription_id)
    },
    'backend_address_pool': {
        'id': resource.construct_bap_id(data.subscription_id)
    },
    'probe': {
        'id': resource.construct_probe_id(data.subscription_id)}}]


# InBoundNATRule1
inbound_nat_rule_configurations = [{
    'name': NETRULE_NAME_1,
    'protocol': 'tcp',
    'frontend_port': FRONTEND_PORT_1,
    'backend_port': BACKEND_PORT,
    'enable_floating_ip': False,
    'idle_timeout_in_minutes': 4,
    'frontend_ip_configuration': {
        'id': resource.construct_fip_id(data.subscription_id)}}]


# InBoundNATRule2
inbound_nat_rule_configurations.append({
    'name': NETRULE_NAME_2,
    'protocol': 'tcp',
    'frontend_port': FRONTEND_PORT_2,
    'backend_port': BACKEND_PORT,
    'enable_floating_ip': False,
    'idle_timeout_in_minutes': 4,
    'frontend_ip_configuration': {
        'id': resource.construct_fip_id(data.subscription_id)}})


# Create Load Balancer
# ********************

load_balancer_configurations = {
    'location': location,
    'frontend_ip_configurations': frontend_ip_configurations,
    'backend_address_pools': backend_ip_configurations,
    'probes': probe_configurations,
    'load_balancing_rules': load_balancer_rule_configurations,
    'inbound_nat_rules': inbound_nat_rule_configurations
}

print("Creating Load Balancer...")

# cumulus.create_update_load_balancers(
#     GROUP_NAME,
#     LOAD_BALANCER_NAME,
#     load_balancer_configurations
# )

resource_set.append(
    cumulus.get_load_balancers(
        GROUP_NAME,
        LOAD_BALANCER_NAME))


print("Summary of resources created in the load balancer workflow...")

resource.workflow_summary(resource_set)


# ------------------------- END OF LOAD_BALANCERS_WORKFLOW.PY -----------------