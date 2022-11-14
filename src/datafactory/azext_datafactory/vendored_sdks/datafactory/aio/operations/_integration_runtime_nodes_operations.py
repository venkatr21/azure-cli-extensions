# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._integration_runtime_nodes_operations import (
    build_delete_request,
    build_get_ip_address_request,
    build_get_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class IntegrationRuntimeNodesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.datafactory.aio.DataFactoryManagementClient`'s
        :attr:`integration_runtime_nodes` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, factory_name: str, integration_runtime_name: str, node_name: str, **kwargs: Any
    ) -> _models.SelfHostedIntegrationRuntimeNode:
        """Gets a self-hosted integration runtime node.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param integration_runtime_name: The integration runtime name. Required.
        :type integration_runtime_name: str
        :param node_name: The integration runtime node name. Required.
        :type node_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SelfHostedIntegrationRuntimeNode or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.SelfHostedIntegrationRuntimeNode
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SelfHostedIntegrationRuntimeNode]

        request = build_get_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            integration_runtime_name=integration_runtime_name,
            node_name=node_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SelfHostedIntegrationRuntimeNode", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName}"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, factory_name: str, integration_runtime_name: str, node_name: str, **kwargs: Any
    ) -> None:
        """Deletes a self-hosted integration runtime node.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param integration_runtime_name: The integration runtime name. Required.
        :type integration_runtime_name: str
        :param node_name: The integration runtime node name. Required.
        :type node_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            integration_runtime_name=integration_runtime_name,
            node_name=node_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName}"}  # type: ignore

    @overload
    async def update(
        self,
        resource_group_name: str,
        factory_name: str,
        integration_runtime_name: str,
        node_name: str,
        update_integration_runtime_node_request: _models.UpdateIntegrationRuntimeNodeRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SelfHostedIntegrationRuntimeNode:
        """Updates a self-hosted integration runtime node.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param integration_runtime_name: The integration runtime name. Required.
        :type integration_runtime_name: str
        :param node_name: The integration runtime node name. Required.
        :type node_name: str
        :param update_integration_runtime_node_request: The parameters for updating an integration
         runtime node. Required.
        :type update_integration_runtime_node_request:
         ~azure.mgmt.datafactory.models.UpdateIntegrationRuntimeNodeRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SelfHostedIntegrationRuntimeNode or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.SelfHostedIntegrationRuntimeNode
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        factory_name: str,
        integration_runtime_name: str,
        node_name: str,
        update_integration_runtime_node_request: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SelfHostedIntegrationRuntimeNode:
        """Updates a self-hosted integration runtime node.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param integration_runtime_name: The integration runtime name. Required.
        :type integration_runtime_name: str
        :param node_name: The integration runtime node name. Required.
        :type node_name: str
        :param update_integration_runtime_node_request: The parameters for updating an integration
         runtime node. Required.
        :type update_integration_runtime_node_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SelfHostedIntegrationRuntimeNode or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.SelfHostedIntegrationRuntimeNode
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        factory_name: str,
        integration_runtime_name: str,
        node_name: str,
        update_integration_runtime_node_request: Union[_models.UpdateIntegrationRuntimeNodeRequest, IO],
        **kwargs: Any
    ) -> _models.SelfHostedIntegrationRuntimeNode:
        """Updates a self-hosted integration runtime node.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param integration_runtime_name: The integration runtime name. Required.
        :type integration_runtime_name: str
        :param node_name: The integration runtime node name. Required.
        :type node_name: str
        :param update_integration_runtime_node_request: The parameters for updating an integration
         runtime node. Is either a model type or a IO type. Required.
        :type update_integration_runtime_node_request:
         ~azure.mgmt.datafactory.models.UpdateIntegrationRuntimeNodeRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SelfHostedIntegrationRuntimeNode or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.SelfHostedIntegrationRuntimeNode
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SelfHostedIntegrationRuntimeNode]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(update_integration_runtime_node_request, (IO, bytes)):
            _content = update_integration_runtime_node_request
        else:
            _json = self._serialize.body(update_integration_runtime_node_request, "UpdateIntegrationRuntimeNodeRequest")

        request = build_update_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            integration_runtime_name=integration_runtime_name,
            node_name=node_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SelfHostedIntegrationRuntimeNode", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName}"}  # type: ignore

    @distributed_trace_async
    async def get_ip_address(
        self, resource_group_name: str, factory_name: str, integration_runtime_name: str, node_name: str, **kwargs: Any
    ) -> _models.IntegrationRuntimeNodeIpAddress:
        """Get the IP address of self-hosted integration runtime node.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param integration_runtime_name: The integration runtime name. Required.
        :type integration_runtime_name: str
        :param node_name: The integration runtime node name. Required.
        :type node_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IntegrationRuntimeNodeIpAddress or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.IntegrationRuntimeNodeIpAddress
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.IntegrationRuntimeNodeIpAddress]

        request = build_get_ip_address_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            integration_runtime_name=integration_runtime_name,
            node_name=node_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_ip_address.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("IntegrationRuntimeNodeIpAddress", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_ip_address.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName}/ipAddress"}  # type: ignore
