from setuptools import find_packages, setup

with open('README.md') as source:
    long_description=source.read()

setup(
    name='Clan',
    version='1.0.0',
    author='Michail Khan',
    description='Blood is thicker than water.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)