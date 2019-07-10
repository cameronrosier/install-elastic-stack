import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_file_exists(host):
    service_file = host.file('/etc/systemd/system/kibana.service')

    assert service_file.exists
    assert service_file.user == 'root'
    assert service_file.group == 'kibana'


def test_kibana_running_and_enabled(host):
    kibana = host.service('kibana')
    assert kibana.is_running
    assert kibana.is_enabled
