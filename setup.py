from setuptools import setup

import tox_pipenv

with open('README.rst') as readme:
    long_description = readme.read()

with open('HISTORY.rst') as history:
    history_txt = history.read()


_version = tox_pipenv.__version__

requirements = [
    'tox==2.9.1',
    'pipenv==11.0.2',
]


def main():
    setup(
        name='tox-pipenv',
        description='A pipenv plugin for tox',
        long_description=long_description + '\n\n' + history_txt,
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
