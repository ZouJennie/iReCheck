# Controlling QTrobot´s behaviours

## Preparation and requirements
Before running the program, please ensure that following setups of your QTrobot and your machine which running the program.

### QTrobot setup
Please copy the package qt_behaviour_control of this folder to the catkin_ws of QTrobot (qtrobot@qtrobot) from your PC by following these steps:
```
$ scp -r ~/YOURPATH/QT_ws/src/qt_behaviour_control qtrobot@qtrobot:~/catkin_ws/src/
```
Don´t forget replace YOURPATH by your path of folder

Then open a new terminal and connect to the QTrobot by using ssh and catkin_make the workspace:
```
qtrobot@QTXXX: cd catkin_ws
qtrobot@QTXXX: catkin_make
qtrobot@QTXXX: source devel/setup.bash
```
To be sure that new type of msg are successfully added in the QTrobot workspace, you need to verify:
```
qtrobot@QTXXX: rosmsg show qt_behaviour_control/GestureCommand
```
You will see:
``` 
string name
float32 speed
```

### PC setup
**add package to the workspace and catkin_make:**

Please copy the package comportement_control to your ROS workspace and `catkin_make` your workspace and `source devel/setup.bash`. Of course if you don´t have a ROS workspace, you can directly use this folder as a workspace by catkin_make this folder.
**Download PyQt5:**

Because PyQt5 do not support pyhton 2.7 so you need install python 3 or newer. Then you need to install PyQt5:
``` 
$ python3 -m pip install PyQt5 
```

## How to run the program
### Run the program in the QTrobot
You need at first run the subsciber in QTrobot:
```
qtrobot@QTXXX: cd catkin_ws
qtrobot@QTXXX: rosrun qt_behaviour_control control_subscriber.py
```

### Run the program in your PC
You need now run the interface in your PC:
```
$ cd ~/YOURWORKSPACE/
$ rosrun comportement_control qt_interface.py
```
Now you will see a interface for control the robot and normally when you click button the robot will do the behaviour. If not, you may close the subsciber in QTrobot and run it again.

 
