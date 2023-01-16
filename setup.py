from setuptools import setup

from src.deeplearningtracker_leandervandenheuvel.deeplearningtracker import __version__

setup(
    name='hass_dl_tracker',
    version=__version__,

    url='https://github.com/LeanderHeuvel/HomeAsssistant-DeepLearning-Tracker',
    author='Leander van den Heuvel',
    author_email='leander.vandenheuvel@gmail.com',

    py_modules=['hass_dl_tracker'],
    install_requires=[
        'requests',
    ],
)
