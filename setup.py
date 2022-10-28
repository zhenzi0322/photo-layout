from setuptools import setup, find_packages
import os


def get_version():
    """
    Get package version.
    """
    curdir = os.path.dirname(__file__)
    filename = os.path.join(curdir, 'src', 'photo_layout', 'version.py')
    with open(filename, 'r') as fp:
        return fp.read().split('=')[1].strip(" \r\n'")



setup(
    name='photo-layout',
    version=get_version(),
    author='玉振',
    author_email='82131529@qq.com',
    url='https://github.com/zhenzi0322/photo-layout',
    description='Photo Layout',
    long_description=(open("README.rst", encoding="utf-8").read()),
    long_description_content_type="text/x-rst",
    license='MIT License',
    keywords="photo-layout",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        "pillow >= 8.4.0",
        "pydantic >= 1.9.0"
    ],
    python_requires=">=3",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Viewers',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
