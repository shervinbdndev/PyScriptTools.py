import os
import codecs
from setuptools import (setup, find_packages)


with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)) , "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


setup(
    name="PyScriptTools",
    version='4.3.9',
    author="Shervin Badanara (shervinbdndev)",
    maintainer="Shervin Badanara",
    author_email="shervin2234@gmail.com",
    description='Simple Python Package to Gather and Show Your System Info.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages() ,
    project_urls={
        'Source':'https://www.github.com/shervinbdndev/PyScriptTools/'
    },
    license='MIT',
    install_requires=['GPUtil' , 'requests' , 'sockets' , 'colorama' , 'python-cfonts' , 'setuptools' , 'wheel' , 'getmac' , 'psutil'] ,
    keywords=['python', 'system', 'systeminfo', 'local ip', 'public ip', 'sockets' , 'cpu info' , 'gpu info' , 'ram info' , 'disk info'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ] ,
    extras_require={
        'dev':['check-manifest'] ,
        'test' : ['coverage'] ,
    }
)