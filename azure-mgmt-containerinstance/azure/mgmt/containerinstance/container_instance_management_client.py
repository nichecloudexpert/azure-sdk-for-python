# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.container_groups_operations import ContainerGroupsOperations
from .operations.operations import Operations
from .operations.container_group_usage_operations import ContainerGroupUsageOperations
from .operations.container_operations import ContainerOperations
from .operations.service_association_link_operations import ServiceAssociationLinkOperations
from . import models


class ContainerInstanceManagementClientConfiguration(AzureConfiguration):
    """Configuration for ContainerInstanceManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ContainerInstanceManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-containerinstance/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class ContainerInstanceManagementClient(SDKClient):
    """ContainerInstanceManagementClient

    :ivar config: Configuration for client.
    :vartype config: ContainerInstanceManagementClientConfiguration

    :ivar container_groups: ContainerGroups operations
    :vartype container_groups: azure.mgmt.containerinstance.operations.ContainerGroupsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.containerinstance.operations.Operations
    :ivar container_group_usage: ContainerGroupUsage operations
    :vartype container_group_usage: azure.mgmt.containerinstance.operations.ContainerGroupUsageOperations
    :ivar container: Container operations
    :vartype container: azure.mgmt.containerinstance.operations.ContainerOperations
    :ivar service_association_link: ServiceAssociationLink operations
    :vartype service_association_link: azure.mgmt.containerinstance.operations.ServiceAssociationLinkOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ContainerInstanceManagementClientConfiguration(credentials, subscription_id, base_url)
        super(ContainerInstanceManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-01-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.container_groups = ContainerGroupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.container_group_usage = ContainerGroupUsageOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.container = ContainerOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.service_association_link = ServiceAssociationLinkOperations(
            self._client, self.config, self._serialize, self._deserialize)
