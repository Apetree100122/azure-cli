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
    "sig list",
)
class List(AAZCommand):
    """List galleries under a resource group.
    """

    _aaz_info = {
        "version": "2021-10-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.compute/galleries", "2021-10-01"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/galleries", "2021-10-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        condition_1 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        if condition_0:
            self.GalleriesList(ctx=self.ctx)()
        if condition_1:
            self.GalleriesListByResourceGroup(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class GalleriesList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/galleries",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
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
                    "api-version", "2021-10-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.description = AAZStrType()
            properties.identifier = AAZObjectType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.sharing_profile = AAZObjectType(
                serialized_name="sharingProfile",
            )
            properties.sharing_status = AAZObjectType(
                serialized_name="sharingStatus",
            )
            properties.soft_delete_policy = AAZObjectType(
                serialized_name="softDeletePolicy",
            )

            identifier = cls._schema_on_200.value.Element.properties.identifier
            identifier.unique_name = AAZStrType(
                serialized_name="uniqueName",
                flags={"read_only": True},
            )

            sharing_profile = cls._schema_on_200.value.Element.properties.sharing_profile
            sharing_profile.community_gallery_info = AAZObjectType(
                serialized_name="communityGalleryInfo",
            )
            sharing_profile.groups = AAZListType(
                flags={"read_only": True},
            )
            sharing_profile.permissions = AAZStrType()

            community_gallery_info = cls._schema_on_200.value.Element.properties.sharing_profile.community_gallery_info
            community_gallery_info.community_gallery_enabled = AAZBoolType(
                serialized_name="communityGalleryEnabled",
                flags={"read_only": True},
            )
            community_gallery_info.eula = AAZStrType()
            community_gallery_info.public_name_prefix = AAZStrType(
                serialized_name="publicNamePrefix",
            )
            community_gallery_info.public_names = AAZListType(
                serialized_name="publicNames",
                flags={"read_only": True},
            )
            community_gallery_info.publisher_contact = AAZStrType(
                serialized_name="publisherContact",
            )
            community_gallery_info.publisher_uri = AAZStrType(
                serialized_name="publisherUri",
            )

            public_names = cls._schema_on_200.value.Element.properties.sharing_profile.community_gallery_info.public_names
            public_names.Element = AAZStrType()

            groups = cls._schema_on_200.value.Element.properties.sharing_profile.groups
            groups.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.sharing_profile.groups.Element
            _element.ids = AAZListType()
            _element.type = AAZStrType()

            ids = cls._schema_on_200.value.Element.properties.sharing_profile.groups.Element.ids
            ids.Element = AAZStrType()

            sharing_status = cls._schema_on_200.value.Element.properties.sharing_status
            sharing_status.aggregated_state = AAZStrType(
                serialized_name="aggregatedState",
                flags={"read_only": True},
            )
            sharing_status.summary = AAZListType()

            summary = cls._schema_on_200.value.Element.properties.sharing_status.summary
            summary.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.sharing_status.summary.Element
            _element.details = AAZStrType()
            _element.region = AAZStrType()
            _element.state = AAZStrType(
                flags={"read_only": True},
            )

            soft_delete_policy = cls._schema_on_200.value.Element.properties.soft_delete_policy
            soft_delete_policy.is_soft_delete_enabled = AAZBoolType(
                serialized_name="isSoftDeleteEnabled",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class GalleriesListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
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
                    "api-version", "2021-10-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.description = AAZStrType()
            properties.identifier = AAZObjectType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.sharing_profile = AAZObjectType(
                serialized_name="sharingProfile",
            )
            properties.sharing_status = AAZObjectType(
                serialized_name="sharingStatus",
            )
            properties.soft_delete_policy = AAZObjectType(
                serialized_name="softDeletePolicy",
            )

            identifier = cls._schema_on_200.value.Element.properties.identifier
            identifier.unique_name = AAZStrType(
                serialized_name="uniqueName",
                flags={"read_only": True},
            )

            sharing_profile = cls._schema_on_200.value.Element.properties.sharing_profile
            sharing_profile.community_gallery_info = AAZObjectType(
                serialized_name="communityGalleryInfo",
            )
            sharing_profile.groups = AAZListType(
                flags={"read_only": True},
            )
            sharing_profile.permissions = AAZStrType()

            community_gallery_info = cls._schema_on_200.value.Element.properties.sharing_profile.community_gallery_info
            community_gallery_info.community_gallery_enabled = AAZBoolType(
                serialized_name="communityGalleryEnabled",
                flags={"read_only": True},
            )
            community_gallery_info.eula = AAZStrType()
            community_gallery_info.public_name_prefix = AAZStrType(
                serialized_name="publicNamePrefix",
            )
            community_gallery_info.public_names = AAZListType(
                serialized_name="publicNames",
                flags={"read_only": True},
            )
            community_gallery_info.publisher_contact = AAZStrType(
                serialized_name="publisherContact",
            )
            community_gallery_info.publisher_uri = AAZStrType(
                serialized_name="publisherUri",
            )

            public_names = cls._schema_on_200.value.Element.properties.sharing_profile.community_gallery_info.public_names
            public_names.Element = AAZStrType()

            groups = cls._schema_on_200.value.Element.properties.sharing_profile.groups
            groups.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.sharing_profile.groups.Element
            _element.ids = AAZListType()
            _element.type = AAZStrType()

            ids = cls._schema_on_200.value.Element.properties.sharing_profile.groups.Element.ids
            ids.Element = AAZStrType()

            sharing_status = cls._schema_on_200.value.Element.properties.sharing_status
            sharing_status.aggregated_state = AAZStrType(
                serialized_name="aggregatedState",
                flags={"read_only": True},
            )
            sharing_status.summary = AAZListType()

            summary = cls._schema_on_200.value.Element.properties.sharing_status.summary
            summary.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.sharing_status.summary.Element
            _element.details = AAZStrType()
            _element.region = AAZStrType()
            _element.state = AAZStrType(
                flags={"read_only": True},
            )

            soft_delete_policy = cls._schema_on_200.value.Element.properties.soft_delete_policy
            soft_delete_policy.is_soft_delete_enabled = AAZBoolType(
                serialized_name="isSoftDeleteEnabled",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]