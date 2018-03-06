# ansible-role-openstack-certification

An Ansible role to automate the certification process

## Pre-requisites

In order to fully understand the content of this ansible role, one needs to be
familiar with the following [documentation](https://access.redhat.com/articles/2126521#Installthesoftwarepackages).

In the above article, the certification workflow and terminology is explained
in details.

## Role Variables

| Variable name                                         | Required | Default                         | Type    | Description                                                           |
|-------------------------------------------------------|----------|---------------------------------|---------|-----------------------------------------------------------------------|
| openstack_certification_output_format                 | False    | text                            | String  | Output format for rhcert-ci print. (values: text, junit, html)        |
| openstack_certification_output_filename               | False    | cert.txt                        | String  | Output filename for rhcert-ci print                                   |
| openstack_certification_test_type                     | False    | test                            | String  | Type of suite of tests to run. (values: test, tag, platform)          |
| openstack_certification_tests                         | False    | self_check,supportable,director | Array   | List of tests to run.                                                 |
| openstack_certification_tags                          | False    | N/A                             | Array   | List of tags to run.                                                  |
| openstack_certification_platform                      | False    | N/A                             | Array   | List of platform tests to run. (values: cloud, openstack, hardware)   |
| openstack_certification_supported_apis_and_extensions | False    | N/A                             | Array   | List of supported APIs and extensions.                                |

## Variables details

### Supported Tests

Available options for `openstack_certification_tests` are :

  * `self_check`
  * `supportable`
  * `director`
  * `tempest_config`
  * `sahara`
  * `cinder_consistency_groups`
  * `cinder_volumes`
  * `manila_share_extend`
  * `manila_share_managed`
  * `manila_share_shrink`
  * `manila_shares`
  * `manila_snapshot_managed`
  * `manila_snapshot_mountable`
  * `manila_snapshot_revert_to_snapshot`
  * `manila_snapshot_share_from_snapshot`
  * `manila_snapshots`
  * `neutron_address_scope`
  * `neutron_agents`
  * `neutron_attribute_extensions`
  * `neutron_availability_zones`
  * `neutron_dhcp_extra`
  * `neutron_flavor`
  * `neutron_gateway_extra`
  * `neutron_gman`
  * `neutron_ip_availability`
  * `neutron_ipv4`
  * `neutron_ipv6`
  * `neutron_l2_multi_provider`
  * `neutron_l3_extra_route`
  * `neutron_l3_flavors`
  * `neutron_l3_ha`
  * `neutron_lbaasv2`
  * `neutron_metering`
  * `neutron_mtu`
  * `neutron_qos`
  * `neutron_rbac`
  * `neutron_security_groups`
  * `neutron_service_types`
  * `neutron_subnet_allocation`
  * `neutron_subnet_default_pool`
  * `neutron_tags`
  * `neutron_trunk`

### Supported Tags

Available options for `openstack_certification_tags` are :

  * `osqa`
  * `portable`
  * `certification`
  * `realtime`
  * `manila`
  * `network`
  * `virtualization`
  * `wlan`
  * `cinder`
  * `usb`
  * `neutron`

### Supported Platforms

Available options for `openstack_certification_platform` are :

  * `cloud`
  * `hardware`
  * `openstack`

### Supported APIs and extensions:

Available options for `openstack_certification_supported_apis_and_extensions` are :

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

## Usage with InfraRed

Run the following steps to run the plugin:
1. Install infrared and add ansible-role-openstack-certification plugin by
providing the url to this repo:
    ```
    (infrared)$ ir plugin add https://github.com/redhat-cip/ansible-role-openstack-certification.git
    ```
2. You can verify that the plugin is imported by:
    ```
    (infrared)$ ir plugin list
    ```
3. From infrared directory symlink roles path:
    ```
    $ ln -s $(pwd)/plugins $(pwd)/plugins/ansible-role-openstack-certification/roles
    ```
4. Run the plugin:
    ```
    (infrared)$ ir ansible-role-openstack-certification
    ```

## License

Apache 2.0


## Author Information

Distributed-CI Team  <distributed-ci@redhat.com>
