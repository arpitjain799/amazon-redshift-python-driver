import configparser
import os
from test import idp_arg

import pytest  # type: ignore

import redshift_connector

conf = configparser.ConfigParser()
root_path = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))
conf.read(root_path + "/config.ini")

PROVIDER = ["azure_idp"]


@pytest.mark.parametrize("idp_arg", PROVIDER, indirect=True)
def test_preferred_role_should_use(idp_arg):
    idp_arg["preferred_role"] = conf.get("azure-idp", "preferred_role")
    with redshift_connector.connect(**idp_arg):
        pass
