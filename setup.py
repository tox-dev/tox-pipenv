from setuptools import setup

import tox_pipenv

with open('README.rst') as readme:
    long_description = readme.read()


_version = tox_pipenv.__version__

requirements = [
    'tox==2.9.1',
    'pipenv==9.0.1'
]

def main():
    setup(
        name='tox-pipenv',
        description='A pipenv plugin for tox',
        long_description=long_description,
        version=_version,
        url='https://github.com/tonybaloney/tox-pipenv',
        license='MIT',
        platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
        author='Anthony Shaw',
        classifiers=['Development Status :: 4 - Beta',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: MacOS :: MacOS X',
                     'Topic :: Software Development :: Testing',
                     'Topic :: Software Development :: Libraries',
                     'Topic :: Utilities',
                     'Programming Language :: Python',
                     ],
        packages=['tox_pipenv', ],
        py_modules=['tox_pipenv'],
        install_requires=[requirements],
        entry_points={'tox': ['pipenv = tox_pipenv.plugin']},
    )

if __name__ == '__main__':
    main()
