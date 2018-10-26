from setuptools import setup, find_packages
import platform

install_requires = [
    'Flask~=1.0',
    'Flask-Sockets~=0.2',
    'Flask-Cors~=3.0',
    'zeroconf~=0.20',
    'configpp~=0.1',
]

if platform.system() != 'Darwin':
    install_requires.append('watchdog~=0.8')

setup(
    name = "mpv-http-router",
    version = "0.8.0",
    description = "Redistribute MPV ipc server sockets",
    author = 'Lajos Santa',
    author_email = 'santa.lajos@gmail.com',
    url = 'https://github.com/voidpp/mpv-http-router',
    license = 'MIT',
    install_requires = install_requires,
    packages = find_packages(),
    extras_require = {},
    scripts = [
        'bin/mpv-http-router'
    ],
    classifiers = {
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    },
)
