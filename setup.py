"""Create a Python distribution package setup.py."""
from setuptools import setup


extra_packages = {
    'testing': ['pytest-cov', 'tox']
}


setup(
    name="Decision Tree",
    description="Contains a Python implementation of a decision tree using the ID3 algorithm",
    version=0.1,
    author="Kurt Maurer",
    author_email="kurtrm@gmail.com",
    license="MIT",
    package_dir={'': 'src'},
    install_requires=["ipython", "pytest"],
    extras_require=extra_packages,
    entry_points={
        'console_scripts': [
        ]
    }
)
