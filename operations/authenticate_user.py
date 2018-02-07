import models.data.pgm_test_data as data

from msrestazure.azure_cloud import AZURE_US_GOV_CLOUD
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient

from azure.common.credentials import ServicePrincipalCredentials
from msrest.exceptions import AuthenticationError

# Create Service Principal
try:
    credentials = ServicePrincipalCredentials(
        client_id=data.CLIENT,
        secret=data.KEY,
        tenant=data.TENANT_ID,
        cloud_environment=AZURE_US_GOV_CLOUD)

except AuthenticationError as e:
    print(e)

network_client = NetworkManagementClient(
    credentials,
    data.subscription_id,
    base_url=AZURE_US_GOV_CLOUD.endpoints.resource_manager)

resource_client = ResourceManagementClient(
    credentials,
    data.subscription_id,
    base_url=AZURE_US_GOV_CLOUD.endpoints.resource_manager)


resource_client.providers.register('Microsoft.Network')