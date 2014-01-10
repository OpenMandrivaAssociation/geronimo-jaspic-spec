%{?_javapackages_macros:%_javapackages_macros}
%define api_version 1.0
%define pkg_name geronimo-jaspic_%{api_version}_spec
Name:          geronimo-jaspic-spec
Version:       1.1
Release:       9.0%{?dist}
Summary:       Java Authentication SPI for Containers
License:       ASL 2.0 and W3C
URL:           http://geronimo.apache.org/
Source0:       http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.tar.gz

BuildArch:     noarch

BuildRequires: java-devel
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: geronimo-osgi-support
BuildRequires: geronimo-parent-poms
BuildRequires: jpackage-utils

Provides:      javax.security.auth.message

%description
Java Authentication Service Provider Interface for Containers (JSR-196) api.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
%{summary}.


%prep
%setup -q -n %{pkg_name}-%{version}

for d in LICENSE NOTICE ; do
  iconv -f iso8859-1 -t utf-8 $d > $d.conv && mv -f $d.conv $d
  sed -i 's/\r//' $d
done

%pom_xpath_remove "pom:parent"
%pom_xpath_inject "pom:project" "
    <parent>
      <groupId>org.apache.geronimo.specs</groupId>
      <artifactId>specs</artifactId>
      <version>any</version>
    </parent>"

%build
%mvn_file  : %{name}
%mvn_alias : org.eclipse.jetty.orbit:javax.security.auth.message
%mvn_build

%install
%mvn_install

install -d -m 755 %{buildroot}%{_javadir}/javax.security.auth.message/
ln -sf ../%{name}.jar %{buildroot}%{_javadir}/javax.security.auth.message/

%files -f .mfiles
%doc LICENSE NOTICE
%{_javadir}/javax.security.auth.message/

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Aug 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-9
- Add javax.security.auth.message provides and directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-7
- Add depmap for org.eclipse.jetty.orbit
- Resolves: rhbz#917621

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 1.1-4
- Build with xmvn

* Thu Aug 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-3
- Fix license tag

* Mon Jul 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-2
- Add BR: geronimo-osgi-support

* Mon Jul 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-1
- Update to upstream version 1.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-1
- Initial package (based on Mageia version)
