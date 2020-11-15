#!/usr/bin/env python3

import os
import subprocess

prefix = os.environ.get('MESON_INSTALL_PREFIX', '/usr/local')
datadir = os.path.join(prefix, 'share')

# Packaging tools define DESTDIR and this isn't needed for them
if 'DESTDIR' not in os.environ:
    print('Compiling GSettings schemas...')
    schemas_dir = os.path.join(datadir, 'glib-2.0', 'schemas')
    if not os.path.exists(schemas_dir):
        os.makedirs(schemas_dir)
    subprocess.call(['glib-compile-schemas', schemas_dir])
