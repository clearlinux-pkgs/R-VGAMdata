#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-VGAMdata
Version  : 1.0.3
Release  : 13
URL      : https://cran.r-project.org/src/contrib/VGAMdata_1.0-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/VGAMdata_1.0-3.tar.gz
Summary  : Data Supporting the 'VGAM' Package
Group    : Development/Tools
License  : GPL-2.0
Requires: R-VGAM
BuildRequires : R-VGAM
BuildRequires : clr-R-helpers

%description
the book "Vector Generalized Linear and

%prep
%setup -q -c -n VGAMdata

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521269728

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521269728
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library VGAMdata
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library VGAMdata
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library VGAMdata
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library VGAMdata|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/VGAMdata/data/datalist
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
