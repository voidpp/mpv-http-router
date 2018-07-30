from setuptools import setup, find_packages
import platform

install_requires = [
    'Flask~=1.0',
    'Flask-Sockets~=0.2',
    'zeroconf~=0.20.0',
]

if platform.system() != 'Darwin':
    install_requires.append('watchdog~=0.8')

setup(
    name = "mpv-http-router",
    version = "0.0.1",
    description = "Redistribute MPV ipc server sockets",
    author = 'Lajos Santa',
    author_email = 'santa.lajos@gmail.com',
    url = '',
    license = 'MIT',
    install_requires = install_requires,
    packages = find_packages(),
    extras_require = {},
    scripts = [
        'bin/mpv-http-router'
    ],
)
