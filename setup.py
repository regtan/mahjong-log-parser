from setuptools import setup, find_packages

setup(
    name='mahjong-log-parser',
    version='0.1.0',
    author='regtan',
    author_email='regtan1210@gmail.com',
    description='A parser for Denno-Mahjong log format to class instances.',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)