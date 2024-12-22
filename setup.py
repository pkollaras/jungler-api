import sys

from setuptools import setup

__version__ = "0.163.1"

setup(
    name="jungler-api",
    version=__version__,
    description="JunglerShop Setup",
    author="Panagiotis Kollaras & George Hatzopoulos",
    author_email="panagiotiskollaras@gmail.com"
)

try:
    from semantic_release import setup_hook

    setup_hook(sys.argv)
except ImportError:
    pass
