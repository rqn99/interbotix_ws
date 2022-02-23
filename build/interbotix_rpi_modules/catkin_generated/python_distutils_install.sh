#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/renee/interbotix_ws/src/interbotix_ros_toolboxes/interbotix_rpi_toolbox/interbotix_rpi_modules"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/renee/interbotix_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/renee/interbotix_ws/install/lib/python3/dist-packages:/home/renee/interbotix_ws/build/interbotix_rpi_modules/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/renee/interbotix_ws/build/interbotix_rpi_modules" \
    "/usr/bin/python3" \
    "/home/renee/interbotix_ws/src/interbotix_ros_toolboxes/interbotix_rpi_toolbox/interbotix_rpi_modules/setup.py" \
     \
    build --build-base "/home/renee/interbotix_ws/build/interbotix_rpi_modules" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/renee/interbotix_ws/install" --install-scripts="/home/renee/interbotix_ws/install/bin"
