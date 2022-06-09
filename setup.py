from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in payu_integration/__init__.py
from payu_integration import __version__ as version

setup(
	name="payu_integration",
	version=version,
	description="Pay U Money Integration with ERPNext",
	author="Aashish & Satya",
	author_email="aashishvashisht6@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
