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
@click.option('--web', default=False, help='create react web dir?')
def new(web, name):
    BASE_DIR = os.path.join(os.getcwd(), name)
    subprocess.run(["git", "clone", "https://github.com/ChanMo/django_boilerplate.git", name])
    #os.chdir(os.path.join(BASE_DIR, name))
    subprocess.run(["docker", "build", "--tag=django", "."])
    subprocess.run(["docker", "run", "--rm", "--mount", "type=bind,src={},target=/app".format(BASE_DIR), "django", "django-admin", "startproject", "api"])
    subprocess.run(["sudo", "chown", "chen:chen", name, "-R"]) # need impro
    #subprocess.run(["docker", "image", "rm", "django"])
    subprocess.run(["cp", "local.example.py", "api/api/local.py"], cwd=name)
    subprocess.run(["cp", "api-dockerfile", "api/Dockerfile"], cwd=name)
    subprocess.run(["cp", "requirements.txt", "api/requirements.txt"], cwd=name)

    if web:
        subprocess.run(["git", "clone", "https://github.com/react-boilerplate/react-boilerplate", "web"])
        os.chdir('web')
        subprocess.run(["docker", "build", "--tag=react", "."])
        subprocess.run(["docker", "run", "--rm", "--mount", "type=bind,src={}/web,target=/app".format(BASE_DIR), "react", "npm", "install"])


cli.add_command(new)

if __name__ == '__main__':
    cli()
