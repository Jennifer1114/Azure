#!/usr/bin/python3
#
# cumulus.py
#
# by Jennifer Yarboro

from msrestazure import azure_exceptions
import operations.authenticate_user as clients

# Cloud definitions:
# AZURE_PUBLIC_CLOUD
# AZURE_CHINA_CLOUD
# AZURE_US_GOV_CLOUD
# AZURE_GERMAN_CLOUD

'''
Create create_update, delete, and get functions for each networknclass at
https://azure-sdk-for-python.readthedocs.io/en/latest/ref/azure.mgmt.network.v2017_03_01.operations.html
'''

network_client = clients.network_client
resource_client = clients.resource_client


# Resource Group Operations
def create_update_resource_group(
        resource_group_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a resource group.

    :param resource_group_name: (str) – The name of the resource group to
        create or update.
    :param parameters: (ResourceGroup) – Parameters supplied to the create or
        update a resource group.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: ResourceGroup or ClientRawResponse if raw=true
    """

    try:
        rg_info = resource_client.resource_groups.create_or_update(
            resource_group_name,
            parameters,
            custom_headers=None,
            raw=False
        )
        print(rg_info.properties.provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_resource_group(
        resource_group_name,
        custom_headers=None,
        raw=False
):
    """
    Gets a resource group.

    :param resource_group_name: (str) – The name of the resource group to
        create or update.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: ResourceGroup or ClientRawResponse if raw=true
    """

    try:
        rg_info = resource_client.resource_groups.get(
            resource_group_name,
            custom_headers=None,
            raw=False
        )
        return (rg_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_resource_group(
        resource_group_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes a resource group.

    :param resource_group_name: (str) – The name of the resource group to
        delete. The name is case insensitive.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """

    try:
        rg_info = resource_client.resource_groups.delete(
            resource_group_name,
            custom_headers=None,
            raw=False)
        rg_info.wait()

        print(rg_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Virtual Networks Operations:
def create_update_virtual_networks(
        resource_group_name,
        virtual_network_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a virtual network in the specified resource group.

    :param network_client: (NetworkManagementClient) - created using Service
        Principal
    :param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_name: (str) – The name of the virtual network.
    :param parameters: (VirtualNetwork) – Parameters supplied to the create or
        update virtual network operation.
    :param custom_headers: (dict) – headers that will be added to the request.
    :param raw: (bool) – returns the direct response alongside the deserialized
        response.
    :return: AzureOperationPoller instance that returns Subnet or
        ClientRawResponse if raw=true
    :raises: CloudError
    """

    try:
        vnet_info = network_client.virtual_networks.create_or_update(
            resource_group_name,
            virtual_network_name,
            parameters,
            custom_headers=None,
            raw=False)
        vnet_info.wait()
        print(vnet_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_virtual_networks(
        resource_group_name,
        virtual_network_name,
        expand=None,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified virtual network by resource group.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_name: (str) – The name of the virtual network.
    :param expand: (str) – Expands referenced resources.
    :param custom_headers: (dict) – headers that will be added to the request.
    :param raw: (bool) – returns the direct response alongside the deserialized
        response.
    :return: VirtualNetwork or ClientRawResponse if raw=true
    :raises: CloudError
    """
    try:
        vnet_info = network_client.virtual_networks.get(
            resource_group_name,
            virtual_network_name,
            expand=None,
            custom_headers=None,
            raw=False)

        return (vnet_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_virtual_networks(
        resource_group_name,
        virtual_network_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified virtual network.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_name: (str) – The name of the virtual network.
    :param custom_headers: (dict) – headers that will be added to the request.
    :param raw: (bool) – returns the direct response alongside the deserialized
        response.
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    :raises: CloudError
    """

    try:
        vnet_info = network_client.virtual_networks.delete(
            resource_group_name,
            virtual_network_name,
            custom_headers=None,
            raw=False)

        #do we need the wait?
        vnet_info.wait()
        print(vnet_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Subnets Operations:
def create_update_subnets(
        resource_group_name,
        virtual_network_name,
        subnet_name,
        subnet_parameters,
        custom_headers=None,
        raw=False
): 
    """
    Creates or updates a subnet in the specified virtual network.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_name: (str) – The name of the virtual network
    :param subnet_name: (str) – The name of the subnet.
    :param subnet_parameters: (Subnet) – Parameters supplied to the create
        or update subnet operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns Subnet or
        ClientRawResponse if raw=true
    :raises: CloudError
    """
    try:
        subnet_creation = network_client.subnets.create_or_update(
            resource_group_name,
            virtual_network_name,
            subnet_name,
            subnet_parameters,
            custom_headers=None,
            raw=False
        )
        print(subnet_creation.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_subnets(
        resource_group_name,
        virtual_network_name,
        subnet_name,
        expand=None,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified subnet by virtual network and resource group.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_name: (str) – The name of the virtual network
    :param subnet_name: (str) – The name of the subnet.
    :param expand: (str) – Expands referenced resources.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: Subnet or ClientRawResponse if raw=true
    :raises: CloudError
    """
    try:
        subnet_info = network_client.subnets.get(
            resource_group_name,
            virtual_network_name,
            subnet_name,
            expand=None,
            custom_headers=None,
            raw=False
        )
        return (subnet_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_subnets(
        resource_group_name,
        virtual_network_name,
        subnet_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified subnet.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_name: (str) – The name of the virtual network.
    :param subnet_name: (str) – The name of the subnet.
    :param custom_headers: (dict) – headers that will be added to the request.
    :param raw: (bool) – returns the direct response alongside the deserialized
        response.
    :return: AzureOperationPoller instance that returns Subnet or
        ClientRawResponse if raw=true.
    :raises: CloudError
    """

    try:
        subnet_info = network_client.subnets.delete(
            resource_group_name,
            virtual_network_name,
            subnet_name,
            custom_headers=None,
            raw=False
        )
        subnet_info.wait()
        print(subnet_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Route Tables Operations
def create_update_route_tables(
        resource_group_name,
        route_table_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Create or updates a route table in a specified resource group.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name:  (str) – The name of the resource group
    :param route_table_name: (str) – The name of the route table.
    :param parameters: (RouteTable) – Parameters supplied to the create or
        update route table operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns RouteTable or
        ClientRawResponse if raw=true
    """

    try:
        route_table_creation = network_client.route_tables.create_or_update(
            resource_group_name,
            route_table_name,
            parameters,
            custom_headers=None,
            raw=False
        )
        print(route_table_creation.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_route_tables(
        resource_group_name,
        route_table_name,
        expand=None,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified route table.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name:  (str) – The name of the resource group
    :param route_table_name: (str) – The name of the route table.
    :param expand: (str) – Expands referenced resources.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: RouteTable or ClientRawResponse if raw=true
    """

    try:
        route_table_info = network_client.route_tables.get(
            resource_group_name,
            route_table_name,
            expand=None,
            custom_headers=None,
            raw=False
        )
        return (route_table_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_route_tables(
        resource_group_name,
        route_table_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified route table.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name:  (str) – The name of the resource group
    :param route_table_name: (str) – The name of the route table.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """

    try:
        route_table_info = network_client.route_tables.delete(
            resource_group_name,
            route_table_name,
            custom_headers=None,
            raw=False
        )
        route_table_info.wait()
        print(route_table_info.status())

    except azure_exceptions.CloudError as e:
        print(e)

# Routes Operations
def create_update_routes(
        resource_group_name,
        route_table_name,
        route_name,
        route_parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a route in the specified route table.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name:  (str) – The name of the resource group
    :param route_table_name: (str) – The name of the route table.
    :param route_name: (str) – The name of the route.
    :param route_parameters: (Route) – Parameters supplied to the create or
        update route operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns Route or
        ClientRawResponse if raw=true
    """

    try:
        route_creation = network_client.routes.create_or_update(
            resource_group_name,
            route_table_name,
            route_name,
            route_parameters,
            custom_headers=None,
            raw=False
        )
        print(route_creation.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_routes(
        resource_group_name,
        route_table_name,
        route_name,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified route from a route table.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name:  (str) – The name of the resource group
    :param route_table_name: (str) – The name of the route table.
    :param route_name: (str) – The name of the route.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: Route or ClientRawResponse if raw=true
    """

    try:
        route_info = network_client.routes.get(
            resource_group_name,
            route_table_name,
            route_name,
            custom_headers=None,
            raw=False
        )
        return (route_info)

    except azure_exceptions.CloudError as e:
        print(e)

def delete_routes(
        resource_group_name,
        route_table_name,
        route_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified route from a route table.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name:  (str) – The name of the resource group
    :param route_table_name: (str) – The name of the route table.
    :param route_name: (str) – The name of the route.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """

    try:
        route_info = network_client.routes.delete(
            resource_group_name,
            route_table_name,
            route_name,
            custom_headers=None,
            raw=False
        )
        route_info.wait()
        print(route_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Virtual Network Peerings Operations
def create_update_virtual_network_peerings(
        resource_group_name,
        virtual_network_name,
        virtual_network_peering_name,
        virtual_network_peering_parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a peering in the specified virtual network.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_name: (str) – The name of the virtual network.
    :param virtual_network_peering_name: (str) – The name of the virtual
        network peering.
    :param virtual_network_peering_parameters:
    :param custom_headers: (dict) – headers that will be added to the request.
    :param raw: (bool) – returns the direct response alongside the deserialized
        response.
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        peering_creation = network_client.virtual_network_peerings.create_or_update(
            resource_group_name,
            virtual_network_name,
            virtual_network_peering_name,
            virtual_network_peering_parameters,
            custom_headers=None,
            raw=False
        )
        print(peering_creation.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_virtual_network_peerings(
        resource_group_name,
        virtual_network_name,
        virtual_network_peering_name,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified virtual network peering.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_name: (str) – The name of the virtual network.
    :param virtual_network_peering_name: (str) – The name of the virtual
        network peering.
    :param custom_headers: (dict) – headers that will be added to the request.
    :param raw: (bool) – returns the direct response alongside the deserialized
        response.
    :return: VirtualNetworkPeering or ClientRawResponse if raw=true
    """
    try:
        route_info = network_client.virtual_network_peerings.get(
            resource_group_name,
            virtual_network_name,
            virtual_network_peering_name,
            custom_headers=None,
            raw=False
        )
        return (route_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_virtual_network_peerings(
        resource_group_name,
        virtual_network_name,
        virtual_network_peering_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified virtual network peering.

    :param network_client: (NetworkManagementClient) - object created using
        Service Principal
    :param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_name: (str) – The name of the virtual network.
    :param virtual_network_peering_name: (str) – The name of the virtual
        network peering.
    :param custom_headers: (dict) – headers that will be added to the request.
    :param raw: (bool) – returns the direct response alongside the deserialized
        response.
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        route_info = network_client.virtual_network_peerings.delete(
            resource_group_name,
            virtual_network_name,
            virtual_network_peering_name,
            custom_headers=None,
            raw=False
        )
        route_info.wait()
        print(route_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Local Network Gateway Operations
def create_update_local_network_gateways(
        resource_group_name,
        local_network_gateway_name,
        parameters,
        custom_headers=None,
        raw=None
):
    """
    Creates or updates a local network gateway in the specified resource group.

    :param resource_group_name: (str) – The name of the resource group.
    :param local_network_gateway_name: (str) – The name of the local network
        gateway.
    :param parameters: (LocalNetworkGateway) – Parameters supplied to the
        create or update local network gateway operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns LocalNetworkGateway or
        ClientRawResponse if raw=true
    """
    try:
        lng_info = network_client.local_network_gateways.create_or_update(
            resource_group_name,
            local_network_gateway_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        lng_info.wait()
        print(lng_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_local_network_gateways(
        resource_group_name,
        local_network_gateway_name,
        custom_headers=None,
        raw=None
):
    """
    Gets the specified local network gateway in a resource group.

    :param resource_group_name: (str) – The name of the resource group.
    :param local_network_gateway_name: (str) – The name of the local network
        gateway.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: LocalNetworkGateway or ClientRawResponse if raw=true
    """
    try:
        lng_info = network_client.local_network_gateways.get(
            resource_group_name,
            local_network_gateway_name,
            custom_headers=None,
            raw=None
        )
        return (lng_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_local_network_gateways(
        resource_group_name,
        local_network_gateway_name,
        custom_headers=None,
        raw=None
):
    """
    Deletes the specified local network gateway.

    :param resource_group_name: (str) – The name of the resource group.
    :param local_network_gateway_name: (str) – The name of the local network
        gateway.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        lng_info = network_client.local_network_gateways.delete(
            resource_group_name,
            local_network_gateway_name,
            custom_headers=None,
            raw=None
        )
        lng_info.wait()
        print(lng_info.status())

    except azure_exceptions.CloudError as e:
        print(e)

# Public IP Addresses Operations
def create_update_public_ip_addresses(
        resource_group_name,
        public_ip_address_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a static or dynamic public IP address.

    :param resource_group_name: (str) – The name of the resource group.
    :param public_ip_address_name: (str) – The name of the public IP address.
    :param parameters: (PublicIPAddress) – Parameters supplied to the create
        or update public IP address operation.
    :param custom_headers:  (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns PublicIPAddress or
        ClientRawResponse if raw=true
    """
    try:
        pip_info = network_client.public_ip_addresses.create_or_update(
            resource_group_name,
            public_ip_address_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        pip_info.wait()
        print(pip_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_public_ip_addresses(
        resource_group_name,
        public_ip_address_name,
        expand=None,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified public IP address in a specified resource group.

    :param resource_group_name: (str) – The name of the resource group.
    :param public_ip_address_name: (str) – The name of the public IP address.
    :param expand: (str) – Expands referenced resources.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: PublicIPAddress or ClientRawResponse if raw=true
    """
    try:
        pip_info = network_client.public_ip_addresses.get(
            resource_group_name,
            public_ip_address_name,
            expand=None,
            custom_headers=None,
            raw=None
        )
        return (pip_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_public_ip_addresses(
        resource_group_name,
        public_ip_address_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified public IP address.

    :param resource_group_name: (str) – The name of the resource group.
    :param public_ip_address_name: (str) – The name of the public IP address.
    :param custom_headers:  (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns PublicIPAddress or
        ClientRawResponse if raw=true
    """
    try:
        pip_info = network_client.public_ip_addresses.delete(
            resource_group_name,
            public_ip_address_name,
            custom_headers=None,
            raw=None
        )
        pip_info.wait()
        print(pip_info.status())

    except azure_exceptions.CloudError as e:
        print(e)

# Virtual Network Gateway Operations
def create_update_virtual_network_gateways(
        resource_group_name,
        virtual_network_gateway_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a virtual network gateway in the specified resource
        group.

    :param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_gateway_name: (str) – The name of the virtual
        network gateway.
    :param parameters: (VirtualNetworkGateway) – Parameters supplied to
        create or update virtual network gateway operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns VirtualNetworkGateway or
        ClientRawResponse if raw=true
    """
    try:
        vng_info = network_client.virtual_network_gateways.create_or_update(
            resource_group_name,
            virtual_network_gateway_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        # vng_info.wait()
        print(vng_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_virtual_network_gateways(
        resource_group_name,
        virtual_network_gateway_name,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified virtual network gateway by resource group.

    param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_gateway_name: (str) – The name of the virtual
        network gateway.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: VirtualNetworkGateway or ClientRawResponse if raw=true
    """
    try:
        vng_info = network_client.virtual_network_gateways.get(
            resource_group_name,
            virtual_network_gateway_name,
            expand=None,
            custom_headers=None,
            raw=None
        )
        return (vng_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_virtual_network_gateways(
        resource_group_name,
        virtual_network_gateway_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified virtual network gateway.

    param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_gateway_name: (str) – The name of the virtual
        network gateway.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        vng_info = network_client.virtual_network_gateways.delete(
            resource_group_name,
            virtual_network_gateway_name,
            custom_headers=None,
            raw=None
        )
        vng_info.wait()
        print(vng_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Virtual Network Gateway Connections Operations
def create_update_virtual_network_gateway_connections(
        resource_group_name,
        virtual_network_gateway_connection_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a virtual network gateway connection in the specified
        resource group.

    :param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_gateway_connection_name: (str) – The name of the
        virtual network gateway connection.
    :param parameters: (VirtualNetworkGatewayConnection) – Parameters
        supplied to the create or update virtual network gateway connection
        operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns
        VirtualNetworkGatewayConnection or ClientRawResponse if raw=true
    """
    try:
        vngc_info = network_client.virtual_network_gateway_connections.create_or_update(
            resource_group_name,
            virtual_network_gateway_connection_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        vngc_info.wait()
        print(vngc_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_virtual_network_gateway_connections(
        resource_group_name,
        virtual_network_gateway_connection_name,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified virtual network gateway connection by resource group.

    :param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_gateway_connection_name: (str) – The name of the
        virtual network gateway connection.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: VirtualNetworkGatewayConnection or ClientRawResponse if raw=true
    """
    try:
        vngc_info = network_client.virtual_network_gateway_connections.get(
            resource_group_name,
            virtual_network_gateway_connection_name,
            expand=None,
            custom_headers=None,
            raw=None
        )
        return (vngc_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_virtual_network_gateway_connections(
        resource_group_name,
        virtual_network_gateway_connection_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified virtual network Gateway connection.

    :param resource_group_name: (str) – The name of the resource group.
    :param virtual_network_gateway_connection_name: (str) – The name of the
        virtual network gateway connection.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        vngc_info = network_client.virtual_network_gateway_connections.delete(
            resource_group_name,
            virtual_network_gateway_connection_name,
            custom_headers=None,
            raw=None
        )
        vngc_info.wait()
        print(vngc_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Network Interfaces Operations
def create_update_network_interfaces(
        resource_group_name,
        network_interface_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a network interface.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_interface_name: (str) – The name of the network interface.
    :param parameters: (NetworkInterface) – Parameters supplied to the create
        or update network interface operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns NetworkInterface or
        ClientRawResponse if raw=true
    """
    try:
        nic_info = network_client.network_interfaces.create_or_update(
            resource_group_name,
            network_interface_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        nic_info.wait()
        print(nic_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_network_interfaces(
        resource_group_name,
        network_interface_name,
        expand=None,
        custom_headers=None,
        raw=False
):
    """
    Gets information about the specified network interface.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_interface_name: (str) – The name of the network interface
    :param expand: (str) – Expands referenced resources.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: NetworkInterface or ClientRawResponse if raw=true
    """
    try:
        nic_info = network_client.network_interfaces.get(
            resource_group_name,
            network_interface_name,
            expand=None,
            custom_headers=None,
            raw=None
        )
        return (nic_info)

    except azure_exceptions.CloudError as e:
        print(e)

def delete_network_interfaces(
        resource_group_name,
        network_interface_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified network interface.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_interface_name: (str) – The name of the network interface.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        nic_info = network_client.network_interfaces.delete(
            resource_group_name,
            network_interface_name,
            custom_headers=None,
            raw=None
        )
        nic_info.wait()
        print(nic_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Network Security Groups Operations
def create_update_network_security_groups(
        resource_group_name,
        network_security_group_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a network interface.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_security_group_name: (str) – The name of the network
        security group.
    :param parameters: (NetworkSecurityGroup) – Parameters supplied to the
        create or update network security group operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns NetworkInterface or
        ClientRawResponse if raw=true
    """
    try:
        nsg_info = network_client.network_security_groups.create_or_update(
            resource_group_name,
            network_security_group_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        nsg_info.wait()
        print(nsg_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)

def get_network_security_groups(
        resource_group_name,
        network_security_group_name,
        expand=None,
        custom_headers=None,
        raw=False
):
    """
    Gets information about the specified network interface.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_security_group_name: (str) – The name of the network
        security group.
    :param expand: (str) – Expands referenced resources.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: NetworkInterface or ClientRawResponse if raw=true
    """
    try:
        nsg_info = network_client.network_security_groups.get(
            resource_group_name,
            network_security_group_name,
            expand=None,
            custom_headers=None,
            raw=None
        )
        return (nsg_info)

    except azure_exceptions.CloudError as e:
        print(e)

def delete_network_security_groups(
        resource_group_name,
        network_security_group_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified network interface.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_security_group_name: (str) – The name of the network
        security group.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        nsg_info = network_client.network_security_groups.delete(
            resource_group_name,
            network_security_group_name,
            custom_headers=None,
            raw=None
        )
        nsg_info.wait()
        print(nsg_info.status())

    except azure_exceptions.CloudError as e:
        print(e)

# Security Rules Operations
def create_update_security_rules(
        resource_group_name,
        network_security_group_name,
        security_rule_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a security rule in the specified network security group.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_security_group_name: (str) – The name of the network
        security group.
    :param security_rule_name: (str) – The name of the security rule.
    :param parameters: (SecurityRule) – Parameters supplied to the create or
        update network security rule operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns SecurityRule or
        ClientRawResponse if raw=true
    """
    try:
        nsgr_info = network_client.security_rules.create_or_update(
            resource_group_name,
            network_security_group_name,
            security_rule_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        nsgr_info.wait()
        print(nsgr_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_security_rules(
        resource_group_name,
        network_security_group_name,
        security_rule_name,
        custom_headers=None,
        raw=False
):
    """
    Get the specified network security rule.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_security_group_name: (str) – The name of the network
        security group.
    :param security_rule_name: (str) – The name of the security rule.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: SecurityRule or ClientRawResponse if raw=true
    """
    try:
        nsgr_info = network_client.security_rules.get(
            resource_group_name,
            network_security_group_name,
            security_rule_name,
            expand=None,
            custom_headers=None,
            raw=None
        )
        return (nsgr_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_security_rules(
        resource_group_name,
        network_security_group_name,
        security_rule_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified network security rule.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_security_group_name: (str) – The name of the network
        security group.
    :param security_rule_name: (str) – The name of the security rule.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        nsgr_info = network_client.security_rules.delete(
            resource_group_name,
            network_security_group_name,
            security_rule_name,
            custom_headers=None,
            raw=None
        )
        nsgr_info.wait()
        print(nsgr_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Express Route Circuits Operations
def create_update_express_route_circuits(
        resource_group_name,
        circuit_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates an express route circuit.

    :param resource_group_name: (str) – The name of the resource group.
    :param circuit_name: (str) – The name of the circuit.
    :param parameters:  (ExpressRouteCircuit) – Parameters supplied to the
        create or update express route circuit operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns ExpressRouteCircuit or
        ClientRawResponse if raw=true
    """
    try:
        erc_info = network_client.express_route_circuits.create_or_update(
            resource_group_name,
            circuit_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        erc_info.wait()
        print(erc_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_express_route_circuits(
        resource_group_name,
        circuit_name,
        custom_headers=None,
        raw=False
):
    """
    Gets information about the specified express route circuit.

    :param resource_group_name: (str) – The name of the resource group.
    :param circuit_name: (str) – The name of express route circuit.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: ExpressRouteCircuit or ClientRawResponse if raw=true
    """
    try:
        erc_info = network_client.express_route_circuits.get(
            resource_group_name,
            circuit_name,
            expand=None,
            custom_headers=None,
            raw=None
        )
        return (erc_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_express_route_circuits(
        resource_group_name,
        circuit_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified express route circuit.

    :param resource_group_name: (str) – The name of the resource group.
    :param circuit_name: (str) – The name of the express route circuit.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        erc_info = network_client.express_route_circuits.delete(
            resource_group_name,
            circuit_name,
            custom_headers=None,
            raw=None
        )
        erc_info.wait()
        print(erc_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Express Route Circuit Authorizations Operations
def create_update_express_route_circuit_authorizations(
        resource_group_name,
        circuit_name,
        authorization_name,
        authorization_parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates an authorization in the specified express route circuit.

    :param resource_group_name: (str) – The name of the resource group.
    :param circuit_name: (str) – The name of the express route circuit.
    :param authorization_name: (str) – The name of the authorization.
    :param authorization_parameters: (ExpressRouteCircuitAuthorization) –
        Parameters supplied to the create or update express route circuit
        authorization operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns
        ExpressRouteCircuitAuthorization or ClientRawResponse if raw=true
    """
    try:
        erca_info = network_client.express_route_circuit_authorizations.create_or_update(
            resource_group_name,
            circuit_name,
            authorization_name,
            authorization_parameters,
            custom_headers=None,
            raw=None
        )
        erca_info.wait()
        print(erca_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_express_route_circuit_authorizations(
        resource_group_name,
        circuit_name,
        authorization_name,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified authorization from the specified express route circuit.

    :param resource_group_name: (str) – The name of the resource group.
    :param circuit_name: (str) – The name of the express route circuit.
    :param authorization_name: (str) – The name of the authorization.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: ExpressRouteCircuitAuthorization or ClientRawResponse if raw=true
    """
    try:
        erca_info = network_client.express_route_circuit_authorizations.get(
            resource_group_name,
            circuit_name,
            authorization_name,
            expand=None,
            custom_headers=None,
            raw=None
        )
        return (erca_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_express_route_circuits_authorizations(
        resource_group_name,
        circuit_name,
        authorization_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified authorization from the specified express route circuit.

    :param resource_group_name: (str) – The name of the resource group.
    :param circuit_name: (str) – The name of the express route circuit.
    :param authorization_name: (str) – The name of the authorization.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        erca_info = network_client.express_route_circuit_authorizations.delete(
            resource_group_name,
            circuit_name,
            authorization_name,
            custom_headers=None,
            raw=None
        )
        erca_info.wait()
        print(erca_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


def create_update_express_route_circuit_peerings(
        resource_group_name,
        circuit_name,
        peering_name,
        peering_parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a peering in the specified express route circuits.

    :param resource_group_name: (str) – The name of the resource group.
    :param circuit_name: (str) – The name of the express route circuit.
    :param peering_name: (str) – The name of the peering.
    :param peering_parameters: (ExpressRouteCircuitPeering) – Parameters
        supplied to the create or update express route circuit peering
        operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns
        ExpressRouteCircuitPeering or ClientRawResponse if raw=true
    """
    try:
        ercp_info = network_client.express_route_circuit_peerings.create_or_update(
            resource_group_name,
            circuit_name,
            peering_name,
            peering_parameters,
            custom_headers=None,
            raw=None
        )
        ercp_info.wait()
        print(ercp_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_express_route_circuit_peerings(
        resource_group_name,
        circuit_name,
        peering_name,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified authorization from the specified express route circuit.

    :param resource_group_name: (str) – The name of the resource group.
    :param circuit_name: (str) – The name of the express route circuit.
    :param peering_name: (str) – The name of the peering.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: ExpressRouteCircuitPeering or ClientRawResponse if raw=true
    """
    try:
        ercp_info = network_client.express_route_circuit_peerings.get(
            resource_group_name,
            circuit_name,
            peering_name,
            expand=None,
            custom_headers=None,
            raw=None
        )
        return (ercp_info)

    except azure_exceptions.CloudError as e:
        print(e)

def delete_express_route_circuit_peerings(
        resource_group_name,
        circuit_name,
        peering_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified peering from the specified express route circuit.

    :param resource_group_name: (str) – The name of the resource group.
    :param circuit_name: (str) – The name of the express route circuit.
    :param peering_name: (str) – The name of the peering.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        ercp_info = network_client.express_route_circuit_peerings.delete(
            resource_group_name,
            circuit_name,
            peering_name,
            custom_headers=None,
            raw=None
        )
        ercp_info.wait()
        print(ercp_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Load Balancer Operations
def create_update_load_balancers(
        resource_group_name,
        load_balancer_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a load balancer.

    :param resource_group_name: (str) – The name of the resource group.
    :param load_balancer_name: (str) – The name of the load balancer.
    :param parameters: (LoadBalancer) – Parameters supplied to the create or
        update load balancer operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns LoadBalancer or
        ClientRawResponse if raw=true
    """
    try:
        lb_info = network_client.load_balancers.create_or_update(
            resource_group_name,
            load_balancer_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        lb_info.wait()
        print(lb_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_load_balancers(
        resource_group_name,
        load_balancer_name,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified load balancer.

    :param resource_group_name: (str) – The name of the resource group.
    :param load_balancer_name: (str) – The name of the load balancer.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: LoadBalancer or ClientRawResponse if raw=true
    """
    try:
        lb_info = network_client.load_balancers.get(
            resource_group_name,
            load_balancer_name,
            expand=None,
            custom_headers=None,
            raw=None
        )
        return (lb_info)

    except azure_exceptions.CloudError as e:
        print(e)

def delete_load_balancers(
        resource_group_name,
        load_balancer_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified load balancer.

    :param resource_group_name: (str) – The name of the resource group.
    :param load_balancer_name: (str) – The name of the load balancer.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        lb_info = network_client.load_balancers.delete(
            resource_group_name,
            load_balancer_name,
            custom_headers=None,
            raw=None
        )
        lb_info.wait()
        print(lb_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Application Gateways Operations
def create_update_application_gateways(
        resource_group_name,
        application_gateway_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates the specified application gateway.

    :param resource_group_name: (str) – The name of the resource group.
    :param application_gateway_name: (str) – The name of the application
        gateway.
    :param parameters: (ApplicationGateway) – Parameters supplied to the create
        or update application gateway operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns ApplicationGateway or
        ClientRawResponse if raw=true
    """
    try:
        ag_info = network_client.application_gateways.create_or_update(
            resource_group_name,
            application_gateway_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        ag_info.wait()
        print(ag_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_application_gateways(
        resource_group_name,
        application_gateway_name,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified application gateway.

    :param resource_group_name: (str) – The name of the resource group.
    :param application_gateway_name: (str) – The name of the application
        gateway.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: ApplicationGateway or ClientRawResponse if raw=true
    """
    try:
        ag_info = network_client.application_gateways.get(
            resource_group_name,
            application_gateway_name,
            custom_headers=None,
            raw=None
        )
        return (ag_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_application_gateways(
        resource_group_name,
        application_gateway_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified application gateway.

    :param resource_group_name: (str) – The name of the resource group.
    :param application_gateway_name: (str) – The name of the application
        gateway.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        ag_info = network_client.application_gateways.delete(
            resource_group_name,
            application_gateway_name,
            custom_headers=None,
            raw=None
        )
        ag_info.wait()
        print(ag_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Network Watchers Operations
def create_update_network_watchers(
        resource_group_name,
        network_watcher_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a network watcher in the specified resource group.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_watcher_name: (str) – The name of the network watcher.
    :param parameters: (NetworkWatcher) – Parameters that define the network
        watcher resource.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: NetworkWatcher or ClientRawResponse if raw=true
    """
    try:
        nw_info = network_client.network_watchers.create_or_update(
            resource_group_name,
            network_watcher_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        nw_info.wait()
        print(nw_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)

def get_network_watchers(
        resource_group_name,
        network_watcher_name,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified network watcher by resource group.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_watcher_name: (str) – The name of the network watcher.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: NetworkWatcher or ClientRawResponse if raw=true
    """
    try:
        nw_info = network_client.network_watchers.get(
            resource_group_name,
            network_watcher_name,
            custom_headers=None,
            raw=None
        )
        return (nw_info)

    except azure_exceptions.CloudError as e:
        print(e)

def delete_network_watchers(
        resource_group_name,
        network_watcher_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified network watcher resource.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_watcher_name: (str) – The name of the network watcher.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        nw_info = network_client.network_watchers.delete(
            resource_group_name,
            network_watcher_name,
            custom_headers=None,
            raw=None
        )
        nw_info.wait()
        print(nw_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


def create_update_packet_captures(
        resource_group_name,
        network_watcher_name,
        packet_capture_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Create and start a packet capture on the specified VM.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_watcher_name: (str) – The name of the network watcher.
    :param packet_capture_name: (str) – The name of the packet capture session.
    :param parameters: (PacketCapture) – Parameters that define the create
        packet capture operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns PacketCaptureResult or
        ClientRawResponse if raw=true
    """
    try:
        pc_info = network_client.packet_captures.create(
            resource_group_name,
            network_watcher_name,
            packet_capture_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        pc_info.wait()
        print(pc_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_packet_captures(
        resource_group_name,
        network_watcher_name,
        packet_capture_name,
        custom_headers=None,
        raw=None
):
    """
    Gets a packet capture session by name.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_watcher_name: (str) – The name of the network watcher.
    :param packet_capture_name: (str) – The name of the packet capture session.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: PacketCaptureResult or ClientRawResponse if raw=true
    """
    try:
        pc_info = network_client.packet_captures.get(
            resource_group_name,
            network_watcher_name,
            packet_capture_name,
            custom_headers=None,
            raw=None
        )
        return (pc_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_packet_captures(
        resource_group_name,
        network_watcher_name,
        packet_capture_name,
        custom_headers=None,
        raw=None
):
    """
    Deletes the specified packet capture session.

    :param resource_group_name: (str) – The name of the resource group.
    :param network_watcher_name: (str) – The name of the network watcher.
    :param packet_capture_name: (str) – The name of the packet capture session.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        pc_info = network_client.packet_captures.delete(
            resource_group_name,
            network_watcher_name,
            packet_capture_name,
            custom_headers=None,
            raw=None
        )
        pc_info.wait()
        print(pc_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Route Filters Operations
def create_update_route_filters(
        resource_group_name,
        route_filter_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a route filter in a specified resource group.

    :param resource_group_name: (str) – The name of the resource group.
    :param route_filter_name: (str) – The name of the route filter.
    :param parameters: (RouteFilter) – Parameters supplied to the create or
        update route filter operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns RouteFilter or
        ClientRawResponse if raw=true
    """
    try:
        rf_info = network_client.route_filters.create_or_update(
            resource_group_name,
            route_filter_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        rf_info.wait()
        print(rf_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)

def get_route_filters(
        resource_group_name,
        route_filter_name,
        expand=None,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified route filter.

    :param resource_group_name: (str) – The name of the resource group.
    :param route_filter_name: (str) – The name of the route filter.
    :param expand: (str) – Expands referenced express route bgp peering
        resources.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the
        deserialized response
    :return: RouteFilter or ClientRawResponse if raw=true
    """
    try:
        rf_info = network_client.route_filters.get(
            resource_group_name,
            route_filter_name,
            expand=None,
            custom_headers=None,
            raw=None
        )
        return (rf_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_route_filters(
        resource_group_name,
        route_filter_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified route filter.

    :param resource_group_name: (str) – The name of the resource group.
    :param route_filter_name: (str) – The name of the route filter.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the
        deserialized response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        rf_info = network_client.route_filters.delete(
            resource_group_name,
            route_filter_name,
            custom_headers=None,
            raw=None
        )
        rf_info.wait()
        print(rf_info.status())

    except azure_exceptions.CloudError as e:
        print(e)


# Route Filter Rules Operations
def create_update_route_filter_rules(
        resource_group_name,
        route_filter_name,
        rule_name,
        parameters,
        custom_headers=None,
        raw=False
):
    """
    Creates or updates a rule in the specified route filter.

    :param resource_group_name: (str) – The name of the resource group.
    :param route_filter_name: (str) – The name of the route filter.
    :param rule_name: (str) – The name of the route filter rule.
    :param parameters: (RouteFilterRule) – Parameters supplied to the create or
        update route filter rule operation.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns RouteFilterRule or
        ClientRawResponse if raw=true
    """
    try:
        rfr_info = network_client.route_filter_rules.create_or_update(
            resource_group_name,
            route_filter_name,
            rule_name,
            parameters,
            custom_headers=None,
            raw=None
        )
        rfr_info.wait()
        print(rfr_info.result().provisioning_state)

    except azure_exceptions.CloudError as e:
        print(e)


def get_route_filter_rules(
        resource_group_name,
        route_filter_name,
        rule_name,
        custom_headers=None,
        raw=False
):
    """
    Gets the specified rule from a route filter.

    :param resource_group_name: (str) – The name of the resource group.
    :param route_filter_name: (str) – The name of the route filter.
    :param rule_name: (str) – The name of the route filter rule.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: RouteFilterRule or ClientRawResponse if raw=true
    """
    try:
        rfr_info = network_client.route_filter_rules.get(
            resource_group_name,
            route_filter_name,
            rule_name,
            custom_headers=None,
            raw=False
        )
        return (rfr_info)

    except azure_exceptions.CloudError as e:
        print(e)


def delete_route_filter_rules(
        resource_group_name,
        route_filter_name,
        rule_name,
        custom_headers=None,
        raw=False
):
    """
    Deletes the specified rule from a route filter.

    :param resource_group_name: (str) – The name of the resource group.
    :param route_filter_name: (str) – The name of the route filter.
    :param rule_name: (str) – The name of the route filter rule.
    :param custom_headers: (dict) – headers that will be added to the request
    :param raw: (bool) – returns the direct response alongside the deserialized
        response
    :return: AzureOperationPoller instance that returns None or
        ClientRawResponse if raw=true
    """
    try:
        rfr_info = network_client.route_filter_rules.delete(
            resource_group_name,
            route_filter_name,
            rule_name,
            custom_headers=None,
            raw=None
        )
        rfr_info.wait()
        print(rfr_info.status())

    except azure_exceptions.CloudError as e:
        print(e)



# END OF CUMULUS.PY