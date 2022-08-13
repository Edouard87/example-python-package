from importlib.metadata import entry_points
from setuptools import setup

setup(
    name        = "example_package",
    package_dir = {"": "src"},
    packages    = ["example_pkg"],
    entry_points = {
        'console_scripts': ['example_cli = example_pkg.module1:cli']
    }
)
