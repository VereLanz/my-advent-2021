from setuptools import setup

setup(
    name="my-advent",
    version="0.1",
    packages=["my_advent"],
    author="VereLanz",
    author_email="verelanz@gmail.com",
    description="My Advent of Code 2021",
    install_requires=[
        "advent-of-code-data",
        "numpy",
        "scipy",
        "pathfinding",
    ],
    tests_require=[
        "pytest",
    ],
)
