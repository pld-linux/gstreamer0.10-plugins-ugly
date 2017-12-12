#
# Conditional build:
%bcond_without	cdio		# cdio plugin
%bcond_without	sid		# sid plugin
%bcond_without	amr		# AMR-NB/AMR-WB plugins

%define		gstname		gst-plugins-ugly
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.36
%define		gstpb_req_ver	0.10.36

%include	/usr/lib/rpm/macros.gstreamer
Summary:	Ugly GStreamer Streaming-media framework plugins
Summary(pl.UTF-8):	Brzydkie wtyczki do środowiska obróbki strumieni GStreamer
Name:		gstreamer0.10-plugins-ugly
Version:	0.10.19
Release:	10
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-ugly/%{gstname}-%{version}.tar.xz
# Source0-md5:	ba26045c8c8c91f0d48d327ccf53ac0c
Patch0:		amr-includes.patch
Patch1:		libcdio.patch
Patch2:		gstreamer-common-gtkdoc.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.10
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.24
BuildRequires:	gstreamer0.10-devel >= %{gst_req_ver}
BuildRequires:	gstreamer0.10-plugins-base-devel >= %{gstpb_req_ver}
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	libtool >= 1.4
BuildRequires:	orc-devel >= 0.4.11
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python >= 2.1
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
##
## plugins
##
BuildRequires:	a52dec-libs-devel
BuildRequires:	lame-libs-devel
%{?with_cdio:BuildRequires:	libcdio-devel >= 0.76}
# not yet
#BuildRequires:	libdvdnav-devel >= 0.1.7
BuildRequires:	libdvdread-devel
BuildRequires:	libid3tag-devel >= 0.15
BuildRequires:	libmad-devel >= 0.15
BuildRequires:	libmpeg2-devel >= 0.5.1
%{?with_sid:BuildRequires:	libsidplay-devel >= 1.36.57}
# ABI 55
BuildRequires:	libx264-devel >= 0.1.3
%{?with_amr:BuildRequires:	opencore-amr-devel}
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	twolame-devel >= 0.3.10
Requires:	glib2 >= 1:2.24
Requires:	gstreamer >= %{gst_req_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Requires:	orc >= 0.4.11
Obsoletes:	gstreamer-asf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%description -l pl.UTF-8
GStreamer to środowisko obróbki danych strumieniowych, bazujące na
grafie filtrów operujących na danych medialnych. Aplikacje używające
tej biblioteki mogą robić wszystko od przetwarzania dźwięku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego związego z
mediami. Architektura bazująca na wtyczkach pozwala na łatwe dodawanie
nowych typów danych lub możliwości obróbki.

##
## Plugins
##

%package -n gstreamer0.10-a52dec
Summary:	GStreamer VOB decoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera dekodująca VOB
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-a52dec < 1.0

%description -n gstreamer0.10-a52dec
Plugin for decoding of VOB files.

%description -n gstreamer0.10-a52dec -l pl.UTF-8
Wtyczka dekodująca pliki VOB.

%package -n gstreamer0.10-amrnb
Summary:	GStreamer AMR-NB decoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera dekodująca pliki AMR-NB
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-amrnb < 1.0

%description -n gstreamer0.10-amrnb
Plugin for decoding of AMR-NB files.

%description -n gstreamer0.10-amrnb -l pl.UTF-8
Wtyczka dekodująca pliki AMR-NB.

%package -n gstreamer0.10-amrwb
Summary:	GStreamer AMR-WB decoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera dekodująca pliki AMR-WB
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-amrwb < 1.0

%description -n gstreamer0.10-amrwb
Plugin for decoding of AMR-WB files.

%description -n gstreamer0.10-amrwb -l pl.UTF-8
Wtyczka dekodująca pliki AMR-WB.

%package -n gstreamer0.10-cdio
Summary:	GStreamer plugin for CD audio input using libcdio
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca płyty CD-Audio przy użyciu libcdio
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	libcdio >= 0.76
Obsoletes:	gstreamer-cdio < 1.0

%description -n gstreamer0.10-cdio
Plugin for playing audio tracks using libcdio under GStreamer.

%description -n gstreamer0.10-cdio -l pl.UTF-8
Wtyczka do odtwarzania ścieżek dźwiękowych pod GStreamerem za pomocą
libcdio.

%package -n gstreamer0.10-dvdread
Summary:	GStreamer plugin for DVD playback
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca DVD
Group:		Libraries
# for NLS
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-dvdread < 1.0
Obsoletes:	gstreamer-libdvdread < 0.11

%description -n gstreamer0.10-dvdread
GStreamer plugin for DVD playback.

%description -n gstreamer0.10-dvdread -l pl.UTF-8
Wtyczka odtwarzająca DVD do GStreamera.

%package -n gstreamer0.10-lame
Summary:	GStreamer plugin encoding MP3 songs
Summary(pl.UTF-8):	Wtyczka do GStreamera kodująca pliki MP3
Group:		Libraries
# for NLS
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	twolame-libs >= 0.3.10
Obsoletes:	gstreamer-lame < 1.0

%description -n gstreamer0.10-lame
Plugin for encoding MP3 with lame.

%description -n gstreamer0.10-lame -l pl.UTF-8
Wtyczka do GStreamera kodująca pliki MP3 przy użyciu lame.

%package -n gstreamer0.10-mad
Summary:	GStreamer plugin using MAD for MP3 decoding
Summary(pl.UTF-8):	Wtyczka do GStreamera używająca MAD do dekodowania MP3
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-mad < 1.0

%description -n gstreamer0.10-mad
Plugin for playback of MP3 songs using the very good MAD library.

%description -n gstreamer0.10-mad -l pl.UTF-8
Wtyczka do odtwarzania plików MP3 przy użyciu bardzo dobrej biblioteki
MAD.

%package -n gstreamer0.10-mpeg
Summary:	GStreamer plugins for MPEG video playback
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca obraz MPEG
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-mpeg < 1.0

%description -n gstreamer0.10-mpeg
Plugins for playing MPEG videos.

%description -n gstreamer0.10-mpeg -l pl.UTF-8
Wtyczki do odtwarzania obrazu MPEG.

%package -n gstreamer0.10-sid
Summary:	GStreamer Sid C64 music plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca muzykę Sid C64
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-sid < 1.0

%description -n gstreamer0.10-sid
Plugin for playback of C64 SID format music files.

%description -n gstreamer0.10-sid -l pl.UTF-8
Wtyczka do odtwarzania plików z muzyką w formacie C64 SID.

%package -n gstreamer0.10-x264
Summary:	GStreamer x264 encoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera kodująca przy użyciu biblioteki x264
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gst_req_ver}
Obsoletes:	gstreamer-x264 < 1.0

%description -n gstreamer0.10-x264
GStreamer x264 encoder plugin.

%description -n gstreamer0.10-x264 -l pl.UTF-8
Wtyczka do GStreamera kodująca przy użyciu biblioteki x264.

%prep
%setup -q -n %{gstname}-%{version}
%patch0 -p1
%patch1 -p1
cd common
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_amr:--disable-amrnb --disable-amrwb} \
	%{!?with_cdio:--disable-cdio} \
	%{!?with_sid:--disable-sidplay} \
	--disable-silent-rules \
	--disable-static \
	--enable-experimental \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
rm -f $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang %{gstname}-%{gst_major_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{gstname}-%{gst_major_ver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{gstlibdir}/libgstasf.so
%attr(755,root,root) %{gstlibdir}/libgstdvdlpcmdec.so
%attr(755,root,root) %{gstlibdir}/libgstdvdsub.so
%attr(755,root,root) %{gstlibdir}/libgstiec958.so
%attr(755,root,root) %{gstlibdir}/libgstrmdemux.so
%attr(755,root,root) %{gstlibdir}/libgstsynaesthesia.so
%{_datadir}/gstreamer-%{gst_major_ver}/presets
%{_gtkdocdir}/gst-plugins-ugly-plugins-0.10

##
## Plugins
##

%files -n gstreamer0.10-a52dec
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsta52dec.so

%if %{with amr}
%files -n gstreamer0.10-amrnb
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstamrnb.so

%files -n gstreamer0.10-amrwb
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstamrwbdec.so
%endif

%if %{with cdio}
%files -n gstreamer0.10-cdio
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcdio.so
%endif

%files -n gstreamer0.10-dvdread
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdvdread.so

%files -n gstreamer0.10-lame
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstlame.so
%attr(755,root,root) %{gstlibdir}/libgsttwolame.so

%files -n gstreamer0.10-mad
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmad.so

%files -n gstreamer0.10-mpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmpeg2dec.so
%attr(755,root,root) %{gstlibdir}/libgstmpegaudioparse.so
%attr(755,root,root) %{gstlibdir}/libgstmpegstream.so

%if %{with sid}
%files -n gstreamer0.10-sid
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsid.so
%endif

%files -n gstreamer0.10-x264
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstx264.so
