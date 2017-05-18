# ansible-role-openstack-certification

An Ansible role to automate the certification process

## Pre-requisites

In order to fully understand the content of this ansible role, one needs to be
familiar with the following [documentation](https://access.redhat.com/articles/2126521#Installthesoftwarepackages).

In the above article, the certification workflow and terminology is explained
in details.

## Role Variables

| Variable name                                         | Required | Default                            | Type    | Description                                                           |
|-------------------------------------------------------|----------|------------------------------------|---------|-----------------------------------------------------------------------|
| openstack_certification_supported_apis_and_extensions | False    | All available                      | array   | List of supported apis and extensions. Available options listed below |
| openstack_certification_tests                         | False    | self_check, supportable, directory | array   | List of suite of tests to run.                                        |


## Supported APIs and extensions:

Available options for `supported_apis_and_extensions` are :

  * `qos`
  * `clone`
  * `snapshots`
  * `volume_types`
  * `quota-set-extension`
  * `backups`
  * `multiple-backends`
  * `availability`
  * `image_metadata`
  * `consistencygroups`
  * `volume_transfers`
  * `extensions`
  * `volumes`
  * `user_messages`
  * `load_balancer`
  * `subnets`
  * `agent_management`
  * `qos`
  * `provider_networks`
  * `lbaas_listeners`
  * `service_type_management`
  * `lbaas_agent_scheduler`
  * `fwaas`
  * `metering`
  * `extra_dhcp_options`
  * `quotas`
  * `dhcp_agent_scheduler`
  * `port_security`
  * `trunk`
  * `lbaas_pools`
  * `load_balancers`
  * `networks`
  * `security_groups`
  * `revisions`
  * `subnetpools`
  * `flavors_extensions`
  * `l3_agent_scheduler`
  * `lbaas_members`
  * `versions`
  * `floating_ips`
  * `address_scopes`
  * `bgp`
  * `allowed_address_pair`
  * `routers`
  * `extensions`
  * `vpnaas`
  * `ports`
  * `lbaas_health_monitor`
  * `cluster-templates`
  * `jobs`
  * `job-binaries`
  * `job-binary-internals`
  * `node-group-templates`
  * `data-sources`
  * `plugins`

## Example

```
---
- hosts: undercloud
  remote_user: stack
  become: yes
  vars:
    openstack_certification_supported_apis_and_extensions:
      - volumes
      - backups
  roles:
    - openstack-certification
```
