Name: lxcfs
Version: 2.0.6
Release: 1
Source0: https://linuxcontainers.org/downloads/lxcfs/lxcfs-%{version}.tar.gz
Summary: Userspace filesystem to provide CGroup-aware values
URL: http://linuxcontainers.org/lxcfs/
License: Apache 2
Group: System/Kernel and hardware
BuildRequires: pkgconfig(fuse)
BuildRequires: pam-devel

%description
LXCFS is a simple userspace filesystem designed to work around some
current limitations of the Linux kernel.

Specifically, it's providing two main things

A set of files which can be bind-mounted over their /proc originals
to provide CGroup-aware values.
A cgroupfs-like tree which is container aware.
The code is pretty simple, written in C using libfuse.

The main driver for this work was the need to run systemd based
containers as a regular unprivileged user while still allowing
systemd inside the container to interact with cgroups.

Now with the introduction of the cgroup namespace in the Linux
kernel, that part is no longer necessary on recent kernels and
focus is now on making containers feel more like a real independent
system through the proc masking feature.

%prep
%setup -q
%configure

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/lxcfs
/%{_lib}/security/pam_cgfs.so
%{_libdir}/liblxcfs.so
%{_datadir}/lxc
%{_datadir}/lxcfs
%{_mandir}/man1/*
