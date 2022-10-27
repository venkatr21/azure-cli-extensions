# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "load create",
    confirmation="",
)
class Create(AAZCommand):
    """Create a load test resource.

    :example: Create load test resource
        az load create --name sample-load-test --location westus2
        az load create -n sample-load-test -l westus2
    """

    _aaz_info = {
        "version": "2022-12-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.loadtestservice/loadtests/{}", "2022-12-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of resource group. You can configure the default group using az configure --defaults group=<name>.",
            required=True,
        )

        # define Arg Group "Optional Parameters"

        _args_schema = cls._args_schema
        _args_schema.identity_type = AAZStrArg(
            options=["--identity-type"],
            arg_group="Optional Parameters",
            help="Type of managed service identity. Accepted values: \"None\", \"SystemAssigned\", \"UserAssigned\" \"SystemAssigned,UserAssigned\"",
            default="None",
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned,UserAssigned": "SystemAssigned,UserAssigned", "UserAssigned": "UserAssigned"},
        )
        _args_schema.user_assigned_identities = AAZDictArg(
            options=["--user-assigned-identities"],
            arg_group="Optional Parameters",
            help="The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.",
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Optional Parameters",
            help="Description of the resource.",
            fmt=AAZStrArgFormat(
                max_length=512,
            ),
        )
        _args_schema.encryption_identity = AAZStrArg(
            options=["--encryption-identity"],
            arg_group="Optional Parameters",
            help="The managed identity for Customer-managed key settings defining which identity should be used to auth to Key Vault.",
        )
        _args_schema.encryption_identity_type = AAZStrArg(
            options=["--encryption-identity-type"],
            arg_group="Optional Parameters",
            help="Managed identity type to use for accessing encryption key Url",
            enum={"SystemAssigned": "SystemAssigned", "UserAssigned": "UserAssigned"},
        )
        _args_schema.encryption_key = AAZStrArg(
            options=["--encryption-key"],
            arg_group="Optional Parameters",
            help="Encryption key URL, versioned. For example, https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78",
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Optional Parameters",
            help="Space-separated tags: key[=value] [key[=value] ...]. Use \"\" to clear existing tags.",
        )

        user_assigned_identities = cls._args_schema.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            blank={},
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Required Parameters"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Required Parameters",
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            arg_group="Required Parameters",
            help="Name of the new load test resource.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        try: 
            self.pre_operations()
            yield self.LoadTestsCreateOrUpdate(ctx=self.ctx)()
            self.post_operations()
        except (ValueError) as err:
            raise err

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class LoadTestsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LoadTestService/loadTests/{loadTestName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "loadTestName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-12-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("identity", AAZObjectType)
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".identity_type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("encryption", AAZObjectType)

            encryption = _builder.get(".properties.encryption")
            if encryption is not None:
                encryption.set_prop("identity", AAZObjectType)
                encryption.set_prop("keyUrl", AAZStrType, ".encryption_key")

            identity = _builder.get(".properties.encryption.identity")
            if identity is not None:
                identity.set_prop("resourceId", AAZStrType, ".encryption_identity")
                identity.set_prop("type", AAZStrType, ".encryption_identity_type")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.identity = AAZObjectType()
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200_201.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200_201.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200_201.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.data_plane_uri = AAZStrType(
                serialized_name="dataPlaneURI",
                flags={"read_only": True},
            )
            properties.description = AAZStrType()
            properties.encryption = AAZObjectType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )

            encryption = cls._schema_on_200_201.properties.encryption
            encryption.identity = AAZObjectType()
            encryption.key_url = AAZStrType(
                serialized_name="keyUrl",
            )

            identity = cls._schema_on_200_201.properties.encryption.identity
            identity.resource_id = AAZStrType(
                serialized_name="resourceId",
            )
            identity.type = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


__all__ = ["Create"]
