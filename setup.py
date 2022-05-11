from setuptools import setup, find_packages

name='PointConv'
version='1.0.0'

setup(
    name=name,
    packages=find_packages(),
    version=version,
    namespace_packages=['PointConv'],
    install_requires=[
        'numpy',
        'sklearn',
        'pandas',
        'torch>=1.10.2',
        'torchvision>=0.11.3',
        'torchaudio>=0.10.2'
    ],
    python_requires='>=3.9'
)
