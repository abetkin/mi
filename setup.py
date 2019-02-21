from setuptools import setup

setup(
    name='mi',
    packages=['mi'],
    install_requires=[
        'docopt',
    ],
    entry_points="""
    [console_scripts]
    mi=mi.main:entry_point
    """,
)
