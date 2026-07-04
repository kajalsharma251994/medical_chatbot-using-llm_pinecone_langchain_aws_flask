#Find all the requirements from the requirements.txt file and install them

from setuptools import find_packages, setup

setup(
    name="medical_chatbot",
    version="0.1.0",
    author="Kajal Sharma",
    author_email="kajalssharma.25@gmail.com",
    packages=find_packages(),
    install_requires=[]
)