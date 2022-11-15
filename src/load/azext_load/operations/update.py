from ..aaz.latest.load._update import Update
from azure.cli.core.aaz import has_value
from msrestazure.tools import is_valid_resource_id
from azure.core.exceptions import ServiceRequestError


class LoadTestUpdate(Update):

    def _cli_arguments_loader(self):
        args = super()._cli_arguments_loader()

        # encryption_identity_type args are not exposed
        # encryption_identity_type is populated based on encryption_identity arg value
        args = [(name, arg) for (name, arg) in args if name not in ["encryption_identity_type"]]
        return args

    def pre_operations(self):
        args = self.ctx.args
        identity_type_str = str(args.identity_type)

        if has_value(args.encryption_identity):
            encryption_identity_id = str(args.encryption_identity)
            if encryption_identity_id.lower() == "systemassigned":
                args.encryption_identity_type = "SystemAssigned"
                args.encryption_identity = None
                if has_value(args.identity_type):
                    if identity_type_str.lower() == "none":
                        args.identity_type = "SystemAssigned"
                    elif identity_type_str.lower() == "userassigned":
                        args.identity_type = "SystemAssigned,UserAssigned"
            elif is_valid_resource_id(encryption_identity_id.lower()):
                args.encryption_identity_type = "UserAssigned"
                if has_value(args.identity_type):
                    if identity_type_str.lower() == "none":
                        args.identity_type = "UserAssigned"
                    elif identity_type_str.lower() == "systemassigned":
                        args.identity_type = "SystemAssigned,UserAssigned"
                    args.user_assigned[encryption_identity_id] = {}
            else:
                raise ServiceRequestError("Invalid encryption identity parameter: " + encryption_identity_id + ". Please enter a valid resource id.")
