---
jupytext:
  formats: md:myst
  text_representation:
    extension: .myst
    format_name: myst
    format_version: 1.1
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Before we begin

_Introduction to Computer Science_ is about
computational thinking.  The principles and techniques
you will learn are not limited to a single programming
language, let alone a particular computer or operating system.
But we have to start somewhere, and that _somewhere_
requires us to choose a programming language and to
install it and supporting tools on the computer that
you will use to work projects. 

## Why Python

In this course we will use Python version 3, and 
specifically Python version 3.10 or higher. 
Python is widely used in data science and scientific
computing, in cartography, in web development,
in machine learning, and in many other domains, but
that is not why we have chosen it. We have chosen Python 3 because 
we believe it is a good language for _learning to program_.   Python 
3 is 

- Consistent.  There are few "special cases" to remember in Python,
  which makes it easier to remember how things work and to build on 
  what you know. 
- Concise.  Python does not require a lot of boilerplate, which 
  makes it easier to read example code. 
- Well-provisioned.  Although there are many extras that you _could_ 
  add, a standard and straightforward installation of Python is 
  enough to build many interesting projects.

That is not to say that Python is a perfect language.  It is 
certainly not the only programming language you will ever want or 
need to learn.   But among the programming langauges available to us 
today, we believe it is an excellent starting point. 

## Install Python 3 on Your Computer

Python 3 runs well on a wide variety of computers.  You will 
need a laptop or desktop computer; tablets and phones will not be a 
good environment for learning to program in Python.  The precise 
steps for installing Python 3, as well as the precise commands for 
starting Python programming tools, necessarily varies depending on 
whether you are using Linux, MacOS, or Windows.   We will cover 
the basics first in a generic manner, then provide some detailed 
notes for the most common platforms. 

### Download and Install

Start by visiting `python.org` with your web browser.

![Visit Python.org](img/python-org.png)

Select `Downloads` and choose the installer or archive for your
computer.  Typically you will want the download labeled as "Latest 
Python 3 Release" for MacOS or Windows.  If you are a Linux user, 
select "Source code".  Then follow directions for your particular 
platform. 

### MacOS Install

The MacOS installer will work like other MacOS application 
installers. You should not have to do anything extra. 

### Windows 10 Install

TBD

### Linux Install

You _may_ find it easier to install using `apt-get` or a similar 
package installer for the version of Linux that you use.  You can 
find example instructions in 
[The Hitchhikers Guide to Linux](https://docs.python-guide.org/starting/install3/linux/).   
Alternatively, you can download a "tarball" archive of the sources from
Python.org.   As a Linux user, you are probably familiar with these 
steps, which are similar to installation of many other tools in Linux. 

## Execute Python statements and programs

### Executing Python commands

Python commands (_statements_) may be executed immediately in a 
_console_, or stored in a program file (often called a _script_) for 
execution later.  In this course we will use _IDLE_ both to execute
statements directly and to edit and execute program files. (Later we 
will explore additional ways to edit and execute Python programs.)

Once you have 
[installed Python 3 on your computer](./01-0-Ready.md), you 
should be able to start _IDLE_ from the command line.  It should look 
something like this: 

![IDLE shell at start-up](img/IDLE.png)

The `>>>` symbol is a _prompt_ indicating that
the Python shell, or console, is ready to
receive a statement and execute it. 

Try this by typing `print("Hello!")` on the
line with the prompt. 

```{code-cell} python3
print("Hello")
```

What happens if you change to "print" to "Print" or "PRINT"?  Does 
this tell you something about the rules of the Python language? 

Whenever you are curious about some rule or characteristic of the 
Python programming language, you should design and carry out 
micro-experiments to build understanding.  As in a full-blown 
scientific experiment, you will get the most from a micro-experiment 
if you have a specific prediction based on a hypothesis about the 
language.  For example, your hypothesis might be "Python is 
case-insensitive; 'Print' and 'print' should do the same thing."  
Your prediction would then be that `Print("Hello")` causes "Hello" 
to be printed.  Your experiment would _disconfirm_ this prediction, 
telling you that the hypothesis was incorrect:  Python is case 
sensitive.  Performing little experiments as you work is much faster 
than correcting a lot of code that was built on wrong assumptions! 

Of course there are other ways you can learn details of Python 
language rules. You should already have bookmarked the 
[Python library documentation](https://docs.python.org/3/library/index.html)
in your browser.  (If you haven't, do it now!)  