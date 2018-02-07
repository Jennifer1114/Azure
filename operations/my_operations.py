import models.data.pgm_test_data as data
import models.data.parameters as parameters
import pyark


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
        print_resource(resource)


def print_resource(resource):
    """
    Print resource parameters.

    :param resource: azure resource object
    :return: none
    """
    print('\nName: {}'
          '\n\tId: {}'
          '\n\tProvisioning State: {}'.format(resource.name,
                                              resource.id,
                                              resource.provisioning_state)
          )

    if hasattr(resource, 'type'):
        print('\t\tParameters:')
        print_parameters(resource)


def print_parameters(resource):
    """
    Print resource parameters based on type.

    :param resource: azure resource object instance
    :param level: recursively track stuff
    :return: none
    """

    key = getattr(resource, '_attribute_map')
    value = getattr(resource, '__dict__')

    for (k,v), (k2,v2) in zip(key.items(), value.items()):
        print('\t\t\t{}: {}'.format(k, v2))
        #print_subparameters(v2)


def print_subparameters(parameter):

    # items = getattr(parameter)
    for item in parameter:
        value = getattr(item, '__dict__')
        for k, v in value.items():
            print('\t\t\t\t{}: {}'.format(k, v))
            #print_subparameters(v)



# Cyberark Password Account Functions
# ***********************************
# https://github.com/adfinis-sygroup/pyark