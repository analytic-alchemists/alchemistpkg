from setuptools import setup, find_packages

setup(
    name='alchemistpkg',
    version='0.1.0',
    author='Analytic Alchemists',
    packages=find_packages(),
    install_requires=['matplotlib', 'requests', 'pyyaml'],
    include_package_data=True
)

