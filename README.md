# memtop

Rapidly crafted memory top script using Python.

Install with pip
================

```
pip install -e 'git+https://github.com/sbz/memtop#egg=master'
```

Install with Debian package
===========================

In order to generate a Debian package, follow the build instructions [here](contrib/debian/BUILD.md)

After the package is generated, run

```
dpkg -i memtop*.deb
```

Install with RPM package
========================

In order to generate a RPM package, follow the build instructions [here](contrib/rpm/BUILD.md)

After the package is generated, run

```
yum -y localinstall memtop*.rpm
```
