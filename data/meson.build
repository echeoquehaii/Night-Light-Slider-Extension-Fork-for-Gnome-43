gse_schema = files([
  gse_prefix + '.gschema.xml',
])

install_data(gse_schema, install_dir: schemadir)

# Test if schema compiles
compile_schemas = find_program('glib-compile-schemas', required: false)
if compile_schemas.found()
  test('Validate schema file', compile_schemas, args: ['--strict', '--dry-run', meson.current_source_dir()])
endif
