Enable [EPEL][1] repository

	# yum install -y epel-release

Install build dependencies

	# yum install -y rpm-build python-setuptools

Install run dependencies

	# yum install -y python-psutil

Build RPM package

    # mkdir -p ~/rpmbuild/SOURCES/
    # curl -L https://github.com/sbz/memtop/archive/master.tar.gz > ~/rpmbuild/SOURCES/memtop-master.tar.gz
	# rpmbuild -bb memtop.spec

Generated package will be in ~/rpmbuild/RPMS/noarch/

[1]: https://fedoraproject.org/wiki/EPEL
