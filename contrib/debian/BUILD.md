Packaged using Debian helper [dh-python][1] method

Install build dependencies

    # apt install -y dpkg-dev devscripts git-buildpackage git

Install run dependencies

    # apt install -y python3-psutil

Build Debian package

    # git clone https://github.com/sbz/memtop
    # cp -r memtop/contrib/debian memtop
    # cd memtop
    # git-buildpackage --git-ignore-new --git-purge --git-builder='dpkg-buildpackage -tc -us -uc'

Generated package will be in $PWD/../*.deb

[1]: http://debian-python.readthedocs.io/en/latest/dh_python.html
