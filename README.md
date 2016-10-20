# ansible-role-openstack-certification

An Ansible role to automate the certification process

## Pre-requisites

In order to fully understand the content of this ansible role, one needs to be
familiar with the following [documentation](https://access.redhat.com/articles/2126521#Installthesoftwarepackages).

In the above article, the certification workflow and terminology is explained
in details.

## Role Variables

| Variable name    | Default  | Type    | Description                                        |
|------------------|----------|---------|----------------------------------------------------|
| certification_id | None     | string  | The SandboxID for running certification test suite |
