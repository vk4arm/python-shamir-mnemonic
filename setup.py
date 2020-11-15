import os.path

from setuptools import setup

# fmt: off
REQUIREMENTS = [
    "attrs",
    "click>=7,<8",
    "colorama",
]
# fmt: on

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="shamir-ru-mnemonic",
    version="0.1.0",
    description="Funny localization for SLIP-39 Shamir Mnemonics",
    long_description=long_description,
    url="https://github.com/vk4arm/python-ru-shamir-mnemonic",
    author="Eastern Angels feat Satoshi Labs",
    packages=["shamir_ru_mnemonic"],
    python_requires=">=3.6",
    install_requires=REQUIREMENTS,
    package_data={"shamir_ru_mnemonic": ["wordlist.txt"]},
    entry_points={"console_scripts": ["rushamir=shamir_ru_mnemonic.cli:cli"]},
    classifiers=[
        "License :: Sorry, i removed it from here. It is just a project-for-fun )",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
