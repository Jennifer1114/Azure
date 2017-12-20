import models.data.pgm_core_data as data

# Type Names
VIRTUAL_NETWORKS = 'Microsoft.Network/virtualNetworks'
VIRTUAL_NETWORK_PEERINGS = 'Microsoft.Network/virtualNetworkPeerings'
VIRTUAL_NETWORK_GATEWAYS = 'Microsoft.Network/virtualNetworkGateways'
VIRTUAL_NETWORK_GATEWAY_CONNECTIONS = 'Microsoft.Network/virtualNetworkGatewayConnections'

SUBNETS = 'Microsoft.Network/subnets'
ROUTES = 'Microsoft.Network/routes'
ROUTE_TABLES = 'Microsoft.Network/routeTables'
ROUTE_FILTERS = 'Microsoft.Network/routeFilters'
ROUTE_FILTER_RULES = 'Microsoft.Network/routeFilterRules'

PUBLIC_IP_ADDRESSES = 'Microsoft.Network/publicIPAddresses'
NETWORK_SECURITY_GROUPS = 'Microsoft.Network/networkSecurityGroups'
NETWORK_INTERFACES = 'Microsoft.Network/networkInterfaces'
NETWORK_INTERFACE_LOAD_BALANCERS = 'Microsoft.Network/networkInterfaceLoadBalancers'
NETWORK_INTERFACE_IP_CONFIGURATIONS = 'Microsoft.Network/networkInterfaceIpConfigurations'

LOCAL_NETWORK_GATEWAYS = 'Microsoft.Network/localNetworkGateways'
LOAD_BALANCERS = 'Microsoft.Network/loadBalancers'
LOAD_BALANCER_PROBES = 'Microsoft.Network/loadBalancerProbes'
LOAD_BALANCER_NETWORK_INTERFACES = 'Microsoft.Network/loadBalancerNetworkInterfaces'
LOAD_BALANCER_LOAD_BALANCING_RULES = 'Microsoft.Network/loadBalancerLoadBalancingRules'
LOAD_BALANCER_FRONTEND_IP_CONFIGURATIONS = 'Microsoft.Network/loadBalancerFrontendIpConfigurations'
LOAD_BALANCER_BACKEND_ADDRESS_POOLS = 'Microsoft.Network/loadBalancerBackendAddressPools'
INBOUND_NAT_RULES = 'Microsoft.Network/inboundNatRules'

EXPRESS_ROUTE_SERVICE_PROVIDERS = 'Microsoft.Network/expressRouteServiceProviders'
EXPRESS_ROUTE_CIRCUITS = 'Microsoft.Network/expressRouteCircuits'
EXPRESS_ROUTE_CIRCUIT_PEERINGS = 'Microsoft.Network/expressRouteCircuitPeerings'
EXPRESS_ROUTE_CIRCUIT_AUTHORIZATIONS = 'Microsoft.Network/expressRouteCircuitAuthorizations'

# Resource ID Construction
# ************************

def construct_fip_id(subscription_id):
    """
    Build the future FrontEndId based on components name.
    """
    return ('/subscriptions/{}'
            '/resourceGroups/{}'
            '/providers/Microsoft.Network'
            '/loadBalancers/{}'
            '/frontendIPConfigurations/{}').format(
                subscription_id, data.GROUP_NAME, data.LOAD_BALANCER_NAME, data.FE_IP_NAME
            )

def construct_bap_id(subscription_id):
    """
    Build the future BackEndId based on components name.
    """
    return ('/subscriptions/{}'
            '/resourceGroups/{}'
            '/providers/Microsoft.Network'
            '/loadBalancers/{}'
            '/backendAddressPools/{}').format(
                subscription_id, data.GROUP_NAME, data.LOAD_BALANCER_NAME, data.ADDRESS_POOL_NAME
            )

def construct_probe_id(subscription_id):
    """
    Build the future ProbeId based on components name.
    """
    return ('/subscriptions/{}'
            '/resourceGroups/{}'
            '/providers/Microsoft.Network'
            '/loadBalancers/{}'
            '/probes/{}').format(
                subscription_id, data.GROUP_NAME, data.LOAD_BALANCER_NAME, data.PROBE_NAME
            )


# Resource Display Functions
# **************************

def workflow_summary(resource_set):
    """
    Constructs a summary of all resources created in a workflow.

    :param display_type: displays a standard or verbose set of parameters
    :param resource_set: dictionary item of all resources and their custom
        parameters
    :return: summary of workflow resources
    """

    for resource in resource_set:
        print_item(resource)


def print_item(resource):
    """
    Print resource parameters.

    :param resource: azure resource object
    :return: none
    """
    print('\nName: {}\n'.format(resource.name),
          '\tId: {}\n'.format(resource.id),
          '\tLocation: {}\n'.format(resource.location),
          '\tProperties:')

    if hasattr(resource, 'properties'):
        print_properties(resource.properties)

    if hasattr(resource, 'type'):
        print_parameters(resource, resource.type)


def print_properties(properties):
    """
    Print resource properties.

    :param properties: subset of azure resource object instance parameters
    :return: none
    """
    if properties and properties.provisioning_state:
        print('\t\tProvisioning State: '
              '{}\n'.format(properties.provisioning_state))


def print_parameters(resource, type):
    """
    Print resource parameters based on type.

    :param resource: azure resource object instance
    :param type: resource type
    :return: none
    """
    print('\t\tProvisioning State: ',
          '{}'.format(resource.__dict__['provisioning_state']))

    if type == LOAD_BALANCERS:
        print('\t\tFrontend IP Configurations: ')
        for config in resource.__dict__['frontend_ip_configurations']:
            print('\t\t\t{}\n'.format(config.private_ip_allocation_method))

