# ansible-role-openstack-certification

An Ansible role to automate the certification process

## Pre-requisites

In order to fully understand the content of this ansible role, one needs to be
familiar with the following [documentation](https://access.redhat.com/articles/2126521#Installthesoftwarepackages).

In the above article, the certification workflow and terminology is explained
in details.

## Role Variables

| Variable name                 | Required | Default       | Type    | Description                                                           |
|-------------------------------|----------|---------------|---------|-----------------------------------------------------------------------|
| certification_id              | True     | None          | string  | The SandboxID for running certification test suite                    |
| plugin_type                   | True     | None          | string  | Plugin type to certifcy. Available options listed below               |
| supported_apis_and_extensions | False    | All available | array   | List of supported apis and extensions. Available options listed below |


### Plugin Type

Available options for `plugin_type` are :

  * `blockstorage`
  * `networking`
  * `dataprocessing`
  * `objectstorage`
  * `image`
  * `database`
  * `identity`

## Supported APIs and extensions:

Available options for `supported_apis_and_extensions` are :


  * `blockstorage`:

    * `volumes`
    * `snapshots`
    * `volume_types`
    * `qos`
    * `backups`
    * `quota-set-extension`
    * `multiple-backends`
    * `availability`
    * `extensions`
    * `volume_transfers`


  * `networking`:

    * `vpnaas`
    * `service_type_management`
    * `security_groups`
    * `routers`
    * `ports`
    * `networks`
    * `subnets`
    * `metering`
    * `load_balancer`
    * `fwaas`
    * `floating_ips`
    * `extra_dhcp_options`
    * `allowed_address_pair`
    * `agent_management`
    * `dhcp_agent_scheduler`
    * `provider_networks`
    * `l3_agent_scheduler`
    * `lbaas_agent_scheduler`
    * `quotas`
    * `address_scopes`
    * `port_security`
    * `flavors_extensions`
    * `qos`
    * `subnetpools`
    * `load_balancers`
    * `lbaas_members`
    * `lbaas_pools`
    * `lbaas_listeners`
    * `lbaas_health_monitor`
    * `bgp`


  * `dataprocessing`:

    * `versions`
    * `limits`
    * `flavors`
    * `databases`
    * `database_users`
    * `database_instances`


  * `objectstorage`:

    * `accounts`
    * `containers`
    * `objects`


  * `image`:

    * `images`
    * `image_data`
    * `image_tags`
    * `image_members`
    * `image_schemas`


  * `database`:

    * `versions`
    * `limits`
    * `flavors`
    * `databases`
    * `database_users`
    * `database_instances`


  * `identity`:

    * `tokens`
    * `roles`
    * `services`
    * `tenants`
    * `users`
    * `credentials`
    * `domains`
    * `endpoints`
    * `groups`
    * `projects`
    * `policies`
    * `regions`
    * `trusts`



## Example

```
---
- hosts: undercloud
  remote_user: stack
  become: yes
  vars:
    certification_id: AVALIDCERTIFICATIONID
    plugin_type: blockstorage
    supported_apis_and_extensions:
      - volumes
      - backups
  roles:
    - openstack-certification
```
