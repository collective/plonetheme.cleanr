
from setuptools import setup, find_packages

setup(
    name='plonetheme.cleanr',
    version='0.0.1',
    packages=find_packages(),
    namespace_packages=[
        'plonetheme'
    ],
    include_package_data=True,
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone'
    },
    install_requires=[
        'setuptools',
        'plone.app.theming',
    ],

)
