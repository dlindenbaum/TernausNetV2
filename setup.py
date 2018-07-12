import os,sys

from setuptools import setup, find_packages
sys.setdefaultencoding('utf-8')

with open('TernausNetV2/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue


#with open('README.rst') as f:
#    readme = f.read()

# Runtime requirements.
inst_reqs = []

extra_reqs = {
    'test': ['mock', 'pytest', 'pytest-cov', 'codecov']
}
        

setup(name='TernausNetV2',
      version=version,
      description=u"""Run basic Segmentation on  Dataset or arbitrary GeoTIffs""",
      long_description='readme',
      classifiers=[
          'Intended Audience :: Information Technology',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Apache License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: GIS'],
      keywords='segmentation spacenet machinelearning',
      author=u"David Lindenbaum",
      author_email='dlindenbaum@iqt.org',
      url='https://github.com/CosmiQ/cw-nets',
      license='Apache 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=False,
      install_requires=inst_reqs,
      extras_require=extra_reqs)
