import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='lanenet',
    version='1.0.0',
    author='MaybeShewill-CV',
    description='Implemention of lanenet model for real time lane detection using deep neural network model',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MaybeShewill-CV/lanenet-lane-detection',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ),
)
