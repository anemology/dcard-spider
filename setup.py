import codecs
from setuptools import setup

def readme():
    with codecs.open('README.rst', 'r', 'utf-8') as f:
        return f.read()

setup(
    name='dcard-spider',
    version='0.1.0',
    url='http://github.coom/leVirve/dcard-spider',
    description='A spider for Dcard through its newest API.',
    long_description=readme(),
    author='Salas leVirve',
    author_email='gae.m.project@gmail.com',
    license='MIT',
    platforms='any',
    packages=['dcard'],
    zip_safe=False,
    scripts=['spider.py'],
    keywords='Dcard crawler spider',
    entry_points = {
        'console_scripts': ['dcard=dcard.cli:main'],
    },
    install_requires=[
        'six',
        'requests',
        'requests-futures',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Customer Service',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)