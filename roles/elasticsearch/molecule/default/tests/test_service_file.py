import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_file_exists(host):
    service_file = host.file('/etc/systemd/system/elasticsearch.service')

    assert service_file.exists
    assert service_file.user == 'root'
    assert service_file.group == 'elasticsearch'


def test_elasticsearch_running_and_enabled(host):
    elasticsearch = host.service('elasticsearch')
    assert elasticsearch.is_running
    assert elasticsearch.is_enabled
