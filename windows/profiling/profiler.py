import pstats, cProfile
import test_processes

test_directory = "D:\\SteamLibrary"
dir_test_directory = "D:\\SteamLibrary\\\\"

########################
### BUILT-IN METHODS ###
########################
cProfile.runctx(f"test_processes.glob_search('{test_directory}', 'exe')", globals(), locals(), "glob.prof")
s = pstats.Stats("glob.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.scandir_search('{test_directory}', 'exe')", globals(), locals(), "scandir.prof")
s = pstats.Stats("scandir.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.walk_search('{test_directory}', 'exe')", globals(), locals(), "walk.prof")
s = pstats.Stats("walk.prof")
s.strip_dirs().sort_stats("time").print_stats()

########################
### DOS+ dir command ###
########################
cProfile.runctx(f"test_processes.dir_custom_search('{dir_test_directory}', 'exe')", globals(), locals(), "dir_custom.prof")
s = pstats.Stats("dir_custom.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.dir_custom_altsplit_search('{dir_test_directory}', 'exe')", globals(), locals(), "dir_custom_altsplit.prof")
s = pstats.Stats("dir_custom_altsplit.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.dir_custom_rstrip_search('{dir_test_directory}', 'exe')", globals(), locals(), "dir_custom_rstrip.prof")
s = pstats.Stats("dir_custom_rstrip.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.dir_custom_tkpre_search('{dir_test_directory}', 'exe')", globals(), locals(), "dir_custom_tkpre.prof")
s = pstats.Stats("dir_custom_tkpre.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.dir_custom_tkon_search('{dir_test_directory}', 'exe')", globals(), locals(), "dir_custom_tkon.prof")
s = pstats.Stats("dir_custom_tkon.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.dir_custom_win32_search('{dir_test_directory}', 'exe')", globals(), locals(), "dir_custom_win32.prof")
s = pstats.Stats("dir_custom_win32.prof")
s.strip_dirs().sort_stats("time").print_stats()

################################
### Windows 7+ where command ###
################################
cProfile.runctx(f"test_processes.where_custom_search('{test_directory}', 'exe')", globals(), locals(), "where_custom.prof")
s = pstats.Stats("where_custom.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.where_custom_altsplit_search('{test_directory}', 'exe')", globals(), locals(), "where_custom_altsplit.prof")
s = pstats.Stats("where_custom_altsplit.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.where_custom_rstrip_search('{test_directory}', 'exe')", globals(), locals(), "where_custom_rstrip.prof")
s = pstats.Stats("where_custom_rstrip.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.where_custom_tkpre_search('{test_directory}', 'exe')", globals(), locals(), "where_custom_tkpre.prof")
s = pstats.Stats("where_custom_tkpre.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.where_custom_tkon_search('{test_directory}', 'exe')", globals(), locals(), "where_custom_tkon.prof")
s = pstats.Stats("where_custom_tkon.prof")
s.strip_dirs().sort_stats("time").print_stats()

cProfile.runctx(f"test_processes.where_custom_win32_search('{test_directory}', 'exe')", globals(), locals(), "where_custom_win32.prof")
s = pstats.Stats("where_custom_win32.prof")
s.strip_dirs().sort_stats("time").print_stats()


##################
### SCANDIR_RS ###
##################
cProfile.runctx(f"test_processes.scandir_rs_search('{test_directory}', 'exe')", globals(), locals(), "scandir_rs.prof")
s = pstats.Stats("scandir_rs.prof")
s.strip_dirs().sort_stats("time").print_stats()