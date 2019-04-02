from setuptools import setup

setup(
    name='featuretools_tsfresh_primitives',
    version='0.0.0',
    author='Feature Labs, Inc.',
    author_email='support@featurelabs.com',
    install_requires=['tsfresh>=0.11.2'],
    packages=['featuretools_tsfresh_primitives'],
    entry_points={
        'featuretools_primitives': [
            'tsfresh = featuretools_tsfresh_primitives',
        ],
    },
)
