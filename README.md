CMake ExternalProject with add_dependencies
===========================================

This small project intents to illustrate how to properly use `ExternalProject_Add`
with `add_dependencies`

Usage
-----

```
git clone git://github.com/jcfr/CMake-ExternalProject-with-AddDependencies
mkdir CMake-ExternalProject-with-AddDependencies-build && cd $_
cmake ../CMake-ExternalProject-with-AddDependencies
make -j5
```

Issues
------

When building with `make -j5`, the project 'python-smmap' and 'PyGithub' are expected to be built
sequentially. This small project shows that this is currently not the case.

Remarks
-------

The name of the external projects used in this example are purely illustrative. The intent is not
build these projects (PyGithub, ...) but simply to show how to use `ExternalProject_Add`
with `add_dependencies`.

Licensing
---------

Materials in this repository are distributed under the following licenses:

All Works of Art are licensed under the Creative Commons Attribution-ShareAlike 3.0.
See LICENSE_CC_BY_SA_30 file for details.
