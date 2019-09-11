#!/usr/bin/python

"""
Mdx
"""
import os
import random
#import argparse
import subprocess

import click


@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
@click.argument('-w')
def new(name):
    BASE_DIR = os.path.join(os.getcwd(), name)
    subprocess.run(["git", "clone", "https://github.com/ChanMo/django_boilerplate.git", name])
    #os.chdir(os.path.join(BASE_DIR, name))
    #subprocess.run(["docker", "build", "--tag=django", "."])
    subprocess.run(["docker", "run", "--rm", "--mount", "type=bind,src={},target=/app".format(BASE_DIR), "django", "django-admin", "startproject", "api"])
    subprocess.run(["sudo", "chown", "chen:chen", name, "-R"])
    #subprocess.run(["docker", "image", "rm", "django"])
    subprocess.run(["cp", "local.example.py", "api/api/local.py"], cwd=name)
    subprocess.run(["cp", "web-dockerfile", "api/Dockerfile"], cwd=name)
    subprocess.run(["cp", "requirements.txt", "api/requirements.txt"], cwd=name)

    subprocess.run(["git", "clone", "https://github.com/react-boilerplate/react-boilerplate", "web"])

cli.add_command(new)

if __name__ == '__main__':
    cli()
