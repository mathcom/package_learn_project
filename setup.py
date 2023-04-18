from setuptools import setup, find_packages

setup(
    name='package-learn',
    version='0.1',
    packages=find_packages(where='src', exclude=['pklearn2*']),
    package_dir={"":'src'},
    package_data={
        'pklearn':['data/*'],
        'pklearn2':['data/*'],
    },
    install_requires=[
        'numpy',
    ]
)
