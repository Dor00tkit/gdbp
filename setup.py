import os
from setuptools import setup, find_packages

readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
with open(readme_path) as readme:
    long_description = readme.read()

setup(name='gdbp',
      description='A wrapper for GDB\'s Python API - extended by Dor00tkit',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/Dor00tkit/gdbp',
      version='0.1.0',
      packages=find_packages(),
      extras_require={
        'test': ['pytest']
      },
      classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux'
      ])
