#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

# Define the name for your package, this will be used when calling `loadPlugin`.
# Note, for packages containing only a single module defining objects to export,
# you should name it something based off this name of the project to avoid
# import collisions with other packages, here we call it `psychopy_emotiv`.
name = "psychopy-emotiv"

# Define entry points. PsychoPy's plugin framework scans packages and looks for
# entry points advertised in the package metadata which pertains to PsychoPy.
# Entry points are a dictionary, where keys are fully qualified names to
# modules and unbound classes which you want to add/modify attributes. Values
# can be single strings, or lists of strings specifying what attributes of those
# PsychoPy objects are to reference objects defined in the plugin module.
entry_points = {
    'psychopy.hardware': ['emotiv = psychopy_emotiv:emotiv'],
    'psychopy.experiment.components': [
        'emotiv_marking = psychopy_emotiv:emotiv_marking',
        'emotiv_record = psychopy_emotiv:emotiv_record'
    ]}

# Run the setup function.
setup(
    name=name,  # set the name
    version="0.1",  # put your plugin version here
    packages=['psychopy_emotiv',
              'psychopy_emotiv.emotiv_marking',
              'psychopy_emotiv.emotiv_record'],
    package_data={"": ["*.txt", "*.md", "*.png"]},
    author="Matthew D. Cutone",
    author_email="mcutone@opensciencetools.org",
    description="PsychoPy plugin for adding support for Emotiv devices.",
    url="https://github.com/mdcutone/psychopy-demo-plugin",
    classifiers=[
        "License :: OSI Approved :: GPL3",
        'Programming Language :: Python :: 3'],
    keywords="psychopy emotiv eeg eyetracker",
    zip_safe=False,
    entry_points=entry_points  # set our entry points in the package metadata
)