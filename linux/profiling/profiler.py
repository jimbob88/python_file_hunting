import pstats, cProfile

import test_processes

########################
### BUILT-IN METHODS ###
########################

cProfile.runctx("test_processes.glob_search('/media/james/Development/Programming', 'py')", globals(), locals(), "glob.prof")
s = pstats.Stats("glob.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx("test_processes.scandir_search('/media/james/Development/Programming', 'py')", globals(), locals(), "scandir.prof")
s = pstats.Stats("scandir.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx("test_processes.walk_search('/media/james/Development/Programming', 'py')", globals(), locals(), "walk.prof")
s = pstats.Stats("walk.prof")
s.strip_dirs().sort_stats("time").print_stats()

#######################
### FIND TEST SUITE ###
#######################

cProfile.runctx("test_processes.find_custom_search('/media/james/Development/Programming', 'py')", globals(), locals(), "find_custom.prof")
s = pstats.Stats("find_custom.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx("test_processes.find_custom_mem_search('/media/james/Development/Programming', 'py')", globals(), locals(), "find_custom_mem.prof")
s = pstats.Stats("find_custom_mem.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx("test_processes.find_custom_mem_qread_search('/media/james/Development/Programming', 'py')", globals(), locals(), "find_custom_mem_qread.prof")
s = pstats.Stats("find_custom_mem_qread.prof")
s.strip_dirs().sort_stats("time").print_stats()

##########################
### MLOCATE TEST SUITE ###
##########################

cProfile.runctx("test_processes.mlocate_custom_search('/media/james/Development/Programming', 'py')", globals(), locals(), "mlocate_custom.prof")
s = pstats.Stats("mlocate_custom.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx("test_processes.mlocate_custom_mem_search('/media/james/Development/Programming', 'py')", globals(), locals(), "mlocate_custom_mem.prof")
s = pstats.Stats("mlocate_custom_mem.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx("test_processes.mlocate_custom_mem_qread_search('/media/james/Development/Programming', 'py')", globals(), locals(), "mlocate_custom_mem_qread.prof")
s = pstats.Stats("mlocate_custom_mem_qread.prof")
s.strip_dirs().sort_stats("time").print_stats()