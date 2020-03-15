# The Original Naive Findings
When I first built onion_file_search, on 2 Mar 2019, I did not do any preliminary testing and naively assumed everything I read online heald up in the real world. This meant I chose to originally use `os.walk` as a baseline of the absolute slowest function, and `os.scandir` being the fastest built-in function. With this so-called "knowledge" in my head, I went out and searched for a faster alternative to `mlocate` and all-hail the amazing linux command `find` <sup>[proof](https://www.tecmint.com/35-practical-examples-of-linux-find-command/)</sup>, with a live search of my whole programming folder it took a mear `real	0m1.109s` (when writing the data directly to a text file). This was much faster than Catfish's `~5.5s`, give or take human reaction speeds ;), so I implemented `find` into onion_file_search, was happy and left the project as it was.

# My approach 1 year later
I chose to revist my project for two reasons:
 * [Somebody](https://github.com/azfirefighter) starred onion_file_search (I had forgoten all about it)
 * I read [this post](https://cython.readthedocs.io/en/latest/src/tutorial/profiling_tutorial.html) in the Cython documentation.
 
 I cannot thank `azfirefighter` enough for his simple star, because it rebirthed an interest into that area of coding, that I had not looked into for a while, and `Cython` had been my point of interest at the time of that notification coming through. So then, what did I read in the Cython Documentation:
>But remember the golden rule of optimization: Never optimize without having profiled. Let me repeat this: Never optimize without having profiled your code. Your thoughts about which part of your code takes too much time are wrong. At least, mine are always wrong.

 And although that seems obvious to me now, that never went through my head when I originally designed onion_file_search, I kind of just built it as I went along and built it so it worked, hence why I did not see some of the glaring issues that are now apparent...
 
 Anyway, with that in mind I built a profiler and decided to analyse the different ways of searching for files, the program which has all these tests in it, can be found [here](https://github.com/jimbob88/python_file_hunting/blob/master/linux/profiling/test_processes.py).
 
 I decided to mess with a couple of different methods, and different approaches to those methods, so here is the rundown of each method:
 * `return_list` as all of these return an iterator they all take very little processing power as they return the values when they are actually needed. To force them to be called, the `return_list` decorator runs the function and returns the `list()` of them.
 * `glob_search` taken from a [stackexchange post](https://codereview.stackexchange.com/a/186705), specifically I  chose the linux version for the linux tests, it is an iterative function that uses the built-in `glob` module
 * `scandir_search` taken from the aforementioned [stackexchange post](https://codereview.stackexchange.com/a/186705) this shows an example of an iterative `scandir` function from the built-in `os` module.
 * `walk_search` is taken from onion_file_search and is a pretty generic implementation that can be found across the internet in varying ways.
 * `find_custom_search` runs the Linux `find` command, and writes the data directly to a text file, this file is then read and each line is yielded.
 * `find_custom_mem_search` is the same as the `find_custom_search` function; however, instead of writing to the disk, it writes to [memory](https://unix.stackexchange.com/a/59305/391053), if the user did not have `/dev/shm` they would have to mount it like [so](https://unix.stackexchange.com/a/59301/391053).
 * `find_custom_mem_qread_search` is intended to try and skip the step of writing to a file and instead read the output directly from `stdout`.
 * `mlocate_custom_search` is the same as `find_custom_search` but with the `mlocate` command over the `find` command.
 * `mlocate_custom_mem_search` is the same as `find_custom_mem_search` but with the `mlocate` command over the `find` command.
 * `mlocate_custom_mem_qread_search` is the same as `find_custom_mem_qread_search` but with the `mlocate` command over the `find` command.
 
 These are then ran through [profiler.py](https://github.com/jimbob88/python_file_hunting/blob/master/linux/profiling/profiler.py) and the stats are spat out into the command line, the profile files are also saved for later.
 
 ## The Results
So then, what did I find after profiling everything?
  If you want to see all of this data visually, in your web browser, these are the different links for each function, it should be noted going [here](https://github.com/jimbob88/python_file_hunting/tree/master/linux/profiling/html), downloading them and viewing it works better & further more running [snakeviz](https://jiffyclub.github.io/snakeviz/) on [these files](https://github.com/jimbob88/python_file_hunting/tree/master/linux/profiling/profiles) will result in an even better experience:
   * [glob_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/linux/profiling/html/glob.html)
   * [scandir_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/linux/profiling/html/scandir.html)
   * [walk_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/linux/profiling/html/walk.html)
   * [find_custom_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/linux/profiling/html/find_custom.html)
   * [find_custom_mem_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/linux/profiling/html/find_custom_mem.html)
   * [find_custom_mem_qread_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/linux/profiling/html/find_custom_mem_qread.html)
   * [mlocate_custom_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/linux/profiling/html/mlocate_custom.html)
   * [mlocate_custom_mem_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/linux/profiling/html/mlocate_custom_mem.html)
   * [mlocate_custom_mem_qread_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/linux/profiling/html/mlocate_custom_mem_qread.html)
   
   The results in text form:
   * ```
      Sun Mar 15 09:20:48 2020    glob.prof
         9396177 function calls (8898745 primitive calls) in 22.342 seconds
     ```
   * ```
      Sun Mar 15 09:20:54 2020    scandir.prof
         6827925 function calls (3098585 primitive calls) in 5.984 seconds
     ```
   * ```
      Sun Mar 15 09:20:57 2020    walk.prof
         3336312 function calls (3002316 primitive calls) in 3.008 seconds
     ```
   * ```
      Sun Mar 15 09:20:59 2020    find_custom.prof
         251499 function calls in 1.232 seconds
     ```
   * ```
      Sun Mar 15 09:21:00 2020    find_custom_mem.prof
         251499 function calls in 1.003 seconds
     ```
   * ```
      Sun Mar 15 09:21:01 2020    find_custom_mem_qread.prof
         242787 function calls in 1.087 seconds
     ```
   * ```
      Sun Mar 15 09:21:02 2020    mlocate_custom.prof
         60601 function calls in 1.596 seconds
     ```
   * ```
      Sun Mar 15 09:21:03 2020    mlocate_custom_mem.prof
         60601 function calls in 0.950 seconds
     ```
   * ```
      Sun Mar 15 09:21:04 2020    mlocate_custom_mem_qread.prof
         59325 function calls in 0.962 seconds
     ```

  What does that actually look like?
  Using [plot.ly](https://www.plot.ly/) I created [this](https://plot.ly/~jimbob88/3/) fancy looking graph:
    ![Fancy Graph](https://user-images.githubusercontent.com/9913366/76705317-11272000-66d7-11ea-8b99-de1a4aea1acc.png)

  But wait, what is that I see, is that `mlocate` outperforming `find`, what is this madness! Well here comes the "bane of mlocate" as mentioned previously, `mlocate` forces one to do an `updatedb` everytime you want to recache all of the files on your system. So how long does this take on my system? A full run of `updatedb` (the command for this looks like this: `time sudo updatedb --output test.db`) takes `real 0m12.446s`; however, this isn't a very fair test as one would not be expected to rebuild the whole database every time, instead if you were to do a partial update that would cost you `real	0m2.259s`.
  Now if we refit the graph with the mlocate timings + the `partial updatedb`, I know this isn't very accurate because it would take slightly longer for the delay of running the command through `subprocess`, [the graph](https://plot.ly/~jimbob88/5/) then fits like so:
  ![Fancy Graph Refit](https://user-images.githubusercontent.com/9913366/76705724-ea1e1d80-66d9-11ea-8a01-8f2c2a4cedb1.png)
  
  Ah yes, here comes a more obvious issue with `mlocate`, we see that it is now outperformed by Walk (even though walk has an order of a magnitude higher amount of function calls), which is `0.847s` faster than the fastest `mlocate` implementation. But why is `os.walk` so god damn fast? I mean for a start the [scandir github page](https://github.com/benhoyt/scandir) literally says `scandir, a better directory iterator and faster os.walk()`. Well with a quick minute of Googling, we can find the answer, since scandir was added to python in [PEP 471](https://www.python.org/dev/peps/pep-0471/), `os.walk()` was optimized to be faster along with it, with [them suggesting 8-9x performance boosts on Windows systems](https://www.python.org/dev/peps/pep-0471/#id16)! 

# What should you use in your next Linux python project?
|        Function vs Aspect       | Performance (s) | Cross Compatible (Linux 2 Windows) |         Pythonic         |
|:-------------------------------:|:---------------:|:----------------------------------:|:------------------------:|
|           glob_search           |      22.342     |         :heavy_check_mark:         |    :heavy_check_mark:    |
|          scandir_search         |      5.984      |         :heavy_check_mark:         |    :heavy_check_mark:    |
|           walk_search           |      3.008      |         :heavy_check_mark:         |    :heavy_check_mark:    |
|        find_custom_search       |      1.232      |      :heavy_multiplication_x:      | :heavy_multiplication_x: |
|      find_custom_mem_search     |      1.003      |      :heavy_multiplication_x:      | :heavy_multiplication_x: |
|   find_custom_mem_qread_search  |      1.087      |      :heavy_multiplication_x:      | :heavy_multiplication_x: |
|      mlocate_custom_search      |  1.596 + ~2.259 |      :heavy_multiplication_x:      | :heavy_multiplication_x: |
|    mlocate_custom_mem_search    |  0.950 + ~2.259 |      :heavy_multiplication_x:      | :heavy_multiplication_x: |
| mlocate_custom_mem_qread_search |  0.962 + ~2.259 |      :heavy_multiplication_x:      | :heavy_multiplication_x: |

Above is a table with basically all you need to know for which to choose. Using `os.walk` is fastest, cross-compatible & pythonic and so is probably the best to use on your next release project; however, if you have a personal program running at home or for a specific userbase the best to use is `find_custom_mem_search` (if there is no `ramfs` or `tmpfs` you either have to [make one](https://unix.stackexchange.com/a/59305/391053) or use `find_custom_mem_qread_search`). So when should one use `mlocate`, only use this if you know the file system is going to remain static and only update once every day or so (for example searching through the fonts folder once per day).

Hope this helps you :) Have fun tinkering!

