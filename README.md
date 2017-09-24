# TomTom Runner Music importer

# Why this tool ?
This tool can be used to import Music on TomTom Runner devices. Unhopefully, TomTom does not provide an official (and maintained) Linux package for its main app in charge of such process, TomTom My Sport. An experimental (and, as a consequence, not maintained) package can be found on TomTom forum, but on my configuration it crashes when I try to import music.

# What does this tool do ?
This tool is designed to have the following features :

* Detect if TomTom Runner device is connected to computer
* Display load
* Allow user to select one or more music track(s)
* Create a new playlist based on loaded tracks
* Import freshly created playlist on device

# Project dependencies
* PyQt4

# How to run it
`python src/ttri_app.py`
