from invoke import task
import os
import shutil
from glob import glob

@task
def clean(c):
    patterns = ["build","dist","**/*.egg-info"]
    for pattern in patterns:
        for path in glob(pattern, recursive = True):
            shutil.rmtree(path)

@task
def develop(c):
    c.run("python setup.py develop")

@task
def install(c):
    c.run("python setup.py install")

@task
def uninstall(c):
    c.run("pip uninstall -y example-package")