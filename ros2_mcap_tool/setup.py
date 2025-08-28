from setuptools import setup, find_packages

setup(
    name='ros2_mcap_tool',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pyqt5',
        'plotly',
        'polars',
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'ros2-mcap-tool=main:main',
        ],
    },
)
