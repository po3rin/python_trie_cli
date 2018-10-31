from setuptools import setup, find_packages


with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="pytrie",
    version="0.0.1",
    description="A Trie in computer science is a tree structure that allows you to do things such as very quick lookup of words within the english language.",
    author="po3rin",
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "pytrie=trie.trie:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)