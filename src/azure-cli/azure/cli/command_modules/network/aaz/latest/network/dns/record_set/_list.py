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
    "network dns record-set list",
)
class List(AAZCommand):
    """List all record sets within a DNS zone.

    :example: List all "@" record sets within this zone.
        az network dns record-set list -g MyResourceGroup -z www.mysite.com --query "[?name=='@']"
    """

    _aaz_info = {
        "version": "2023-07-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/dnszones/{}/recordsets", "2023-07-01-preview"],
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
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.zone_name = AAZStrArg(
            options=["-z", "--zone-name"],
            help="Name of the DNS zone.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.RecordSetsListByDnsZone(ctx=self.ctx)()
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

    class RecordSetsListByDnsZone(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/recordsets",
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
                **self.serialize_url_param(
                    "zoneName", self.ctx.args.zone_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-07-01-preview",
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
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType()
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.aaaa_records = AAZListType(
                serialized_name="AAAARecords",
            )
            properties.a_records = AAZListType(
                serialized_name="ARecords",
            )
            properties.cname_record = AAZObjectType(
                serialized_name="CNAMERecord",
            )
            properties.ds_records = AAZListType(
                serialized_name="DSRecords",
            )
            properties.mx_records = AAZListType(
                serialized_name="MXRecords",
            )
            properties.naptr_records = AAZListType(
                serialized_name="NAPTRRecords",
            )
            properties.ns_records = AAZListType(
                serialized_name="NSRecords",
            )
            properties.ptr_records = AAZListType(
                serialized_name="PTRRecords",
            )
            properties.soa_record = AAZObjectType(
                serialized_name="SOARecord",
            )
            properties.srv_records = AAZListType(
                serialized_name="SRVRecords",
            )
            properties.tlsa_records = AAZListType(
                serialized_name="TLSARecords",
            )
            properties.ttl = AAZIntType(
                serialized_name="TTL",
            )
            properties.txt_records = AAZListType(
                serialized_name="TXTRecords",
            )
            properties.caa_records = AAZListType(
                serialized_name="caaRecords",
            )
            properties.fqdn = AAZStrType(
                flags={"read_only": True},
            )
            properties.metadata = AAZDictType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.target_resource = AAZObjectType(
                serialized_name="targetResource",
            )

            aaaa_records = cls._schema_on_200.value.Element.properties.aaaa_records
            aaaa_records.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.aaaa_records.Element
            _element.ipv6_address = AAZStrType(
                serialized_name="ipv6Address",
            )

            a_records = cls._schema_on_200.value.Element.properties.a_records
            a_records.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.a_records.Element
            _element.ipv4_address = AAZStrType(
                serialized_name="ipv4Address",
            )

            cname_record = cls._schema_on_200.value.Element.properties.cname_record
            cname_record.cname = AAZStrType()

            ds_records = cls._schema_on_200.value.Element.properties.ds_records
            ds_records.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.ds_records.Element
            _element.algorithm = AAZIntType()
            _element.digest = AAZObjectType()
            _element.key_tag = AAZIntType(
                serialized_name="keyTag",
            )

            digest = cls._schema_on_200.value.Element.properties.ds_records.Element.digest
            digest.algorithm_type = AAZIntType(
                serialized_name="algorithmType",
            )
            digest.value = AAZStrType()

            mx_records = cls._schema_on_200.value.Element.properties.mx_records
            mx_records.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.mx_records.Element
            _element.exchange = AAZStrType()
            _element.preference = AAZIntType()

            naptr_records = cls._schema_on_200.value.Element.properties.naptr_records
            naptr_records.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.naptr_records.Element
            _element.flags = AAZStrType()
            _element.order = AAZIntType()
            _element.preference = AAZIntType()
            _element.regexp = AAZStrType()
            _element.replacement = AAZStrType()
            _element.services = AAZStrType()

            ns_records = cls._schema_on_200.value.Element.properties.ns_records
            ns_records.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.ns_records.Element
            _element.nsdname = AAZStrType()

            ptr_records = cls._schema_on_200.value.Element.properties.ptr_records
            ptr_records.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.ptr_records.Element
            _element.ptrdname = AAZStrType()

            soa_record = cls._schema_on_200.value.Element.properties.soa_record
            soa_record.email = AAZStrType()
            soa_record.expire_time = AAZIntType(
                serialized_name="expireTime",
            )
            soa_record.host = AAZStrType()
            soa_record.minimum_ttl = AAZIntType(
                serialized_name="minimumTTL",
            )
            soa_record.refresh_time = AAZIntType(
                serialized_name="refreshTime",
            )
            soa_record.retry_time = AAZIntType(
                serialized_name="retryTime",
            )
            soa_record.serial_number = AAZIntType(
                serialized_name="serialNumber",
            )

            srv_records = cls._schema_on_200.value.Element.properties.srv_records
            srv_records.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.srv_records.Element
            _element.port = AAZIntType()
            _element.priority = AAZIntType()
            _element.target = AAZStrType()
            _element.weight = AAZIntType()

            tlsa_records = cls._schema_on_200.value.Element.properties.tlsa_records
            tlsa_records.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.tlsa_records.Element
            _element.cert_association_data = AAZStrType(
                serialized_name="certAssociationData",
            )
            _element.matching_type = AAZIntType(
                serialized_name="matchingType",
            )
            _element.selector = AAZIntType()
            _element.usage = AAZIntType()

            txt_records = cls._schema_on_200.value.Element.properties.txt_records
            txt_records.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.txt_records.Element
            _element.value = AAZListType()

            value = cls._schema_on_200.value.Element.properties.txt_records.Element.value
            value.Element = AAZStrType()

            caa_records = cls._schema_on_200.value.Element.properties.caa_records
            caa_records.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.caa_records.Element
            _element.flags = AAZIntType()
            _element.tag = AAZStrType()
            _element.value = AAZStrType()

            metadata = cls._schema_on_200.value.Element.properties.metadata
            metadata.Element = AAZStrType()

            target_resource = cls._schema_on_200.value.Element.properties.target_resource
            target_resource.id = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
