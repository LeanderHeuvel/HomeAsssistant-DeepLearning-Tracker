# HomeAsssistant-DeepLearning-Tracker
This repository contains the code the for the Home Assistant Deep Learning Tracker

The hass_dl_tracker packages allows to easily upload your deeplearning metrics through home assistant while training.

## Installation

`
pip install git+https://github.com/LeanderHeuvel/HomeAsssistant-DeepLearning-Tracker.git#egg=hass_dl_tracker
`

## Usage

`

##upload any metrics by adding them to the constructer of update_state(). By default the loss will be used to update the 'state' attribute of the entity.
upload.update_state(loss = i*0.45, epoch = i, accuracy_val = 74)

`