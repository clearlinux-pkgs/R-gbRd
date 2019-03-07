#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gbRd
Version  : 0.4.11
Release  : 3
URL      : https://cran.r-project.org/src/contrib/gbRd_0.4-11.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gbRd_0.4-11.tar.gz
Summary  : Utilities for processing Rd objects and files
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
Extract argument descriptions and other parts of the help pages
        of functions.

%prep
%setup -q -c -n gbRd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535122865

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1535122865
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gbRd
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gbRd
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gbRd
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library gbRd|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gbRd/DESCRIPTION
/usr/lib64/R/library/gbRd/INDEX
/usr/lib64/R/library/gbRd/Meta/Rd.rds
/usr/lib64/R/library/gbRd/Meta/features.rds
/usr/lib64/R/library/gbRd/Meta/hsearch.rds
/usr/lib64/R/library/gbRd/Meta/links.rds
/usr/lib64/R/library/gbRd/Meta/nsInfo.rds
/usr/lib64/R/library/gbRd/Meta/package.rds
/usr/lib64/R/library/gbRd/NAMESPACE
/usr/lib64/R/library/gbRd/R/gbRd
/usr/lib64/R/library/gbRd/R/gbRd.rdb
/usr/lib64/R/library/gbRd/R/gbRd.rdx
/usr/lib64/R/library/gbRd/help/AnIndex
/usr/lib64/R/library/gbRd/help/aliases.rds
/usr/lib64/R/library/gbRd/help/gbRd.rdb
/usr/lib64/R/library/gbRd/help/gbRd.rdx
/usr/lib64/R/library/gbRd/help/paths.rds
/usr/lib64/R/library/gbRd/html/00Index.html
/usr/lib64/R/library/gbRd/html/R.css
