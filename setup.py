from setuptools import find_packages, setup

setup(
    name="ml_package",
    version="0.1.0",
    packages=find_packages(where="ml_project/src"),
    package_dir={"": "ml_project/src"},
    install_requires=["pandas", "numpy", "scikit-learn", "argparse", "pytest"],
)
