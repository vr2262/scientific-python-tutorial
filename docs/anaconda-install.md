Installing Anaconda
===================

This tutorial assumes you will be using a Linux distribution, but includes Mac and Windows instructions as well.

**Table of Contents**

- [Installing Anaconda](#)
	- [Download](#)
	- [Install](#)
		- [Linux](#)
		- [Mac](#)
		- [Windows](#)
	- [Check your installation](#)
	- [Create a virtual environment](#)

## Download

Go to http://continuum.io/downloads and download the Python 2.7 installer for your operating system.

## Install

See the official guide at http://docs.continuum.io/anaconda/install.html

### Linux

Open a terminal window, navigate to the directory where you have downloaded the installer, and execute this command, replacing 2.x.x with the version number of the installer file:

`$ bash Anaconda-2.x.x-Linux-x86_64.sh`

The installer will ask you to accept the license agreement and specify an install location (the default is `~/anaconda`). The installer will then download the various packages included in Anaconda. Finally, it will ask you whether you want to add the Anaconda directory to the `PATH` in your `.bashrc` file. The default is no, but if you use `bash` you should say yes, then open a new terminal window.

### Mac

Double click the Anaconda installer. A user interface will pop up to guide you through the installation.

**Notes from the install guide:**

Due to a bug in the Mac OS X installer software, you may see a screen that says “You cannot install Anaconda in this location. The Anaconda installer does not allow its software to be installed here.” To fix this, just click the “Install for me only” button with the house icon, and the installation will work again.

The installer package will automatically modify your `bash` profile to add anaconda to your `PATH`. If you do not want it to do this, you can choose “Customize” at the “Installation Type” phase, then deselect the “Modify PATH” option.

### Windows

Double click the Anaconda installer. A user interface will pop up to guide you through the installation.

## Check your installation

If you installed Anaconda successfully, then in a new terminal window you should have access to the `conda` command. If you get a `command not found` error, then the Anaconda directory is probably not in your `PATH`.

## Create a virtual environment

See the official guide at http://conda.pydata.org/docs/faq.html#env-creating

Run this command to create a virtual environment with the name "my_environment":

`$ conda create -n my_environment python`

The `conda` program will list the actions it will take and whether you would like it to proceed. Hit enter to say yes.

At this point you should install `pip`, the standard Python package installer, in your `conda` environment. This way you can install packages into the environment that aren't avaialabe in the Anaconda repositories.

`$ conda install -n my_environment pip`

You can install various scientific packages this way, such as `numpy`, `scipy`, and `pandas`.

Now you can enter your environment with this command:

`$ source activate my_environment`

Your command line prompt should look something like this:

`(my_environment)user_name@machine_name:~$`

In the environment, you control exactly which packages (and which versions) are available, making it easier to replicate or share development environments between machines or people.

You should install IPython in your environment with this command:

`(my_environment)user_name@machine_name:~$ pip install "ipython[all]"`

To leave the environment, use this command:

`$ source deactivate`
