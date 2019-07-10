import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_file_exists(host):
    service_file = host.file('/etc/systemd/system/logstash.service')

    assert service_file.exists
    assert service_file.user == 'root'
    assert service_file.group == 'logstash'


def test_logstash_running_and_enabled(host):
    logstash = host.service('logstash')
    assert logstash.is_running
    assert logstash.is_enabled
