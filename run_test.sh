#!/bin/bash

set -eux

sudo yum install python2-docker-py

ansible-galaxy install -r tests/requirements.yml -p tests/roles/
ansible-playbook tests/test.yml -i tests/inventory --syntax-check
ansible-playbook tests/test.yml -i tests/inventory
