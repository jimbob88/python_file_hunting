# My Approach
Since my original [Linux Analysis](https://github.com/jimbob88/python_file_hunting/tree/master/linux), I have looked into working with file searches within the Windows operating system, even if I have a rather melodramatic love hate relationship with the way Microsoft works. For example, they have some amazing programming tools like VS Code & VS; however, they also have, in my opinion, stupid "intuitive" features that don't work properly (try copying only the `.HTM` file from a saved website) and often force me to use Command Line WSL (Windows Subsystem for Lunux) so as to get them to work as I want.

More detail about why I did this project is noted in the Linux section and the core `README.MD` of this GitHub Repository but lets get on with some analysis, after a quick note about why you should profile ;) 


### Why Profile?
Whenever you want to time your program to see how long it takes ALWAYS profile, never make an excuse, just do it. Why? Well let's look at this quote from the [Cython Documentation](https://cython.readthedocs.io/en/latest/src/tutorial/profiling_tutorial.html):

>But remember the golden rule of optimization: Never optimize without having profiled. Let me repeat this: Never optimize without having profiled your code. Your thoughts about which part of your code takes too much time are wrong. At least, mine are always wrong.

So let us have a look into the functions I have used and the profiling results!

### The Different Methods
I decided to mess with a couple of different methods, some use built-in functions & others use external dependencies, here is the rundown of these methods:
##### Built-in Methods
 * `return_list`: as all of these return an iterator they all take very little time as they only return the values when they are actually needed. To force them to be called, the return_list decorator runs the function and returns the list() of the iterative.
 * `glob_search` taken from a [stackexchange post](https://codereview.stackexchange.com/a/186705), specifically I  chose the windows version for the linux tests, it is an iterative function that uses the built-in `glob` module
 * `scandir_search` taken from the aforementioned [stackexchange post](https://codereview.stackexchange.com/a/186705) this shows an example of an iterative `scandir` function from the built-in `os` module.
 * `walk_search` is taken from onion_file_search and is a pretty generic implementation that can be found across the internet in varying ways.
##### DOS `DIR` COMMAND
 * `dir_custom_search` runs the Windows `dir` command, and writes the data directly to a text file, this file is then read and each line is yielded.
 * `dir_custom_altsplit_search` is the same as `dir_custom_search` yet it doesn't use `f.read().splitlines()` but instead just slices the last character of the string, which is `\n`, essentially resulting in the same return.
 * `dir_custom_rstrip_search` is the same as `dir_custom_search` yet it doesn't use `f.read().splitlines()` but instead use `rstrip` to remove trailing white spaces from the string.
 * `dir_custom_tkpre_search` works by running the `dir` command, and then writing the result to the clipboard, and using a pregenerated Tkinter window to grab the current Clipboard. 
 * `dir_custom_tkon_search` works by running the `dir` command, and then writing the result to the clipboard, and then creates a Tk window and yeilds each line of the clipboard
 * `dir_custom_win32_search` works by running the `dir` command, and then writing the result to the clipboard, and then uses win32 to open the clipboard and get the clipboard data.
 
##### Windows 7+ `WHERE` COMMAND
 * `where_custom_search` runs the Windows `where` command, and writes the data whereectly to a text file, this file is then read and each line is yielded.
 * `where_custom_altsplit_search` is the same as `where_custom_search` yet it doesn't use `f.read().splitlines()` but instead just slices the last character of the string, which is `\n`, essentially resulting in the same return.
 * `where_custom_rstrip_search` is the same as `where_custom_search` yet it doesn't use `f.read().splitlines()` but instead use `rstrip` to remove trailing white spaces from the string.
 * `where_custom_tkpre_search` works by running the `where` command, and then writing the result to the clipboard, and using a pregenerated Tkinter window to grab the current Clipboard. 
 * `where_custom_tkon_search` works by running the `where` command, and then writing the result to the clipboard, and then creates a Tk window and yeilds each line of the clipboard
 * `where_custom_win32_search` works by running the `where` command, and then writing the result to the clipboard, and then uses win32 to open the clipboard and get the clipboard data.

##### Brmmm3's [scandir_rs](https://github.com/brmmm3/scandir-rs) module
 * `scandir_rs_search` uses the `scandir_rs.walk.Walk` function to loop through all of the folders and files like `os.walk`
 
These are then run through [profiler.py](https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/profiler.py) to get the profiled results.

## The Issues
`os.scandir` is the only function that discovered broken dynamic links, on my system I had a folder (`D:\\SteamLibrary\\steamapps\\common\\Arma 3\\!Workshop\\@Community Base Addon ver. 3.1.2`), which resulted in `os.scandir` stopping and raising the error `PermissionError: [WinError 21] The device is not ready` and it also raised an error on a folder (`D:\\SteamLibrary\\steamapps\\common\\DayZ\\!dzsal\\@TEST_EDZ`), which resulted in the error `FileNotFoundError: [WinError 3] The system cannot find the path specified`. None of the other functions brought this up so that should be noted if you are thinking of choosing `os.scandir` for your next project (make sure to do a `try: except:` ;)

`where` requires a directory string in the format `D:\SteamLibrary\` not `D:\SteamLibrary`.

## The Results
Tested on this folder:
```
Test Folder: 875 GB (940,413,947,220 bytes)
Contains: 435,044 Files, 22,908 Folders
```
The question is though, what did these results show to us? If you want to see all of this data visually, in your web browser, these are the different links for each function, it should be noted going [here](https://github.com/jimbob88/python_file_hunting/tree/master/windows/profiling/html), downloading them and viewing it works better & further more running [snakeviz](https://jiffyclub.github.io/snakeviz/) on [these files](https://github.com/jimbob88/python_file_hunting/tree/master/windows/profiling/profiles) will result in an even better experience:
 * [glob_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/walk.htm)
 * [scandir_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/scandir.htm)
 * [walk_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/walk.htm)
 * [dir_custom_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/dir_custom.htm)
 * [dir_custom_altsplit_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/dir_custom_altsplit.htm)
 * [dir_custom_rstrip_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/dir_custom_rstrip.htm)
 * [dir_custom_tkpre_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/dir_custom_tkpre.htm)
 * [dir_custom_tkon_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/dir_custom_tkon.htm)
 * [dir_custom_win32_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/dir_custom_win32.htm)
 * [where_custom_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/where_custom.htm)
 * [where_custom_altsplit_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/where_custom_altsplit.htm)
 * [where_custom_rstrip_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/where_custom_rstrip.htm)
 * [where_custom_tkpre_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/where_custom_tkpre.htm)
 * [where_custom_tkon_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/where_custom_tkon.htm)
 * [where_custom_win32_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/where_custom_win32.htm)
 * [scandir_rs_search](https://htmlpreview.github.io/?https://github.com/jimbob88/python_file_hunting/blob/master/windows/profiling/html/scandir_rs.htm)
 
 The results in text form:
  * ```
        Tue Mar 17 16:58:48 2020    glob.prof
          12619000 function calls (12236630 primitive calls) in 18.641 seconds
    ```
  * ```
        Tue Mar 17 16:58:55 2020    scandir.prof
          1468167 function calls (1369485 primitive calls) in 6.993 seconds
    ```
  * ```
        Tue Mar 17 16:59:06 2020    walk.prof
          3318998 function calls (2936401 primitive calls) in 11.454 seconds
    ```    
  * ```
        Tue Mar 17 16:59:15 2020    dir_custom.prof
          1615 function calls in 8.947 seconds
    ```  
  * ```
        Tue Mar 17 16:59:24 2020    dir_custom_altsplit.prof
          1645 function calls in 8.582 seconds
    ```  
  * ```
        Tue Mar 17 16:59:32 2020    dir_custom_rstrip.prof
          3245 function calls in 8.397 seconds
    ```  
  * ```
        Tue Mar 17 16:59:40 2020    dir_custom_tkpre.prof
          1620 function calls in 8.315 seconds
    ```  
  * ```
        Tue Mar 17 16:59:49 2020    dir_custom_tkon.prof
          1721 function calls (1720 primitive calls) in 8.313 seconds
    ```   
  * ```
        Tue Mar 17 16:59:57 2020    dir_custom_win32.prof
          1611 function calls in 8.336 seconds
    ```  
  * ```
        Tue Mar 17 17:00:20 2020    where_custom.prof
          2078 function calls in 23.305 seconds
    ```  
  * ```
        Tue Mar 17 17:00:44 2020    where_custom_altsplit.prof
          2118 function calls in 23.327 seconds
    ```  
  * ```
        Tue Mar 17 17:01:09 2020    where_custom_rstrip.prof
          4181 function calls in 25.281 seconds
    ```
  * ```
        Tue Mar 17 17:01:34 2020    where_custom_tkpre.prof
          2079 function calls in 24.845 seconds
    ```
  * ```
        Tue Mar 17 17:01:58 2020    where_custom_tkon.prof
          2184 function calls (2183 primitive calls) in 24.396 seconds
    ```
  * ```
        Tue Mar 17 17:02:23 2020    where_custom_win32.prof
          2074 function calls in 24.342 seconds
    ```
  * ```
        Tue Mar 17 17:02:25 2020    scandir_rs.prof
          114539 function calls in 2.288 seconds
    ```

And as always, [a fancy graph](https://chart-studio.plot.ly/~jimbob88/8#plot), oooo! 
![Windows Fancy Graph](https://user-images.githubusercontent.com/9913366/76897857-6eb09d80-688c-11ea-8496-97b826b395a1.png)

## What does this actually mean though?
Well from the graph one can see that `scandir_rs` is the fastest, with it being 3x faster than the closest competititor, so I would thoroughly recommend [checking it out](https://github.com/brmmm3/scandir-rs) as it is superb, and one can almost always translate `os.walk` code into `scandir_rs` for a high performance file search, quickly and easily. 
The only issue I encountered with `scandir_rs` was that the current build errors out; however, I am glad to say [the developer](https://github.com/brmmm3) is [working to fix it](https://github.com/brmmm3/scandir-rs/issues/1#issuecomment-599877357).

## So `scandir_rs` for days?
Well yes, one can simply install it with `pip install scandir-rs` (as long as they are using a [support python version](https://pypi.org/project/scandir-rs/#files)) and they can then start to use this beautiful state of the art module!

Hope this helps y'all,
Jim
