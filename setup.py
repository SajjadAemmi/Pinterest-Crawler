from pathlib import Path
from setuptools import setup, find_packages


def post_install():
    """ Implement post installation routine """
    with open('./requirements.txt') as f:
        install_requires = f.read().splitlines()

    return install_requires


def pre_install():
    """ Implement pre installation routine """
    # read the contents of your README file
    global long_description
    this_directory = Path(__file__).parent
    long_description = (this_directory / "README.md").read_text()


pre_install()


setup(
    name='pynterest',
    version='0.1.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["pynterest"],
    setup_requires=[],
    url='https://github.com/SajjadAemmi/Pinterest-Crawler',
    license='',
    author='Sajjad Aemmi',
    author_email='sajjadaemmi@gmail.com',
    description='Pinterest Crawler: Download as many images as you want about the searched words',
    include_package_data=True,
    install_requires=post_install(),
    entry_points={
        "console_scripts": ["pynterest=pynterest.plantsai:main"],
    },
)
