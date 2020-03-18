# python_file_hunting
An investigation into different methods of searching for a file with python.

## Why am I looking into this?
For my project [onion_file_search](https://github.com/jimbob88/onion_file_search) I wanted to be able to outperform [Catfish](https://launchpad.net/catfish-search), which is the default included piece of software for finding files under [Xubuntu](https://xubuntu.org/), due to the fact the default file manager, [Thunar](https://en.wikipedia.org/wiki/Thunar), had only limited search functionality (only being able to search for a sub-string with a max-depth of 1).   

## A quick note on onion_file_search
The onion_file_search project is now deprecated due to the fact it used an outdated function `populate_tree`, that at the time of original development I never thought to fix... Simply put, when I originally copy & pasted that function from [dirbrowser.py](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=2ahUKEwjK5duW3JroAhXoUBUIHR--AaIQFjAAegQIBhAB&url=https%3A%2F%2Fsvn.python.org%2Fprojects%2Fpython%2Ftrunk%2FDemo%2Ftkinter%2Fttk%2Fdirbrowser.py&usg=AOvVaw05IXaGmqBFfoZJ17jX1s4d) I edited to add all the features I wanted; however, I forgot to fix the crucial issue found within the basis of `populate_tree`, which is the fact it uses `os.listdir` and the whole point of my code was to attempt to implement a brand new search function into Python.

## The issues with Catfish
The idea of this is not to diss catfish because honestly it looks amazing and it is very functional for the average user, but I am not an average user, due to the sheer size of my directory that I often need to search through...  My development folder has `303,692 items, totalling 5.4 GB`. As I needed to search for specific strings often, I wanted to build my own custom tool to do that and to be honest I could have simply used the terminal and stuck with that; however, I wanted a project so I chose to build it with python. ;)

#### Why catfish didn't work for my use case
Catfish uses the [`mlocate` program](https://wiki.archlinux.org/index.php/Mlocate), which works by having a massive database of all the accessible files to the current user. This program "contains an updatedb.timer unit, which invokes a database update each day"; however, as my programming database is constantly changing and updating I would personally want something that gets a live update from the sytstem, instead of having to call `updatedb` every time I want to search for a file (which, on my system, takes `real	0m9.126s`).

# The Operating Systems I have tested

## [Linux (tested on Ubuntu 19.04)](https://github.com/jimbob88/python_file_hunting/tree/master/linux)
## [Windows (tested on Windows 10)](https://github.com/jimbob88/python_file_hunting/tree/master/windows)
