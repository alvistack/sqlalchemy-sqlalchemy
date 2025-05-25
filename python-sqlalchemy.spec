# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-sqlalchemy
Epoch: 100
Version: 2.0.44
Release: 1%{?dist}
Summary: Database Abstraction Library
License: MIT
URL: https://github.com/sqlalchemy/sqlalchemy/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that
gives application developers the full power and flexibility of SQL.
SQLAlchemy provides a full suite of well known enterprise-level
persistence patterns, designed for efficient and high-performing
database access, adapted into a simple and Pythonic domain language.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-SQLAlchemy
Summary: Database Abstraction Library
Requires: python3
Requires: python3-greenlet >= 1
Requires: python3-importlib-metadata
Requires: python3-typing-extensions >= 4.6.0
Provides: python3-SQLAlchemy = %{epoch}:%{version}-%{release}
Provides: python3dist(SQLAlchemy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-SQLAlchemy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(SQLAlchemy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-SQLAlchemy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(SQLAlchemy) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-SQLAlchemy
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that
gives application developers the full power and flexibility of SQL.
SQLAlchemy provides a full suite of well known enterprise-level
persistence patterns, designed for efficient and high-performing
database access, adapted into a simple and Pythonic domain language.

%files -n python%{python3_version_nodots}-SQLAlchemy
%license LICENSE
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-SQLAlchemy
Summary: Database Abstraction Library
Requires: python3
Requires: python3-greenlet >= 1
Requires: python3-importlib-metadata
Requires: python3-typing-extensions >= 4.6.0
Provides: python3-SQLAlchemy = %{epoch}:%{version}-%{release}
Provides: python3dist(SQLAlchemy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-SQLAlchemy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(SQLAlchemy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-SQLAlchemy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(SQLAlchemy) = %{epoch}:%{version}-%{release}

%description -n python3-SQLAlchemy
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that
gives application developers the full power and flexibility of SQL.
SQLAlchemy provides a full suite of well known enterprise-level
persistence patterns, designed for efficient and high-performing
database access, adapted into a simple and Pythonic domain language.

%files -n python3-SQLAlchemy
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-sqlalchemy
Summary: Database Abstraction Library
Requires: python3
Requires: python3-greenlet >= 1
Requires: python3-importlib-metadata
Requires: python3-typing-extensions >= 4.6.0
Provides: python3-sqlalchemy = %{epoch}:%{version}-%{release}
Provides: python3dist(sqlalchemy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-sqlalchemy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(sqlalchemy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-sqlalchemy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(sqlalchemy) = %{epoch}:%{version}-%{release}

%description -n python3-sqlalchemy
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that
gives application developers the full power and flexibility of SQL.
SQLAlchemy provides a full suite of well known enterprise-level
persistence patterns, designed for efficient and high-performing
database access, adapted into a simple and Pythonic domain language.

%files -n python3-sqlalchemy
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
