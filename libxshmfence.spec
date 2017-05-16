#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libxshmfence
Version  : 1.2
Release  : 8
URL      : http://xorg.freedesktop.org/releases/individual/lib/libxshmfence-1.2.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libxshmfence-1.2.tar.bz2
Summary  : The X Shared Memory Fence Library
Group    : Development/Tools
License  : MIT
Requires: libxshmfence-lib
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(32xproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)

%description
libxshmfence - Shared memory 'SyncFence' synchronization primitive
This library offers a CPU-based synchronization primitive compatible
with the X SyncFence objects that can be shared between processes
using file descriptor passing.

%package dev
Summary: dev components for the libxshmfence package.
Group: Development
Requires: libxshmfence-lib
Provides: libxshmfence-devel

%description dev
dev components for the libxshmfence package.


%package dev32
Summary: dev32 components for the libxshmfence package.
Group: Default
Requires: libxshmfence-lib32

%description dev32
dev32 components for the libxshmfence package.


%package lib
Summary: lib components for the libxshmfence package.
Group: Libraries

%description lib
lib components for the libxshmfence package.


%package lib32
Summary: lib32 components for the libxshmfence package.
Group: Default

%description lib32
lib32 components for the libxshmfence package.


%prep
%setup -q -n libxshmfence-1.2
pushd ..
cp -a libxshmfence-1.2 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/xshmfence.h
/usr/lib64/libxshmfence.so
/usr/lib64/pkgconfig/xshmfence.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libxshmfence.so
/usr/lib32/pkgconfig/32xshmfence.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxshmfence.so.1
/usr/lib64/libxshmfence.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libxshmfence.so.1
/usr/lib32/libxshmfence.so.1.0.0
