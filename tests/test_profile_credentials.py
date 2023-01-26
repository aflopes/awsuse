from tempfile import mktemp

from awsuse.cli import read_source_profile_credentials, write_default_credentials


def test_should_read_credentials(
    test_profile_name: str, test_credentials_filepath: str, expected_credentials
):
    credentials = read_source_profile_credentials(
        test_profile_name, test_credentials_filepath
    )
    assert credentials == expected_credentials


def test_should_write_default_credentials():

    expected_credentials = [
        ("key1", "value1"),
        ("key2", "value2"),
        ("key3", "value3"),
    ]
    credentials_file = mktemp()
    write_default_credentials(expected_credentials, credentials_file)

    written_credentials = read_source_profile_credentials("default", credentials_file)

    assert written_credentials == expected_credentials
