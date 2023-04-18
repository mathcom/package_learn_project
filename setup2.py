from setuptools import setup, find_packages

setup(
    name='package-learn',
    version='0.2',
    packages=find_packages(where='src', include=['pklearn*']),
    package_dir={"":'src'},
    package_data={
        'pklearn2':['data/*'],
    },
    install_requires=[
        'numpy',
    ]
)
