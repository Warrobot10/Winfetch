from setuptools import setup

setup(
    name='winfetch-py',
    version='1.0.5',
    py_modules=['winfetch'],
    install_requires=[
        'termcolor',
        'WMI',
        'py-cpuinfo'
    ],
    entry_points={
        'console_scripts': [
            'winfetch=winfetch:main'
        ]
    },
)
