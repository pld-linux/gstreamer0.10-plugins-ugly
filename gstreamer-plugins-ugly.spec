#
# Conditional build:
%bcond_without	sid		# don't build sid plugin
#
%define		gstname		gst-plugins-ugly
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.3
#
Summary:	Ugly GStreamer Streaming-media framework plugins
Summary(pl):	Brzydkie wtyczki do ¶rodowiska obróbki strumieni GStreamer
Name:		gstreamer-plugins-ugly
Version:	0.10.3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-ugly/%{gstname}-%{version}.tar.bz2
# Source0-md5:	af6f238507b0040bf84fcbc6a241e559
Patch0:		%{name}-bashish.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.5
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gst_req_ver}
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	liboil-devel >= 0.3.0
BuildRequires:	libtool >= 1.4
BuildRequires:	pkgconfig >= 1:0.9.0
##
## plugins
##
BuildRequires:	a52dec-libs-devel
BuildRequires:	amrnb-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libid3tag-devel >= 0.15
BuildRequires:	libmad-devel >= 0.15
%{?with_sid:BuildRequires:	libsidplay-devel >= 1.36.57}
BuildRequires:	mpeg2dec-devel >= 0.4.0
BuildRequires:	rpmbuild(macros) >= 1.98
Requires:	gstreamer >= %{gst_req_ver}
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
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

%description -l pl
GStreamer to ¶rodowisko obróbki danych strumieniowych, bazuj±ce na
grafie filtrów operuj±cych na danych medialnych. Aplikacje u¿ywaj±ce
tej biblioteki mog± robiæ wszystko od przetwarzania d¼wiêku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego zwi±zego z
mediami. Architektura bazuj±ca na wtyczkach pozwala na ³atwe dodawanie
nowych typów danych lub mo¿liwo¶ci obróbki.

##
## Plugins
##

%package -n gstreamer-a52dec
Summary:	GStreamer VOB decoder plugin
Summary(pl):	Wtyczka do GStreamera dekoduj±ca VOB
Group:		Libraries

%description -n gstreamer-a52dec
Plugin for decoding of VOB files.

%description -n gstreamer-a52dec -l pl
Wtyczka dekoduj±ca pliki VOB.

%package -n gstreamer-amrnb
Summary:	GStreamer AMR-NB decoder plugin
Summary(pl):	Wtyczka do GStreamera dekoduj±ca pliki AMR-NB
Group:		Libraries

%description -n gstreamer-amrnb
Plugin for decoding of AMR-NB files.

%description -n gstreamer-amrnb -l pl
Wtyczka dekoduj±ca pliki AMR-NB.

%package -n gstreamer-dvdread
Summary:	GStreamer plugin for DVD playback
Summary(pl):	Wtyczka do GStreamera odtwarzaj±ca DVD
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}
Obsoletes:	gstreamer-libdvdread

%description -n gstreamer-dvdread
GStreamer plugin for DVD playback.

%description -n gstreamer-dvdread -l pl
Wtyczka odtwarzaj±ca DVD do GStreamera.

%package -n gstreamer-lame
Summary:	GStreamer plugin encoding MP3 songs
Summary(pl):	Wtyczka do GStreamera koduj±ca pliki MP3
Group:		Libraries

%description -n gstreamer-lame
Plugin for encoding MP3 with lame.

%description -n gstreamer-lame -l pl
Wtyczka do GStreamera koduj±ca pliki MP3 przy u¿yciu lame.

%package -n gstreamer-mad
Summary:	GStreamer plugin using MAD for MP3 decoding
Summary(pl):	Wtyczka do GStreamera u¿ywaj±ca MAD do dekodowania MP3
Group:		Libraries

%description -n gstreamer-mad
Plugin for playback of MP3 songs using the very good MAD library.

%description -n gstreamer-mad -l pl
Wtyczka do odtwarzania plików MP3 przy u¿yciu bardzo dobrej biblioteki
MAD.

%package -n gstreamer-mpeg
Summary:	GStreamer plugins for MPEG video playback and encoding
Summary(pl):	Wtyczka do GStreamera odtwarzaj±ca i koduj±ca obraz MPEG
Group:		Libraries

%description -n gstreamer-mpeg
Plugins for playing and encoding MPEG video.

%description -n gstreamer-mpeg -l pl
Wtyczki do odtwarzania i kodowania obrazu MPEG.

%package -n gstreamer-sid
Summary:	GStreamer Sid C64 music plugin
Summary(pl):	Wtyczka do GStreamera odtwarzaj±ca muzykê Sid C64
Group:		Libraries

%description -n gstreamer-sid
Plugin for playback of C64 SID format music files.

%description -n gstreamer-sid -l pl
Wtyczka do odtwarzania plików z muzyk± w formacie C64 SID.

%prep
%setup -q -n %{gstname}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_sid:--disable-sidplay} \
	--disable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
rm -f $RPM_BUILD_ROOT%{gstlibdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{gstlibdir}/libgstasf.so
%attr(755,root,root) %{gstlibdir}/libgstdvdlpcmdec.so
%attr(755,root,root) %{gstlibdir}/libgstdvdsub.so
%attr(755,root,root) %{gstlibdir}/libgstiec958.so
%attr(755,root,root) %{gstlibdir}/libgstrmdemux.so
%{_gtkdocdir}/gst-plugins-ugly-plugins-*

##
## Plugins
##

%files -n gstreamer-a52dec
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsta52dec.so

%files -n gstreamer-amrnb
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstamrnb.so

%files -n gstreamer-dvdread
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdvdread.so

%files -n gstreamer-lame
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstlame.so

%files -n gstreamer-mad
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmad.so

%files -n gstreamer-mpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmpeg2dec.so
%attr(755,root,root) %{gstlibdir}/libgstmpegaudioparse.so
%attr(755,root,root) %{gstlibdir}/libgstmpegstream.so

%if %{with sid}
%files -n gstreamer-sid
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsid.so
%endif
