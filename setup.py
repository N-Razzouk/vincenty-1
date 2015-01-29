try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='vincenty',
    version='0.1.0',
    description='Calculate the geographical distance between 2 points with extreme accuracy.',
    long_description=open('README.txt').read(),
    author='Maurycy Pietrzak',
    author_email=['github.com@wayheavy.com'],
    url='https://github.com/maurycyp/vincenty',
    packages=['vincenty'],
    license=open('LICENSE').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    # TODO zip_safe, package_data
)