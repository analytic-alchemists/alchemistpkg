from setuptools import setup
from setuptools import find_packages
setup(
    name='alchemistpkg',
    version='0.1.0',
    author='Analytic Alchemists',
    packages=['alchemistpkg', 'configs'],
    include_package_data=True,
    install_requires=['matplotlib', 'requests', 'pyyaml']
)

