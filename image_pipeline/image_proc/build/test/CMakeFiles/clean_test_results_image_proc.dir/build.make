# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/odroid/catkin_ws/src/image_pipeline/image_proc

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/odroid/catkin_ws/src/image_pipeline/image_proc/build

# Utility rule file for clean_test_results_image_proc.

# Include the progress variables for this target.
include test/CMakeFiles/clean_test_results_image_proc.dir/progress.make

test/CMakeFiles/clean_test_results_image_proc:
	cd /home/odroid/catkin_ws/src/image_pipeline/image_proc/build/test && /usr/bin/python /opt/ros/kinetic/share/catkin/cmake/test/remove_test_results.py /home/odroid/catkin_ws/src/image_pipeline/image_proc/build/test_results/image_proc

clean_test_results_image_proc: test/CMakeFiles/clean_test_results_image_proc
clean_test_results_image_proc: test/CMakeFiles/clean_test_results_image_proc.dir/build.make

.PHONY : clean_test_results_image_proc

# Rule to build all files generated by this target.
test/CMakeFiles/clean_test_results_image_proc.dir/build: clean_test_results_image_proc

.PHONY : test/CMakeFiles/clean_test_results_image_proc.dir/build

test/CMakeFiles/clean_test_results_image_proc.dir/clean:
	cd /home/odroid/catkin_ws/src/image_pipeline/image_proc/build/test && $(CMAKE_COMMAND) -P CMakeFiles/clean_test_results_image_proc.dir/cmake_clean.cmake
.PHONY : test/CMakeFiles/clean_test_results_image_proc.dir/clean

test/CMakeFiles/clean_test_results_image_proc.dir/depend:
	cd /home/odroid/catkin_ws/src/image_pipeline/image_proc/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/odroid/catkin_ws/src/image_pipeline/image_proc /home/odroid/catkin_ws/src/image_pipeline/image_proc/test /home/odroid/catkin_ws/src/image_pipeline/image_proc/build /home/odroid/catkin_ws/src/image_pipeline/image_proc/build/test /home/odroid/catkin_ws/src/image_pipeline/image_proc/build/test/CMakeFiles/clean_test_results_image_proc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/CMakeFiles/clean_test_results_image_proc.dir/depend

