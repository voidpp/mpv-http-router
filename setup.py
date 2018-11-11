from setuptools import setup, find_packages
import platform
import json

with open('setup.json') as f:
    data = json.load(f)

if platform.system() != 'Darwin':
    data['install_requires'].append('watchdog~=0.8')

data['packages'] = find_packages()

setup(**data)
