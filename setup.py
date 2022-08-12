from importlib.metadata import entry_points
from setuptools import setup

setup(
    name        = "example_package",
    package_dir = {"example_pkg": "src"},
    packages    = ["example_pkg"]
)
