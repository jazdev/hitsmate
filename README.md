hitsmate v0.2
========

Developed by [Jasdev Singh](http://singh.am)

Hitsmate: A simple web traffic estimator
======================

This document gives a quick overview on how to use this program.

###1. Installation

Download the whole project source from GitHub. [Do this by clicking here](https://github.com/jazdev/hitsmate/archive/master.zip). Once downloaded, extract the source to a directory of your choice. 

The project has the following directory structure:

```
hitsmate/
├── docs
│   └── screenshots/
├── hitsmate
│   ├── graphs/
│   ├── hitsmate.py
│   ├── model.cached
│   ├── model.cfg
│   ├── sample_data/
│   └── test/
├── LICENSE
├── README.md
└── requirements.txt
```

* The ```hitsmate/``` directory contains the main program files.

* The ```graphs/``` directory contains the generated graphs.

* The ```sample_data/``` directory contains sample logs that the program can use.

* ```screenshots/``` contains runtime screenshots of the program.

* The ```hitsmate.py``` file is the main executable program code. We'll run this file to use the program.

* The ```LICENSE``` contains important copyright references and redistribution terms.

To install Tkinter on Ubuntu, use the following command:
```
		$ sudo apt-get install python python-tk idle python-pmw python-imaging
```		

In particular, this program requires you to have the following libraries:
* Tkinter
* ttk
* tkintertable

###2. Running the Program

The program can be run in the following ways:

* Command Line method:
	
	```
	$ cd hitsmate
	$ python hitsmate.py
	```

* Using IDLE:

	Open the hitsmate.py file in IDLE IDE and press F5 to run the program


###3. Program Walkthrough

The correct way to use this program is as follows:

####a. Main Window

This is the main screen of the program. It has all the options that the user can select by pressing the appropriate button. Usually, you'll want to select the ```Generate Random Web Logs``` or the ```Select custom log file``` button if this is the first time you are running the program.

<img style="float: right" src="https://github.com/jazdev/hitsmate/blob/master/docs/screenshots/1.png" alt="Hitsmate: Main window" />

####b. Generate Random Web Logs Window

This window shows the randomly generated web log data. It lists the cumulative hour number and the hits received in that hour.

<img style="float: right" src="https://github.com/jazdev/hitsmate/blob/master/docs/screenshots/2.png" alt="Hitsmate: Generate Random Web Logs Window" />

