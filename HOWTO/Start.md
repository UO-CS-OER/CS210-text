# Installing the tools you need

CS210-text (or a forked version under 
another title) is built with Jupyter Book. 
You need to create a Python virtual environment
and some supporting software to build
the book from sources. 

These instructions were tested on a MacOS
12.4 (Monterrey) system.  There will be some
minor differences if you use Linux, Windows, 
or a future version of MacOS.  _If you build in a different 
environment, please consider adding notes on differences
to this document._

## Step 1:  Virtual environment

Create a Python virtual environment. 

```commandline
python3 -m venv env
source env/bin/activate
```

Note:  If you are more familiar with Conda environments, you should
be able to accomplish the same thing with miniconda.  We document the
virtual environment (venv) approach because it is what we know.  _If
you successfully build the book with Conda, please add suitable
instructions for others._

If you use PyCharm or a similar IDE, you may need to alter the 
project configuration to use this virtual environment.  In PyCharm on
MacOS, bring up the Preferences menu, choose Project, and choose 
Project Interpreter.  Choose "new" and set to "existing environment",
where you should find the interpreter linked in your virtual 
environment.  You may need to close and reopen your project to make
this setting effective.  After the project configuration has been made,
the prompt in the Terminal window should always begin with `(env)`,
and the Python Console window should display the correct paths.  For
example, on the author's system the PyCharm Python Console window
shows: 

```commandline
/Users/michal/Dropbox/22F-210/Book/CS210-text/env/bin/python "/Users/michal/Library/Application Support/JetBrains/Toolbox/apps/PyCharm-P/ch-0/221.6008.17/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevconsole.py" --mode=client --port=53807
```

## Step 2:  Install packages

The jupyter-book and ghp-import packages can be installed into the
virtual environment using pip. The file `requirements.txt` has
references to these packages.  For Python version 3.10, it should 
work "out of the box" like this: 

```commandline
pip install -r requirements.txt
```

## Step 3:  Test the build

You should be able to build the derived HTML version of the book from
the markdown sources with this command: 

```commandline
jupyter-book build Intro_to_CS
```

You can abbreviate "jupyter-book" to "jb". 

If it works without errors, the end of the output should look 
something like this: 

```commandline
Finished generating HTML for book.
Your book's HTML pages are here:
    Intro_to_CS/_build/html/
You can look at your book by opening this file in a browser:
    Intro_to_CS/_build/html/index.html
Or paste this line directly into your browser bar:
    file:///Users/michal/Dropbox/22F-210/Book/CS210-text/Intro_to_CS/_build/html/index.html        
```

