#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v19
# autospec commit: f35655a
#
Name     : R-VGAMdata
Version  : 1.1.12
Release  : 53
URL      : https://cran.r-project.org/src/contrib/VGAMdata_1.1-12.tar.gz
Source0  : https://cran.r-project.org/src/contrib/VGAMdata_1.1-12.tar.gz
Summary  : Data Supporting the 'VGAM' Package
Group    : Development/Tools
License  : GPL-2.0
Requires: R-VGAM
BuildRequires : R-VGAM
BuildRequires : buildreq-R

%description
the book "Vector Generalized Linear and

%prep
%setup -q -n VGAMdata
pushd ..
cp -a VGAMdata buildavx2
popd
pushd ..
cp -a VGAMdata buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726581657

%install
export SOURCE_DATE_EPOCH=1726581657
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/VGAMdata/CITATION
/usr/lib64/R/library/VGAMdata/DESCRIPTION
/usr/lib64/R/library/VGAMdata/INDEX
/usr/lib64/R/library/VGAMdata/Meta/Rd.rds
/usr/lib64/R/library/VGAMdata/Meta/data.rds
/usr/lib64/R/library/VGAMdata/Meta/demo.rds
/usr/lib64/R/library/VGAMdata/Meta/features.rds
/usr/lib64/R/library/VGAMdata/Meta/hsearch.rds
/usr/lib64/R/library/VGAMdata/Meta/links.rds
/usr/lib64/R/library/VGAMdata/Meta/nsInfo.rds
/usr/lib64/R/library/VGAMdata/Meta/package.rds
/usr/lib64/R/library/VGAMdata/NAMESPACE
/usr/lib64/R/library/VGAMdata/NEWS
/usr/lib64/R/library/VGAMdata/R/VGAMdata
/usr/lib64/R/library/VGAMdata/R/VGAMdata.rdb
/usr/lib64/R/library/VGAMdata/R/VGAMdata.rdx
/usr/lib64/R/library/VGAMdata/data/Rdata.rdb
/usr/lib64/R/library/VGAMdata/data/Rdata.rds
/usr/lib64/R/library/VGAMdata/data/Rdata.rdx
/usr/lib64/R/library/VGAMdata/demo/binom2.or.R
/usr/lib64/R/library/VGAMdata/demo/cqo.R
/usr/lib64/R/library/VGAMdata/demo/distributions.R
/usr/lib64/R/library/VGAMdata/demo/lmsqreg.R
/usr/lib64/R/library/VGAMdata/demo/vgam.R
/usr/lib64/R/library/VGAMdata/demo/zipoisson.R
/usr/lib64/R/library/VGAMdata/help/AnIndex
/usr/lib64/R/library/VGAMdata/help/VGAMdata.rdb
/usr/lib64/R/library/VGAMdata/help/VGAMdata.rdx
/usr/lib64/R/library/VGAMdata/help/aliases.rds
/usr/lib64/R/library/VGAMdata/help/paths.rds
/usr/lib64/R/library/VGAMdata/html/00Index.html
/usr/lib64/R/library/VGAMdata/html/R.css
