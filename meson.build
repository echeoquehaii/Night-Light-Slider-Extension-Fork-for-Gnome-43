project('night-light-slider.timur@linux.com',
  version: '23',
  license: 'GPL2+',
  meson_version: '>= 0.50.0')

gnome = import('gnome')
i18n = import('i18n')

# Extension information
gse_uuid = meson.project_name()
gse_prefix = 'org.gnome.shell.extensions.nightlightslider'
gettext_domain = gse_uuid

# Installation directories
prefixdir = get_option('prefix')
datadir = get_option('datadir')
schemadir = datadir/'glib-2.0'/'schemas'
extensiondir = datadir/'gnome-shell'/'extensions'/gse_uuid

subdir('src')
subdir('data')
subdir('po')

# Create release zip for distribution
custom_target('extension.zip',
  command: [
    'gnome-extensions', 'pack', prefixdir/extensiondir,
    '--extra-source', 'convenience.js',
    '--extra-source', 'prefs.ui',
    '--schema', prefixdir/schemadir/gse_prefix + '.gschema.xml',
    '--podir', meson.current_source_dir()/'po',
    '--gettext-domain', gettext_domain,
  ],
  output:  gse_uuid + '.shell-extension.zip')

# Post-install scripts
meson.add_install_script('build-aux'/'postinstall.py')
