# interbotix_ws

Working workspace for trossen locobot rovers 

Steps to setup on your computer:
1. install ros-noetic by following the tutorial found at: http://wiki.ros.org/ROS/Installation
      If you're running on a windows machine this tutorial may be useful: https://jack-kawell.com/2020/06/12/ros-wsl2/

2. install catkin-tools by following this tutorial: https://catkin-tools.readthedocs.io/en/latest/installing.html

3. clone this repo into your home directory: 
      $ cd
      $ git clone https://github.com/rqn99/interbotix_ws.git

4. run this in terminal to install missing controller packages 
      $ sudo apt-get install ros-noetic-ros-control ros-noetic-ros-controllers

5. run the following in terminal to install all dependancies and build the workspace 
      $ cd ~/interbotix_ws
      $ rosdep install -y --from-paths . --ignore-src --rosdistro noetic
      $ catkin build
      
6. run the following in terminal to properly source your workspace
      $ echo "source ~/interbotix_ws/devel/setup.bash" >> ~/.bashrc
      $ source ~/.bashrc

That's it! You should have a functional workspace:) 

To test your workspace try:
      $ roslaunch interbotix_xslocobot_moveit xslocobot_moveit.launch robot_model:=locobot_wx250s show_lidar:=true dof:=6 use_gazebo:=true use_moveit_rviz:=true
several windows should open after a moment open another terminal and run:
      $ rosservice call /gazebo/unpause physics 
otherwise rviz will never launch 
