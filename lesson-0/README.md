### Lesson 0 - The OS, Terminal Basics, and Git

Writing code is only one of the many tasks computer programers must become proficient in to be able to do anything useful. There is a whole suite of technologies you must learn, depending on how you are planning to exercise your programming knowledge.

We'll begin this course by understanding how we interact with our computer through a terminal, and how to download new technologies (software).

### Contents

* [0.1 - The Operating System](#01---the-operating-system)
* [0.2 - The Terminal & Unix Shell Basics](#03---the-terminal-and-unix-shell-basics)
* [0.3 - The OS Package Manager](#03---the-os-package-manager)
* [0.4 - Git and Version Control](#04---git-and-version-control)

## 0.1 - The Operating System

The "OS" is system software that manages computer hardware, software resources, and provides common services for computer programs.

Such services include input/output from devices (keyboard, mouse...), low level access to the network (i.e. Internet) through something called sockets, the ability to start and stop programs, and many,  **MANY**... more.

Basically, the OS is a service that is always running on your computer, and it provides computer users and programmers with enough abstraction such that they don't need to know anything about how their computer works in order to use it!

<img src="../.media/osabstraction.png" height="300">

> Computer Abstraction Layers - [source](https://en.wikipedia.org/wiki/Operating_system)

Take a look at the image above. If you have no experience with programming, so far you have only interacted with your computer/machine as a user. Throughout this course, you will learn to write application software, such that you can tell your computer what you want it to do.

## 0.2 - The Terminal and Unix Shell Basics

A "terminal" is an electronic device that is used for entering data into, and displaying or printing data from, a computing system.

<img src="../.media/terminal.png" height="300">

> DEC VT100 Terminal - [source](https://en.wikipedia.org/wiki/Computer_terminal)

Modern operating systems (MacOS X, Windows, Ubuntu...) include a terminal emulator (simulator) program, called a **"shell"**. Physical hardware terminals as shown in the image above are no longer used in practice.

Throughout this course we will learn to navigate the terminal and communicate with our computer system so as to read, write, or execute computer programs.

##### Open your terminal and try the following commands:

* `pwd`: Print Working Directory

This command will tell you where in your file system you are currently at (e.g. /Users/You, /Desktop, ...).

* `ls`: List (Files/Directories)

This command will list the files in your current working directory

* `cd`: Change Directory

This command will change your working directory to the directory given as the first argument. Example: `cd directory_name`

* `mkdir`: Create Directory

This command will create a directory at the location given with the name given. Example `mkdir directory_name`

* `touch`: Create File

This command will create a directory at the location given with the name given. Example `mkdir directory_name`

## 0.3 - The OS Package Manager

UNIX-based Operating Systems (e.g. Linux, MacOS X... - not windows) typically come with a program called package manager.

The package manager allows us to download software and libraries to our computers.

For Linux the package manager is called "apk" or "apt" (depending on the distribution of Linux).

For **MacOS**, there is no default package manager, but you may download a package manager made for MacOS, [Homebrew](https://brew.sh/), by pasting the following in the terminal:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
Now you may invoke the homebrew package manger from the terminal by using the 'brew' command as follows:

```
$ brew install PACKAGE_NAME
```

To update downloaded packages:

```
$ brew upgrade PACKAGE_NAME
```

##### Installing Python:

We will install the latest version of python to our machines with the command:

```
$ brew install python
```

##### Installing Git:

[Git](https://git-scm.com/) is an Open-Source version control system.
 
We will need to install the git program to our machines in order to be able to access (this) course material from your terminal:

```
$ brew install git
```

## 0.4 - Git and Version Control

Clone this git repository:

```
$ git clone https://github.com/adrianosela/python-101
```

Pull the most recent changes (from inside the repository directory):

```
$ git pull
```

This is all you need to know at this point - we will come back to git commands as needed.
