# Example Python Package

An example python package structure. Supports `setup.py` to allow it to be installed.

It is recommended to create a virtual environment for testing with `python -m venv ".venv"`. Activate it before running any commands.

This should run properly on Windows, Linux, and Mac. Tested on Windows.

## Installing

Install for development with `invoke develop`. This causes modificatios to the package to be persisted without needing to uninstall and reinstall the package.

After the package was installed, import it into the python interpreter with `import example_pkg`.

## Uninstalling

Uninstall with `invoke uninstall` whether the module was installed as `develop` or `install`. After the command is run, importing the package will raise an `ImportError` and the `cli` to output `command not found`.

If the package was installed in development mode, uninstalling and reinstalling is only necessary when `setup.py` is modified.

If the package was installed using `invoke install`, uninstalling and reinstalling is necessary when the package itself or `setup.py` is modified.

## Docs

`example_pkg` contains a single module named `module1`. `module1` contains two methods called `func_1` and `cli`, and a class called `TestClass`. These just output things in the terminal.

## CLI Entrypoint

The module also contains a CLI entrypoint which should be installed automatically in your `Scripts` directory with `invoke develop`. Run it with `example_cli` in the terminal assuming your `PATH` environment variable is configured correctly.
