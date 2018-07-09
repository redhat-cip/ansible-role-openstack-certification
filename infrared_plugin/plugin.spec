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
                 openstack_certification_results_download:
                     type: Bool
                     help: |
                       Enable downloading the results file (/var/rhcert/results.xml)
                     default: No
                 openstack_certification_output_filename:
                     type: Value
                     help: |
                       Output filename for rhcert-ci print.
                     default: cert.txt
                 openstack_certification_test_type:
                     type: Value
                     help: |
                       Type of suite of tests to run. (values: test, tag, program).
                     default: test
                 openstack_certification_tests:
                     type: ListValue
                     help: |
                       List of tests to run.
                     default: self_check,supportable,director
                 openstack_certification_tags:
                     type: ListValue
                     help: |
                       List of tags to run.
                 openstack_certification_programs:
                     type: ListValue
                     help: |
                       List of programs to run.
                 openstack_certification_supported_apis_and_extensions:
                     type: ListValue
                     help: |
                       List of supported APIs and extensions.
                 openstack_certification_enable_rhsm_repo:
                     type: Bool
                     help: |
                       When No/False, RHSM registration will be omitted.
                     default: Yes
                 openstack_certification_repo_file:
                     type: Value
                     help: |
                       Path to a repo file, which will be copied to the host.
                 openstack_certification_tempest_conf_path:
                     type: Value
                     help: |
                       Path to a tempest configuration file.
