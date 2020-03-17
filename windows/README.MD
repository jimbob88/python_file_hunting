Test Folder: 875 GB (940,413,947,220 bytes)
Contains: 435,044 Files, 22,908 Folders


os.scandir is the only search that discovered "Arma3 !Workshop" which errors out in windows 
https://imgur.com/a/T9rZx01
Only one that errors out on linked folders that no longer exist

FileNotFoundError: [WinError 3] The system cannot find the path specified: 'D:\\SteamLibrary\\steamapps\\common\\DayZ\\!dzsal\\@TEST_EDZ'
PermissionError: [WinError 21] The device is not ready: 'D:\\SteamLibrary\\steamapps\\common\\Arma 3\\!Workshop\\@Community Base Addon ver. 3.1.2'


Traceback (most recent call last):
  File "profiler.py", line 9, in <module>
    cProfile.runctx(f"test_processes.glob_search('{test_directory}', 'exe')", globals(), locals(), "glob.prof")
  File "C:\Program Files\Python36\lib\cProfile.py", line 20, in runctx
    filename, sort)
  File "C:\Program Files\Python36\lib\profile.py", line 64, in runctx
    prof.runctx(statement, globals, locals)
  File "C:\Program Files\Python36\lib\cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 1
    test_processes.glob_search('D:\SteamLibrary\', 'exe')
                                                      ^
SyntaxError: invalid syntax
when using  "D:\\SteamLibrary\\" becuase of layered f strings and the  way runctx works

when using "D:\\SteamLibrary\\\\" errors out because "where"  expects the format D:\SteamLibrary not D:\SteamLibrary\ 


snakeviz doesn't work on windows, built using WSL, BIONIC