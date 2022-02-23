execute_process(COMMAND "/home/renee/interbotix_ws/build/interbotix_perception_modules/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/renee/interbotix_ws/build/interbotix_perception_modules/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
