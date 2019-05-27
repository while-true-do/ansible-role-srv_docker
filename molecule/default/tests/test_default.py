import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_package(host):
    pkg = host.package("docker")

    assert pkg.is_installed


def test_docker_service(host):
    vrt = host.ansible("setup")["ansible_facts"]["ansible_virtualization_type"]
    if vrt != 'docker':
        srv = host.service("docker")

        assert srv.is_running
        assert srv.is_enabled


def test_docker_group(host):
    grp = host.group("docker")

    assert grp.exists
