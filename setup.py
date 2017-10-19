from setuptools import setup
# from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='locustor',
    version=version,
    description="Tool to execute locust and produce reports",
    author="jamatute",
    author_email="jmm@riseup.net",
    url="https://github.com/jamatute/locustor",
    license='GPLv2',
    packages=['locustor'],
    long_description=open('README.md').read(),
)
