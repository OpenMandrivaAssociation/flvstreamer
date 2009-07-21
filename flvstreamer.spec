%define name 	flvstreamer
%define version 1.8e
%define release %mkrel 2

Summary: 	Open source command line RTMP client
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
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
%make %{name} streams

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
%ifarch i586
	install -m 755 flvstreamer_x86 %{buildroot}%{_bindir}/
	install -m 755 streams_x86 %{buildroot}%{_bindir}/
%endif

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(755,root,root)
%doc README
%{_bindir}/flvstreamer_x86
%{_bindir}/streams_x86
