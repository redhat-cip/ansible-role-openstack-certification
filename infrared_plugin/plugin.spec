---
plugin_type: test
subparsers:
    ansible-role-openstack-certification:
        description: OpenStack certification tests
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: OpenStack Certification Tests
              options:
                 openstack_certification_output_format:
                     type: Value
                     help: |
                       Output format for rhcert-ci print. (values: text, junit, html).
                     default: text
                 openstack_certification_output_filename:
                     type: Value
                     help: |
                       Output filename for rhcert-ci print.
                     default: cert.txt
                 openstack_certification_test_type:
                     type: Value
                     help: |
                       Type of suite of tests to run. (values: test, tag, platform).
                     default: test
                 openstack_certification_tests:
                     type: Value
                     action: append
                     help: |
                       List of tests to run.
                     default: self_check,supportable,director
                 openstack_certification_tags:
                     type: Value
                     action: append
                     help: |
                       List of tags to run.
                 openstack_certification_platform:
                     type: Value
                     action: append
                     help: |
                       List of platform tests to run. (values: cloud, openstack, hardware).
                 openstack_certification_supported_apis_and_extensions:
                     type: Value
                     action: append
                     help: |
                       List of supported APIs and extensions.
                 openstack_certification_enable_rhsm_repo:
                     type: Bool
                     help: |
                       When No/False, RHSM registration will be omitted.
                     default: Yes
