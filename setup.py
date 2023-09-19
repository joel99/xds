from setuptools import setup, find_packages

setup(
    name='xds_python',
    version='0.0.1',

    url='https://github.com/limblab/xds',
    author='Miller Lab',
    author_email='lm@northwestern.edu',

    packages=find_packages(exclude=['xds_matlab']),
    py_modules=['xds_python'],

    install_requires=[
        'numpy',
	'scipy',
	'h5py',
    ],
)
