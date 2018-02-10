# fluotracker

The purpose of this repository is to extract and analyse tracks of nanoparticles from
fluorescent microscopy movies of neurons.

TODO: add background info (lab, links to publications, etc.)

# Setup

## Python environment

You should first make sure your Python environment is setup properly. The prefered method
is to use [pyenv](https://github.com/pyenv/pyenv) and
[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).
However if your are confident in your environment setup you should be fine.

The code is intended to be used in **Python 3**.

## Downloading the repository

```
$ git clone https://github.com/BenjaminHabert/fluotracker.git
$ cd fluotracker
$ pip install -r requirements.txt
```

You now need to add this folder to your `PYTHONPATH` environment variable. For instance on mac-os
I add the following lines to the `~/.bash_profile` file:

```
# the first line is a convenience to cd to this folder easily
alias fluo="cd /Users/benjaminhabert/Documents/FluotrackerProject/fluotracker/"
# this makes sure that Python knows to look in this directory to find modules and functions of the project
# make sure that the line ends with :$PYTHONPATH if you do not want to override existing variable
export PYTHONPATH=/Users/benjaminhabert/Documents/FluotrackerProject/fluotracker/:$PYTHONPATH
```

In order to test that everything is setup:

```
# open jupyter notebook
$ jupyter notebook
# open the file notebooks/2018-02-10_refactoring_code_as_functions.ipynb
# run the notebook. If everything runs smoothly you should be all set!
```

## Editor setup

Use what you want as an editor. We suggest using [atom](https://atom.io/) with the following plugins:

- linter-pep8
- python-indent
- kite plugin (requires installation of [kite](http://help.kite.com/article/53-quickstart)).
This provides code completion! You can configure kite itself to whitelist the repository
(which allows code inspection not only for basic python packages but also modules degined here)
- minimap

Make sure to configure your editor to use **4-spaces indentation** and not tabs!

# Conventions

## Data Management

All data files are stored in the `data/` folder. These files **should not me comitted** to the
repository. The module `fluotracker.io.files` provides convenient functions to load and save
files from the folder.

## Using git

TODO
