ARG: Image VERSION Fedora:3.5 
Image_Build:
ENV
Cli_Version=DEV
Python_Package=Python3
RUN SUDO APT INSTALL python3 -y
Windows WGET RPM-Build
GCC 
Libf
FI
Python_package --Openssl
-Dev 
# Make bash Core_utils, diff_utils, patch dos2_unix, Perl
WORKDIR /Azure- Cli
# COPY RUN dos2unix ./scripts/release/rpm/azure-cli.spec
&&
\
 #   REPO_PATH=$(pwd) CLI_VERSION=$cli_version PYTHON_PACKAGE=$python_package PYTHON_CMD=python3
\ 
# rpmbuild -v -bb --clean scripts/release/rpm/azure-cli.spec
&&
\  
# cp /root/rpmbuild/RPMS/*/azure-cli-${cli_version}-1.*.rpm /azure-cli-dev.rpm && 
		\
#		mkdir /out && cp /root/rpmbuild/RPMS/*/azure-cli-${cli_version}-1.*.rpm /out/
FROM $imagel 
AS  execution-env
COPY --from=build-env /azure-cli-dev.rpm
./
RUN dnf install -y
./azure-cli-dev.rpm
	&& 
	\ 
	'az  --version'
