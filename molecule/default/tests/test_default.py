import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_paperless_web_is_running_and_enabled(host):
    web = host.service("paperless-web")
    assert web.is_running


def test_paperless_consumer_is_running_and_enabled(host):
    consumer = host.service("paperless-consumer")
    assert consumer.is_running


def test_folders_exists(host):
    assert host.file("/opt/paperless").is_directory

    consumption = host.file("/opt/paperless/consumption")
    assert consumption.is_directory
    assert consumption.user == "paperless"
    assert consumption.group == "paperless_consumption"
    assert consumption.mode == 0o770

    configuration = host.file("/etc/paperless.conf")
    assert configuration.is_file
    assert configuration.user == "root"
    assert configuration.group == "root"


def test_password_script_does_not_exist(host):
    assert not host.file("/opt/paperless/admin_password.sh").exists


def test_listenning_on_port_8000(host):
    assert host.socket("tcp://127.0.0.1:8000").is_listening
