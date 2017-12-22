import models.data.pgm_core_data as data
import models.data.parameters as parameters

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
    print('\nName: {}'
          '\n\tId: {}'
          '\n\tProvisioning State: {}'.format(resource.name,
                                              resource.id,
                                              resource.provisioning_state)
          )

    if hasattr(resource, 'type'):
        print('\t\tParameters:')
        print_parameters(resource, 0)


def print_parameters(resource, level=0):
    """
    Print resource parameters based on type.

    :param resource: azure resource object instance
    :param level: recursively track stuff
    :return: none
    """
    # param_list = []
    #
    # for key, value in resource.__dict__.items():
    #     if key == 'type':
    #         param_list = parameters.params_by_type[value]

    # for key, value in resource.__dict__.items():
    #     # if key in param_list:
    #     print('\t\t\t{}: {}'.format(key, value))

    for attr in dir(resource):
        if attr != '__doc__' and attr != '__module__':
            val = getattr(resource, attr)
            if isinstance(val, (int, str, list, dict)):
                print('{}: {}'.format(attr, val))
            else:
                print_parameters(val, level=level+1)