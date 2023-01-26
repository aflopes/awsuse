import os
import uuid

import pytest
from botocore.exceptions import ProfileNotFound

from awsuse.cli import validate_aws_profile


@pytest.fixture()
def load_test_aws_env_vars(test_configs_filepath, test_credentials_filepath):
    os.environ["AWS_CONFIG_FILE"] = test_configs_filepath
    os.environ["AWS_SHARED_CREDENTIALS_FILE"] = test_credentials_filepath


def test_should_validate_existing_profile(
    load_test_aws_env_vars, test_profile_name: str
):
    validate_aws_profile(test_profile_name)


def test_should_raise_exception_when_profile_does_not_exist(load_test_aws_env_vars):
    with pytest.raises(ProfileNotFound):
        validate_aws_profile(str(uuid.uuid4()))
