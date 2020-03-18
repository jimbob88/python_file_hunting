import pstats, cProfile
import test_processes

test_directory = '/media/james/Development/Programming'

########################
### BUILT-IN METHODS ###
########################

cProfile.runctx(f"test_processes.glob_search('{test_directory}', 'py')", globals(), locals(), "glob.prof")
s = pstats.Stats("glob.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.scandir_search('{test_directory}', 'py')", globals(), locals(), "scandir.prof")
s = pstats.Stats("scandir.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.walk_search('{test_directory}', 'py')", globals(), locals(), "walk.prof")
s = pstats.Stats("walk.prof")
s.strip_dirs().sort_stats("time").print_stats()

#######################
### FIND TEST SUITE ###
#######################

cProfile.runctx(f"test_processes.find_custom_search('{test_directory}', 'py')", globals(), locals(), "find_custom.prof")
s = pstats.Stats("find_custom.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.find_custom_mem_search('{test_directory}', 'py')", globals(), locals(), "find_custom_mem.prof")
s = pstats.Stats("find_custom_mem.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.find_custom_mem_qread_search('{test_directory}', 'py')", globals(), locals(), "find_custom_mem_qread.prof")
s = pstats.Stats("find_custom_mem_qread.prof")
s.strip_dirs().sort_stats("time").print_stats()

##########################
### MLOCATE TEST SUITE ###
##########################

cProfile.runctx(f"test_processes.mlocate_custom_search('{test_directory}', 'py')", globals(), locals(), "mlocate_custom.prof")
s = pstats.Stats("mlocate_custom.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.mlocate_custom_mem_search('{test_directory}', 'py')", globals(), locals(), "mlocate_custom_mem.prof")
s = pstats.Stats("mlocate_custom_mem.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.mlocate_custom_mem_qread_search('{test_directory}', 'py')", globals(), locals(), "mlocate_custom_mem_qread.prof")
s = pstats.Stats("mlocate_custom_mem_qread.prof")
s.strip_dirs().sort_stats("time").print_stats()

##################
### SCANDIR_RS ###
##################
cProfile.runctx(f"test_processes.scandir_rs_search('{test_directory}', 'py')", globals(), locals(), "scandir_rs.prof")
s = pstats.Stats("scandir_rs.prof")
s.strip_dirs().sort_stats("time").print_stats()