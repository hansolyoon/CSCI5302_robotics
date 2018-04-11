execute_process(COMMAND "/home/odroid/catkin_ws/src/image_pipeline/camera_calibration/build/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/odroid/catkin_ws/src/image_pipeline/camera_calibration/build/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
