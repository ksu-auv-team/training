# 2018-2019 AUV Software Plan

## Goals:

* Refactor existing code so it's easier to work with
* Add to existing code so we have more working for next year (especially easyish tasks)
* Document everything so it's easier to get new people started
* Recruit more programmers

## Competition obstacles:
### Doneish
* Start gate

### Easyish
* Dice/buoys
* Path

### Medium
* Surfacing in area
* Dropper/roulette wheel

### Hard
* Torpedoes
* Pickup/drop off
    * Funnels
    * Gold chips

## Documentation
* Ideally want a guide/tutorial we can give new people to get them started with minimal help. Probably won't get that, so go for a guide we can give new people to get them started. We'll probably need one for complete beginners and one for programmers.
* Explain what every module does and how it fits together.
* Explain how each module works (i.e. comment and document each)
* Explain how we use third-party libraries like ROS and the NCSDK, ideally with both links to their documentation and our own documentation of how we use it.
* Explain other software we use, like Ubuntu.
* Find ways to get nonprogrammers started and to get non-Python programmers switched over.

## Things to be explained
* Ubuntu
* Terminal
* Git/GitHub
* Python
* ROS
    * General idea
    * Publishers and subscribers
    * Messages and message types
    * Roscore, is_shutdown, other utility functions
    * Useful commands (like roscd, rostopic)
* Catkin    
* Hardware
    * Movidius
    * Pixhawk
    * Cameras
* NCSDK
* Neural networks
* MavROS
    * General idea and specific messages/features we use
* execute.py
* run-nnet.py
* movement_package
* OpenCV
* RoboSub
* NumPy (briefly)
* Caffe
* Architecture


## Recruitment
* Recruit at events like competition team test drive
* Work with PR
* Recruit from CS majors specifically
    * Set up table in atrium for a day or two, with software people there

## Assorted things:
* Find something nonprogrammers can work on
    * Labeling data
    * Can they help test somehow? Can we teach them to train the network?

## Potential projects:
* Refactor:
    * execute.py
* Write more convenience scripts, especially for training and starting the sub tethered
* Find a better way to log data from runs
* Find a way to connect to the sub wirelessly (or otherwise without opening it)
* Update execute.py to use depth sensor throughout
* Figure out why pixhawk depth_hold won't work
* Test stereo camera
* Retrain SSD properly for start gate
    * Figure out if we need to label gate parts separately and rewrite if so
* Fix qualification code
* Write classifier for die faces or get SSD working with them if possible, then write dice code
* Train SSD for path marker (or other detection) & write path following code
* Start work on claw/dropper/torpedoes
    * First figure out what we'll have
    * Then be ready to start working with it

## Hardware requirements:
### Needs
* Movidius (preferably two)
* PC for training
* Raspberry Pi
* Mouse/keyboard/monitor
* Sub
* Two cameras
### Wants
* Better bottom camera?
* Stereo camera setup
* Claw cam? Some way to track it.
* Sub hardware more powerful than a Pi? That's just a bonus.


## Immediate tasks:
* Get network working for Thursday
* Set meeting time
* Write basic guide to overall structure
* Give everyone a project
* Make pool test plans
    * First test is data collection. Want start gate + dice, but will accept buoys in a pinch.
    * Second goal (not test) is updating qualification code
    * Third is depth sensor
    * Next after that is testing dice.
    * After that work on path
    * If we get more than that done this semester I'll be happy and want to start using the claw

## Medium-term tasks:
* Test stereo camera
* Refactor current code
* Retrain network properly