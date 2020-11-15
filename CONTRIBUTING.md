## Contributing

- Read the [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md)
- Speak in English, if possible

## Bug Reports, Feature Requests, & Questions

- Fill out the template as best you can

## Code

- Lint your code with [eslint](https://eslint.org/)
- You agree that your code will be distributed under the [GPL-2.0-or-later](LICENSE)

## Building

The extension uses the [meson](https://mesonbuild.com/) build system.

- You can set up a development environment by running `meson setup --prefix=$HOME/.local builddir`
- You can compile and install a build by running `meson install -C builddir`
- Changes to the `meson.build` will require reconfiguring it with `meson --reconfigure builddir`
- You can create a packed extension by running `meson compile extension.zip -C builddir`
