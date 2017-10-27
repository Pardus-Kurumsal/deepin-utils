#! /usr/bin/env python

import sys
from setuptools import setup, Extension
import subprocess

def pkg_config(pkgs, include=True):
    if include:
        arg = "--cflags-only-I"
    else:
        arg = "--libs-only-l"
    commands = 'pkg-config %s %s' % (arg, ' '.join(pkgs))
    try:
        output = subprocess.check_output(commands, shell=True).strip()
        return [path[2:] for path in output.split(" ") if path != ""]
    except subprocess.CalledProcessError as e:
        print "Error executed commands: %s" % e.cmd
        sys.exit(1)

cairo_mod = Extension('dtk_cairo_blur',
                include_dirs = pkg_config(['cairo', 'pygobject-2.0'], True),
                libraries = ['cairo', 'pthread', 'glib-2.0'],
                sources = ['./deepin_utils/cairo_blur.c'])
webkit_mod = Extension('dtk_webkit_cookie',
                include_dirs = pkg_config(['gtk+-2.0', 'webkit-1.0', 'pygobject-2.0'], True),
                libraries = ['webkitgtk-1.0', 'soup-2.4', 'pthread', 'glib-2.0'],
                sources = ['./deepin_utils/webkit_cookie.c'])
deepin_font_icon_mod = Extension('deepin_font_icon',
                include_dirs = pkg_config(['gtk+-2.0', 'pycairo', "pygobject-2.0"], True),
                libraries = pkg_config(['gtk+-2.0', 'pycairo', "pygobject-2.0"], False),
                sources = ['./deepin_utils/deepin_font_icon.c'])

setup(name='deepin_utils',
      version='1.0',
      ext_modules = [cairo_mod, webkit_mod, deepin_font_icon_mod],
      description='Basic utils for all projects in Linux Deepin.',
      long_description ="""Python download library for Linux DeepinBasic utils for all projects in Linux Deepin.""",
      author='Wang Yong',
      author_email='wangyong@linuxdeepin.com',
      license='GPL-3',
      url="https://github.com/linuxdeepin/deepin-utils",
      download_url="git://github.com/linuxdeepin/deepin-utils.git",
      platforms = ['Linux'],
      packages = ['deepin_utils'],
      )

