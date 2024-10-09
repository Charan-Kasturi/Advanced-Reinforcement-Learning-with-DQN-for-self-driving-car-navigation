# Advanced-Reinforcement-Learning-with-DQN-for-self-driving-car-navigation
ENPM690-Robot Learning
## Files
1) Final_with_obstacle.mp4
2) Final_without_obstacle.mp4
3) testing.zip
4) ENPM690_charan03_ksharma7_fp
5) turtlebot3_gazebo.zip

## Setup
1) Download the zip files with names 'testing.zip' and 'turtlebot3_gazebo.zip'
2) Create a ROS2 workspace 
3) Create a src directory in the workspace
4) Extract the testing.zip to src
5) Install the required libraries(tensorflow(version==2.13.1),numpy,opencv2,matplotlib)
6) Clone the turtlebot3 and its dependencies
    git clone -b ros2 https://github.com/ROBOTIS-GIT/turtlebot3.git
    git clone -b ros2 https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
    git clone -b ros2 https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
    git clone -b ros2 https://github.com/ROBOTIS-GIT/DynamixelSDK.git
    git clone -b ros2 https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver.git

    rosdep update
    rosdep install --from-paths src --ignore-src -r -y

7) Change the MODEL to waffle_pi in bashrc or zshrc script
8) Extract the turtlebot3_gazebo.zip to the cloned turtlebot3_gazebo package, overwriting any files with conflicts. The extra additions are the world files and launch files.
9) Navigate to the main directory of the workspace
10) Delete build,log and install directories if they exist
11) Build the workspace: colcon build
10) Run this command in the terminal: source install/setup.bash


## Evaluation

### Evaluation Without Obstacles:
Terminal 1: ros2 launch turtlebot3_gazebo Without_Obstacles.launch.py  
Terminal 2: ros2 run testing without_obstacle_evaluation  
![](https://github.com/charankasturi/Advanced-Reinforcement-Learning-with-DQN-for-self-driving-car-navigation/blob/main/Without_Obstacles_Evaluation.gif)  

### Evaluation With Obstacles:
Terminal 1: ros2 launch turtlebot3_gazebo With_Obstacles.launch.py    
Terminal 2: ros2 run testing with_obstacle_evaluation  
![](https://github.com/charankasturi/Advanced-Reinforcement-Learning-with-DQN-for-self-driving-car-navigation/blob/main/With_Obstacles_Evaluation.gif)

## Training

### Training Without Obstacles:
Terminal 1: ros2 launch turtlebot3_gazebo Without_Obstacles.launch.py  
Terminal 2: ros2 run testing without_obstacle_training  
![](https://github.com/charankasturi/Advanced-Reinforcement-Learning-with-DQN-for-self-driving-car-navigation/blob/main/Without_Obstacles_Training.gif)  


### Training With Obstacles:
Terminal 1: ros2 launch turtlebot3_gazebo With_Obstacles.launch.py  
Terminal 2: ros2 run testing with_obstacle_training  
![](https://github.com/charankasturi/Advanced-Reinforcement-Learning-with-DQN-for-self-driving-car-navigation/blob/main/With_Obstacles_Training.gif)
