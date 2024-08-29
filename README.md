# `za_description` package

[![license - apache 2.0](https://img.shields.io/:license-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)

This package contains URDF files and meshes for the **Tormach ZA6** robot.

<p align="center">
  <img src=https://github.com/user-attachments/assets/3374a09c-8da8-4547-b49b-d1576fb6c3ab width=200/>
</p>

## Installation

Create a catkin workspace and clone the repository locally.

```shell
mkdir -p catkin_ws/src  && cd catkin_ws/src
git clone git@github.com:alexarbogast/za_description.git
```

Build the ROS package.

```shell
cd ../
catkin build
```

## Run the demo

After installation run the following command to visualize the robot:

```shell
roslaunch za_description za_arm_description.launch
```

## Further Assistance

- [ZA6 Robot Documentation](https://tormach.atlassian.net/wiki/spaces/ROBO/overview?homepageId=2822144301)
- [ROS URDF Tutorial](https://wiki.ros.org/urdf/Tutorials)
