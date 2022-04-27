from setuptools import setup

setup(
    name="idwall",
    packages=["app"],
    include_package_data=True,
    install_requires=[
        "flask",
    ],
)
