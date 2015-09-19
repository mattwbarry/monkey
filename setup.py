APP_NAME = 'monkey'
VERSION = '0.0.0'

import pip
from setuptools import setup, find_packages

install_reqs = pip.req.parse_requirements('requirements.txt',
    session=pip.download.PipSession())
required = [str(ir.req) for ir in install_reqs]

settings = {
    'name': APP_NAME,
    'version': VERSION,
    'author': 'mattwbarry',
    'author_email': 'mattwbarry@gmail.com',
    'packages': find_packages(),
    'include_package_data': True,
    'url': 'https://github.com/mattwbarry/monkey.git',
    'license': 'None',
    'description': 'An implementation of the Infinite Monkey Theorem',
    'long_description': open('README.md').read(),
    'install_requires': required,
    'classifiers': [
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    'entry_points': {
        'console_scripts': [
            'monkey = monkey.cli:cli'
        ],
    }
}
setup(**settings)