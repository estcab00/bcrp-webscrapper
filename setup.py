import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='bcrp_webscrapper',
    version = '1.0.2',
    author = 'Esteban Cabrera',
    description = 'Time series extraction from the Peruvian Central Bank Database (BCRP Statistics)',
    long_description = long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/estcab00/bcrp-webscrapper',
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ], 
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'numpy',
        'requests',
        'unidecode',
        'selenium',
        'openpyxl',
        'more-itertools',
    ]
)