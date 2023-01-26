import pytest


@pytest.fixture()
def test_profile_name() -> str:
    return "test-profile"


@pytest.fixture()
def test_credentials_filepath() -> str:
    return "tests/files/test-credentials"


@pytest.fixture()
def test_configs_filepath() -> str:
    return "tests/files/test-configs"


@pytest.fixture()
def expected_configs():
    return [
        ("region", "us-east-2"),
        ("output", "json"),
    ]


@pytest.fixture()
def expected_credentials():
    return [
        ("aws_access_key_id", "ABCDEF1234567890"),
        ("aws_secret_access_key", "ABCDEF1234567890ABCDEF1234567890"),
    ]
