from setuptools import (
    setup,
    find_packages,
)
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="chpronounce",
    version = "0.1.2",
    author="Yi Kuo",
    author_email="kuokuoyiyi@gmail.com",
    url="https://github.com/YiPrograms/chpronounce",
    description="Convert Chinese to zhuyin(bopomofo) or pinyin",
    keywords="chinese pinyin zhuyin bopomofo",
    install_requires=["pkuseg"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3',
    license="MIT",
    packages=find_packages(exclude=['tests*']),
    classifiers=["Development Status :: 3 - Alpha",
                 "Intended Audience :: Developers",
                 "Intended Audience :: Science/Research",
                 "License :: OSI Approved :: MIT License",
                 "Natural Language :: Chinese (Traditional)",
                 "Natural Language :: Chinese (Traditional)",
                 "Programming Language :: Python",
                 'Programming Language :: Python :: 3.7',
                 "Topic :: Text Processing :: Linguistic",
                 "Topic :: Software Development :: Libraries :: Python Modules",
                ],
    package_data={
            '': [
                'README.md',
                'LICENSE',
            ],
            'chpronounce': [
                'xdic.pkl',
                't2s',
                'postag',
            ]
        },
)
