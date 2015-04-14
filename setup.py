from setuptools import setup, find_packages

setup(
    name='threecolor',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Flask',
        'Flask-FlatPages',
        'Frozen-Flask',
        'Fabric'
    ],
    entry_points='''
        [console_scripts]
        3color=threecolor.manager:cli
        ''',
)
