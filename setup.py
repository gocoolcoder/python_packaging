from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'gktools is an assiting package for doing basic math operations'
LONG_DESCRIPTION = 'A package that allows to basic math operations. This package is built as part of a tutorial for packaging phython module'

# Setting up
setup(
    name="gktools",
    version=VERSION,
    author="Gokul Kumar Jayaram",
    author_email="<gokulkumar.jayaram@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'gktools', 'packaging' , 'baisc math'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)