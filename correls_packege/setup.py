from setuptools import setup, find_packages

setup(
    name='rho_mu_correls',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    include_package_data=True,
)
