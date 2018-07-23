Name:       ansible-role-openstack-certification
Version:    0.0.VERS
Release:    1%{?dist}
Summary:    Ansible role for running the Red Hat Openstack Certification suite.
License:    ASL 2.0
URL:        https://github.com/redhat-cip/ansible-role-openstack-certification
Source0:    ansible-role-openstack-certification-%{version}.tar.gz

BuildArch:  noarch
Requires:   ansible

%description
An Ansible role to automate the openstack certification process

%prep
%setup -qc


%build

%install
mkdir -p %{buildroot}%{_datadir}/dci/roles/openstack-certification
chmod 755 %{buildroot}%{_datadir}/dci/roles/openstack-certification

cp -r meta %{buildroot}%{_datadir}/dci/roles/openstack-certification
cp -r tasks %{buildroot}%{_datadir}/dci/roles/openstack-certification
cp -r defaults %{buildroot}%{_datadir}/dci/roles/openstack-certification
cp -r templates %{buildroot}%{_datadir}/dci/roles/openstack-certification


%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/openstack-certification


%changelog
* Wed Apr 26 2017 Yanis Guenane <yguenane@redhat.com> - 0.0.1-1
- Initial release
