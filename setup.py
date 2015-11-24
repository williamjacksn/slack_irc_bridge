from setuptools import find_packages, setup

setup(
    name='slirck',
    version='0.7',
    install_requires=['aiohttp'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'slirck = slirck.slirck:main'
        ]
    }
)
