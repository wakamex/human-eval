import os

import pkg_resources
from setuptools import setup, find_packages


setup(
    name="human-eval",
    version="1.0.3",
    description="",
    author="OpenAI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": [
            "evaluate_functional_correctness = human_eval.evaluate_functional_correctness:main",
        ]
    }
)
