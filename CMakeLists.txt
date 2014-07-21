cmake_minimum_required(VERSION 2.8.9)

include(ExternalProject)

#-- SuperBuild -     python-setuptools => Requires python[INCLUDED],
#-- SuperBuild -     python-setuptools[OK]
# [...]
#-- SuperBuild -   pydicom => Requires python[INCLUDED], python-setuptools[INCLUDED],
#-- SuperBuild -   pydicom[OK]
#-- SuperBuild -   GitPython => Requires python[INCLUDED], python-setuptools[INCLUDED], python-gitdb,
#-- SuperBuild -     python-gitdb => Requires python[INCLUDED], python-setuptools[INCLUDED], python-async, python-smmap,
#-- SuperBuild -       python-async => Requires python[INCLUDED], python-setuptools[INCLUDED],
#-- SuperBuild -       python-async[OK]
#-- SuperBuild -       python-smmap => Requires python[INCLUDED], python-setuptools[INCLUDED],
#-- SuperBuild -       python-smmap[OK]
#-- SuperBuild -     python-gitdb[OK]
#-- SuperBuild -   GitPython[OK]
#-- SuperBuild -   python-chardet => Requires python[INCLUDED], python-setuptools[INCLUDED], python-async[INCLUDED], python-smmap[INCLUDED],
#-- SuperBuild -   python-chardet[OK]
#-- SuperBuild -   PyGithub => Requires python[INCLUDED], python-setuptools[INCLUDED],
#-- SuperBuild -   PyGithub[OK]

find_package(PythonInterp REQUIRED)

function(add_proj name)
  set(seconds_config 1)
  set(seconds_build 3)
  set(seconds_install 2)
  set(proj "${name}")
  set(depends_args)
  message("${proj} -> ${ARGN}")
  if(ARGN)
    set(depends_args DEPENDS ${ARGN})
  endif()
  ExternalProject_Add(${proj}
    ${depends_args}
    DOWNLOAD_COMMAND ""
    CONFIGURE_COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_SOURCE_DIR}/patience.py ${proj} config ${seconds_config}
    BUILD_COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_SOURCE_DIR}/patience.py ${proj} build ${seconds_build}
    INSTALL_COMMAND ${CMAKE_SOURCE_DIR}/patience.py ${proj} install ${seconds_install}
    )
endfunction()

add_proj(python "")
add_proj(python-setuptools python)

add_proj(python-async python python-setuptools)
add_proj(python-smmap python python-setuptools)

add_proj(python-gitdb python python-setuptools python-async python-smmap)

add_proj(pydicom python python-setuptools)
add_proj(GitPython python python-setuptools python-gitdb)
add_proj(python-chardet python python-setuptools python-async python-smmap)
add_proj(PyGithub python python-setuptools)

#
# The following enable sequential build of the associated targets
#
add_dependencies(pydicom GitPython)
add_dependencies(GitPython python-chardet)
add_dependencies(python-chardet PyGithub)
add_dependencies(python-async python-smmap)

# It means that the targets 'GitPython' and 'PyGithub' are expected to build sequentially. 
# By extension, it means that 'python-smmap' and 'PyGithub'are also expected to build sequentially.

# It turns out this is not the case, when building with 'make -j5', I get the following output:

#
# [ 34%] [ 36%] Performing configure step for 'python-smmap'
# Performing configure step for 'PyGithub'
# [python-smmap] [config] is waiting 0.5s [0.5/1]
# [PyGithub] [config] is waiting 0.5s [0.5/1]
#


