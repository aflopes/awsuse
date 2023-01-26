from tempfile import mktemp

from awsuse.cli import (
    read_config_section,
    read_source_profile_configs,
    write_default_configs,
)


def test_should_read_configs(
    test_profile_name: str, test_configs_filepath: str, expected_configs
):
    configs = read_source_profile_configs(test_profile_name, test_configs_filepath)
    assert configs == expected_configs


def test_should_write_default_configs():

    expected_configs = [
        ("key1", "value1"),
        ("key2", "value2"),
        ("key3", "value3"),
    ]
    config_file = mktemp()
    write_default_configs(expected_configs, config_file)

    written_configs = read_config_section(config_file, "default")

    assert written_configs == expected_configs
