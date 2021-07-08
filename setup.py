from setuptools import find_packages, setup

install_requires = []

with open("requirements.txt") as file:
    install_requires.extend(file.read().splitlines())

setup(
    name="Data-Driven-Business",
    version="1.0.0",
    description="Recognizing forests from aerial photos",
    author="Wail Abou",
    author_email="wail.abou@student.hu.nl",
    packages=find_packages(),
    install_requires=install_requires,
)