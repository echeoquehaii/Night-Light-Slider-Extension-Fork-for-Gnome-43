gse_sources = files([
  'convenience.js',
  'extension.js',
  'prefs.js',
  'prefs.ui',
])

# Create metadata file
gse_conf = configuration_data()
gse_conf.set('uuid', gse_uuid)
gse_conf.set('version', meson.project_version())
gse_conf.set('settings_schema', gse_prefix)
gse_conf.set('gettext_domain', gettext_domain)
metadata_json = configure_file(
  input: 'metadata.json.in',
  output: 'metadata.json',
  configuration: gse_conf,
)
gse_sources += metadata_json

install_data(gse_sources, install_dir: extensiondir)
