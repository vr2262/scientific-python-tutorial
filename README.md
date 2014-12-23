**Table of Contents**

- [Scientific Python Tutorial](#scientific-python-tutorial)
	- [Prerequisites](#prerequisites)
		- [A Python environment](#a-python-environment)
		- [A text editor](#a-text-editor)
		- [Some way to share your code](#some-way-to-share-your-code)
	- [Getting Started](#getting-started)

Scientific Python Tutorial
==========================

An introduction to getting Python up and running, with an emphasis on sharable scientific code.

## Prerequisites

### A Python environment

Most people manage an environment using [pip](http://en.wikipedia.org/wiki/Pip_%28package_manager%29) &mdash; the Python package installer &mdash; and [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) &mdash; a tool that creates "virtual environments" to keep project-specific Python environments encapsulated.
  
For the purposes of this tutorial, we'll use [Anaconda](https://store.continuum.io/cshop/anaconda/), which is a distribution of Python that comes bundled with a number of popular scientific packages.
  
[Click here](docs/anaconda-install.md) for instructions on setting up Anaconda.

### A text editor

One of the nice things about Python is that it allows you to write short, expressive code. As such, some people feel most productive writing Python programs using a command line text editor such as [Vim](http://en.wikipedia.org/wiki/Vim_%28text_editor%29) or [Emacs](http://en.wikipedia.org/wiki/Emacs). Or, for those preferring a more typical interface, editors like [gedit](http://en.wikipedia.org/wiki/Gedit) or [Notepad++](http://en.wikipedia.org/wiki/Notepad%2B%2B) have plugins for Python syntax highlighting.
 
**Note for Windows users:** Do not use the built-in Notepad program to write or edit code.
 
There are also a number of options for users that prefer an integrated desktop environment. The most popular IDE for Python is [PyCharm](https://www.jetbrains.com/pycharm/), which has a free community edition. For users familiar with [Eclipse](http://www.eclipse.org/), [PyDev](http://pydev.org/) is available as an Eclipse plugin or bundled with [LiClipse](http://www.liclipse.com/) and [Aptana Studio](http://www.aptana.com/). For users familiar with MATLAB, [Spyder](http://en.wikipedia.org/wiki/Spyder_%28software%29), which comes bundled with Anaconda, provides a similar user interface and access to scientific functions.
 
This tutorial will make use of the [IPython Notebook](http://ipython.org/notebook.html), a browser-based Mathematica-like environment that has become the de facto standard for sharable, interactive, and scientific Python code.
 
[Click here](docs/ipython-notebook.md) for instructions on using the IPython Notebook.
 
### Some way to share your code

These days most people (myself incldued) prefer to host open source software and information on GitHub. GitHub provides you with a remote [Git](http://en.wikipedia.org/wiki/Git_%28software%29) repository and a web interface that makes it easy to distribute and manage your code.
  
In addition, [nbviewer](http://nbviewer.ipython.org) provides a convenient way to share IPython Notebooks online.
  
The instructions and IPython Notebooks in this tutorial are available at https://github.com/vr2262/scientific-python-tutorial and http://nbviewer.ipython.org/github/vr2262/scientific-python-tutorial/tree/master/

## Getting Started

### Scripts and Modules

#### Hello, World!

An executable Python file is simply a text file with the extension `.py` that contains valid Python code. As such, a basic "hello world" program could look like this ([`hello.py`](hello.py)):

```
print 'Hello, World!'
```

You can run this program with the command...

`$ python hello.py`

which will print to `stdout`:

`Hello, World!`

#### Best Practices

The official Python style guide, known as [PEP 8](https://www.python.org/dev/peps/pep-0008/), contains many suggestions about coding and organizational conventions for Python code. Here are some best practices for a Python script ([`hello_improved.py`](hello_improved.py)):

- The first line should have a [shebang](http://en.wikipedia.org/wiki/Shebang_%28Unix%29) like so:

  `#!/usr/bin/env python`

- The second line should declare the character encoding of the file. You should use UTF-8:

  `# -*- coding: UTF-8 -*-`

- Define units of functionality inside of functions:

  ```
  def main():
      print 'Hello, World!'
  ```

- Any code that should run when the Python file is executed should be inside a special conditional like so:

  ```
  if __name__ == '__main__':
    main()
  ```

You can now run the script `hello_improved.py` as before...

`$ python hello_improved.py`

or you can make the file executable...

`$ chmod +x hello_improved.py`

and run it as a shell script:

`$ ./hello_improved.py`

### Functions
