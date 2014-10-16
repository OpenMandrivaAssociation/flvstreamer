%define name 	flvstreamer
%define version 2.1c1
%define release 2

Summary: 	Open source command line RTMP client
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPLv2+
Group: 		Networking/File transfer
Url: 		http://savannah.nongnu.org/projects/flvstreamer
Source: 	http://mirrors.linhub.com/savannah/flvstreamer/source/flvstreamer-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-root

%description
Flvstreamer is an open source command-line RTMP client intended to stream 
audio or video content from all types of flash or rtmp servers. Forked from 
rtmpdump v1.6 with encrypted rtmp and swf verification support removed. This 
tool provides free interoperability with the previously undocumented adobe 
RTMP protocol so widely in use on the internet today. It was developed 
entirely by reverse engineering methods and without access to any proprietary 
or restrictive-license protocol specifications. 

%prep
%setup -q -n %{name}

%build
%make posix OPT="%optflags" XLDFLAGS="%{?ldflags}"

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
find -type f -perm -u+x | xargs install -m755 -t %{buildroot}%{_bindir}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/flvstreamer
%{_bindir}/streams
%{_bindir}/rtmpsrv
%{_bindir}/rtmpsuck
