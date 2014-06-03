#!/bin/env python

from setuptools import setup, find_packages 


VERSION = "0.0.1"

long_description = '''Libraries that interface with Apache Mesos'
External Container interfaces'''

setup_info=dict(name="mesos-docker-containerizer",
            version=VERSION,
            author="Tom Arnfeld",
            author_email="tarnfeld@me.com",
            description="Mesos Container Interface",
            long_description=long_description,
            packages=find_packages(),
            scripts=["bin/docker-containerizer"],
            data_files=[("/etc/default", ["etc/default/containerizer"]),
                        ("/opt/containerizer", ["requirements.pip"]),
                        ("/opt/containerizer/bin", ["bin/setup"])
                        ])


setup(**setup_info)
