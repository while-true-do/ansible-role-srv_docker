<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-srv_docker.svg)](https://github.com/while-true-do/ansible-role-srv_docker/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-srv_docker.svg)](https://github.com/while-true-do/ansible-role-srv_docker/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-srv_docker.svg)](https://github.com/while-true-do/ansible-role-srv_docker/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-srv_docker.svg)](https://github.com/while-true-do/ansible-role-srv_docker/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-srv_docker.svg)](https://travis-ci.com/while-true-do/ansible-role-srv_docker)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_docker%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_docker)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_docker%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_docker)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_docker%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_docker)

# Ansible Role: srv_docker

An Ansible Role to install and configure [Docker](https://docs.docker.com/) on
Linux.

## Motivation

[Docker](https://docs.docker.com/) and Docker Containers are widely used.
Setting up a docker service is very common and useful.

## Description

This role is setting up docker and configuring it from official repositories.

-   install docker or docker-ce
-   control the docker-ce repository
-   optional: install docker-compose
-   start docker service
-   create docker group
-   add users to group

## Requirements

Used Modules:

-   [Ansible package_facts Module](https://docs.ansible.com/ansible/latest/modules/package_facts_module.html)
-   [Ansible package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible service Module](https://docs.ansible.com/ansible/latest/modules/service_module.html)
-   [Ansible systemd Module](https://docs.ansible.com/ansible/latest/modules/systemd_module.html)
-   [Ansible group Module](https://docs.ansible.com/ansible/latest/modules/group_module.html)
-   [Ansible user Module](https://docs.ansible.com/ansible/latest/modules/user_module.html)

## Installation

Install from [Github](https://github.com/while-true-do/ansible-role-srv_docker)
```
git clone https://github.com/while-true-do/ansible-role-srv_docker.git while_true_do.srv_docker
```

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_docker)
```
ansible-galaxy install while_true_do.srv_docker
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.srv_docker

## Package Management
wtd_srv_docker_package: "docker"
# State can be present|latest|absent
wtd_srv_docker_package_state: "present"

# Define the source of docker:
# Source can be dist|ce
# dist = repository of your distribution
# ce = official community docker repository
wtd_srv_docker_package_source: "dist"
# Only used for source = ce|ee
# *_enabled can be 0|1
wtd_srv_docker_package_edge_enabled: 0
wtd_srv_docker_package_test_enabled: 0

# Docker Compose Packages
# State can be present|latest|absent|unmanaged
wtd_srv_docker_compose_package_state: "unmanaged"
# Source can be binary
wtd_srv_docker_compose_package_source: "binary"
# Only used, when source = binary
wtd_srv_docker_compose_package_version: "1.24.1"
wtd_srv_docker_compose_package_path: "/usr/local/bin/docker-compose"

## Service Management
wtd_srv_docker_service: "docker"
# State can be started|stopped
wtd_srv_docker_service_state: "started"
wtd_srv_docker_service_enabled: true

## User and Group Management
wtd_srv_docker_group: "docker"
# State can be present|absent
wtd_srv_docker_group_state: "present"
# A list of user names.
wtd_srv_docker_group_users: []
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.srv_docker
```

#### Advanced

Add users to the docker group.

```
- hosts: all
  roles:
    - role: while_true_do.srv_docker
      wtd_srv_docker_group_users:
        - user1
        - user2
      wtd_srv_docker_service_enabled: "no"
```

Use the docker-ce version and install docker-compose.

```
- hosts: all
  roles:
    - role: while_true_do.srv_docker
      wtd_srv_docker_compose_package_state: "present"
      wtd_srv_docker_package_source: "ce"
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_docker/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_docker/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
