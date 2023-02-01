<h1 align="center">
    Integrating a high fidelity ship maneuvering simulator with <i>ROS2</i> : a path-following case study
</h1>

<p align="center">
    Undergraduate Thesis for the obtention of the Mechatronics Engineering degree from the University of São Paulo (USP).
</p>

<p >
    This project develops the <i>pydyna_simple</i> package that encapsulates <i>pydyna's</i> maneuvering simulator in a <i>ROS2</i> node and enables taking advantage of it in the <i>ROS2</i> environment. There, it can be combined with multiple other packages natively and in modular fashion. In this structure, the project can also scale very well to a complex robotic system when more modules are added. The package proposition is done in the context of a proof-of-concept case study, where the aim is to provide enough demonstration of the capabilities that come along with the <i>ROS2</i> environment. It is a path-following scenario, similar to the ones in <i>fast-time</i> simulations done by TPN. The case study is encapsulated in the <i>path_following</i> package. Therefore, this repo holds two packages. An overview of these two packages is given below. 
</p>

<p>
    <strong>
        <i>pydyna_simple</i> package: 
    </strong>  
    The <i>pydyna_simple</i> package has the objective of integrating <i>pydyna</i> to <i>ROS2</i>. This package contains the <i>pydyna_simple</i> <i>node</i>, which runs the simulation. The package also includes a <i>launch</i> file that should be used to launch the <i>node</i>, and consequently, the simulation. A <i>config</i> folder contains the necessary archives to support <i>pydyna's</i> functioning and installation (the main files are the <i>.p3d</i> files of the vessels, and the <i>.whl</i> file of the <i>pydyna</i> library).
</p>

<p>
    <strong>
        <i>path_following</i> 
        package:
    </strong> 
    The <i>path_following</i> package implements a ship that follows a path defined by <i>waypoints</i>. Each  <i>waypoint</i> is a tuple <i>(x, y, u)</i> where <i>x</i> and <i>y</i> define the location in the 2D plane and <i>u</i> is the desired velocity when passing through the aforementioned location. It is a complement to <i>pydyna_simple</i> package as it integrates a GNC (Guidance-Navigation-Control) architecture to <i>pydyna's</i> dynamical system. This package not only complements <i>pydyna</i> as a way of implementing it into the architecture of a path following vessel, but also includes a GUI to visualize the        vessel. Given the starting state and the desired <i>waypoints</i>, the vessel will then follow a path given by straight lines connecting the <i>waypoints</i> positions, following also the surge velocity given by the <i>waypoints</i> velocities. <br>
</p>

<p align="center">
    Example of the ship following a zigzag path (gif with speed increase).
</p>

<div align="center">
    <img 
         src="https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/readme_resources/zigzag.gif" 
    >
</div>

## *ROS2* terminology

- ***Node:*** independent processes that are able to send and receive data from each other;
- ***topic:*** one of the means in which nodes can send (by publishing to a *topic*) and receive (subscribing to a *topic*) data;
- ***service:*** another mean of communication between *nodes* with a request and response pattern. Can be asynchronous or synchronous. In our application only asynchronous services are used;
- ***msg and srv files:*** *msg* files define the data structure for *topics* and *srv* files for services. There are standard libraries with basic data types and structures available for use, but custom implementations are also needed in the application;
- ***rosbag:*** tool that subscribes to topics and writes a bag file with the contents of all messages published on those specified topics. A bag file is essentially a *sqlite* database.

## Features

### *pydyna_simple* package

<p align="center">
      <i>rqt</i> graph of the <i>pydyna_simple</i> package. Topics are rectangles and nodes are elipses.
</p>

<div align="center">
    <img 
         src="https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/readme_resources/pydyna_simple__graph.png" 
    >
</div>

With this package, the user is able to start the simulation with a *request* using a service containing the initial state of the vessel, propeller rotation and yaw angle. After the simulation is initialized, the user can give two inputs to *pydyna*: propeller rotation and the rudder angle. The *pydyna* node subscribes to these two inputs as *topics*, runs one step of the simulation only when it has received both of these inputs, and publishes the next state of the vessel to the *state topic*. Ending the simulation is also an option and can be done with one of two topics: *end* or *shutdown*. The last relates to the *path_following* package that will presented afterwards.

To start a simulation, a request has to be sent using the service **InitValues.srv**, shown in _**Source Code 1**_. This service is a custom *srv* file. This file contains a request and response in *yaml* format. Request and response are separated by a dashed line. The request contains four properties: **initial_state**, **waypoints**, **surge** and **yaw**. The **initial_state** property contains the initial state of the vessel. The **waypoints** property is not used in this case. The **surge** and **yaw** properties are the inital values for propeller rotation and rudder angle, respectively. The values to the right are the default values for the properties.

The three, mentioned earlier, *topics* are: **propeller_rotation**, **rudder_angle** and **state**; and are defined by their *msg* files. Propeller rotation and rudder angle use the standard library *Float32 msg file*. The state, seen in _**Source Code 2**_, uses a custom *yaml-styled msg* file that contains **time**, **position** and **velocity** properties, which are *msg* files by themselves. Position is a set of three *Float32* properties: **x**, **y** and **theta**, seen in _**Source Code 3**_. Velocity, in the same way, is defined by having **u**, **v** and **r**, seen in _**Source Code 4**_. The values to the right are the default values for the properties.

All custom *msg* and *srv* files are defined and in a separate package for flexibility. This
package is called *path_following_interfaces*. After building the aforementioned package, these
data structures can be imported in nodes as *Python* objects.


#### Source Code 1 - **InitValues.srv**
```python
#request
State initial_state
Waypoints waypoints
float32 surge 0.0
float32 yaw 0.0
---
#response 
float32 surge 0.0
float32 yaw 0.0
```

#### Source Code 2 - **State.msg**
```python
# 3DOF state of the craft
Position position 
Velocity velocity
float32 time 0.0
```

#### Source Code 3 - **Position.msg**
```python
# positions (earth-fixed reference frame)
float32 x 0.0
float32 y 0.0
# 1.57079632679 radians = 90 degrees
float32 theta 1.57079632679 
```

#### Source Code 4 - **Velocity.msg**
```python
# velocities (craft-fixed reference frame)
float32 u 1.0
float32 v 0.0
float32 r 0.0
```

### <a name="features>path_following">*path_following* package

<p align="center">
    GNC architecture of the <i>path_following</i> package.
</p>

<div align="center">
    <img 
         src="https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/readme_resources/architecture.png" 
    >
</div>

With the nodes active, it’s possible to visualize the vessel in <http://localhost:6150>. Using the packages’ **HTTP API**, then send requests to start the simulation, the initial state of the vessel, and the desired *waypoints* to <http:localhost:5000>.

In order to run the simulation with desired parameters, the user must send two **POST** and one **GET** request. Send the initial state to **/initial_condition**, illustrated in Figure **X**, and desired waypoints to **/waypoints**, illustrated in Figure **X**. In **/waypoints**, the “from_gui” property, for the time being, is always zero. This is because the *waypoints* are given solely through the HTTP Client, however, in future work the value 1 will say to the backend that it should ignore the *waypoints* in the *payload*, and instead get them from the GUI’s application server. Then, the user sends a **GET** request to **/start**, illustrated in Figure **X**.

The user can also end the simulation in two ways: killing only *pydyna* node or killing all nodes except for *backend* node. The first one is achieved with a **GET** request to **/end**, illustrated in Figure **X**; while the second option is achieved with a **GET** request to **/shutdown**, illustrated in Figure **X**.

<p align="center">
    <b>POST</b> request to <b>/initial_condition</b>
</p>

<div align="center">
    <img 
         src="https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/readme_resources/insomniaInitial.PNG" 
    >
</div>

<p align="center">
    <b>POST</b> request to <b>/waypoints</b>
</p>        
       
<div align="center">
    <img 
         src="https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/readme_resources/insomniaWaypoints.PNG" 
    >
</div>
        
<p align="center">
    <b>GET</b> request to <b>/start</b>
</p>          

<div align="center">
    <img 
         src="https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/readme_resources/startget.png" 
    >
</div>

<p align="center">
    <b>GET</b> request to <b>/end</b>
</p>    
        
<div align="center">
    <img 
         src="https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/readme_resources/end_route.PNG" 
    >
</div>

<p align="center">
    <b>GET</b> request to <b>/shutdown</b>
</p>            
        
<div align="center">
    <img 
         src="https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/readme_resources/shutdown_route.PNG" 
    >
</div>

## Requirements

* *Windows 10*;
* *Python 3.6.8*;
* Python public libraries specified in *project_requirements.txt*;
* *pydyna* (*pydyna* is a private Python library made by TPN);
* *venus* (*venus* is a private Python library made by TPN);
* *ROS2* galactic;
* *Chocolatey*;
* *vcredist2013*;
* *vcredist140*;
* *OpenSSL*;
* *Visual Studio 2019*;
* DDS implementation<b>\*<sup>1</sup></b>;
* *OpenCV*;
* *CMake*;
* *Qt5*;
* *Graphviz*;
* *xmllint*;

## Folder structure

- **/** &#8594; root directory:
    - **/helpers** &#8594; contains complementary files:
        - **/helpers/payloads** &#8594; contains json payloads to be used with the project's HTTP API:
            - **comments.md** &#8594; comments on the payloads;
            - **initialCondition.json** &#8594; initial condition json payload;
            - **waypointsHexagon.json** &#8594; waypoints, that form an hexagon, json payload;
            - **waypointsLinear.json** &#8594; waypoints, that form an straight line, json payload;
            - **waypointsSantos.json** &#8594; waypoints, to be used at the port of Santos, json payload;
            - **waypointsZigZag.json** &#8594; waypoints, that form a zigzag, json payload;
        - **client.bat** &#8594; sends initial condition, waypoints and runs the path following simulation through *curl* HTTP requests, using payloads in /helpers/payloads;
        - **configpublic.bat** &#8594; configuration file, required to use the scripts in this folder;
        - **overlay.bat** &#8594; batch script that sources the workspace;
        - **path.bat** &#8594; batch script that runs the *path_following* package;
        - **pydyna.bat** &#8594;  batch script that runs the *pydyna_simple* package;
        - **vsbuildall.bat** &#8594; batch script that builds all packages;
    - **/notes** &#8594; contains useful notes on *pydyna* or *ROS2*:
        - **/notes/pydyna_docs** &#8594; *pydyna* documentation;
        - **/notes/ros2_notes** &#8594; our notes on some important *ROS2* commands;
    - **/readme_resources** &#8594; contains static files used in README.md;        
    - **/reports** &#8594; contains documents that explain the project, which were developed for the obtention of our Mechatronics Engineering degree:
        - **monograph.pdf** &#8594; monograph in ABNT like format (contains some diffferences);
        - **paper.pdf** &#8594; paper in IEEE format;
        - **slides.pdf** &#8594; slides developed in LaTex;
    - **/src** &#8594; contains project code:
        - **/src/experiments** &#8594; experiments made to develop some modules of the system:
            - **/src/experiments/notch-filter** &#8594; notch filter experimentation and development;
            - **/src/experiments/surge-control** &#8594; surge controller experimentation and development;
            - **/src/experiments/yaw-cotrol** &#8594; yaw controller experimentation and development;
        - **/src/main_ws** &#8594; *ROS2* worskpace:
            - **/src/main_ws/install** &#8594; overlay *ROS2* installation;
                - **/src/main_ws/install/lib** &#8594; contains installed *ROS2* packages;
                - **/src/main_ws/install/share** &#8594; contains files used by, or generated by, installed packages. Plots, logs and data (of the *ROS2* packages) go here;
            - **/src/main_ws/src** &#8594; source code of the *ROS2* packages;
                - **/src/main_ws/src/path_following** &#8594; *path_following* package : ship that follows a path defined by waypoints;
                - **/src/main_ws/src/path_following_interfaces** &#8594; *path_following_interfaces* package: provides *msg* and *srv* files to the other packages;
                - **/src/main_ws/src/pydyna_simple** &#8594; *pydyna_simple* package : ship dynamical system. Subscribes to rudder angle and propeller rotation, and publishes the state of the ship;
    - **project_requirements.txt** &#8594; requirements file for the project.
        
## Getting started

### *pydyna_simple* package

To install *ROS2* and pydyna, follow
the steps in the [*ROS2 Galactic* docs](https://docs.ros.org/en/galactic/index.html) and [TPN page](https://doccode.tpn.usp.br/projetos/tpnship) (need VPN access) respectively. Then, clone this repository.

1. To build packages, run the following command in **src/main_ws/src** with the *x64 Prompt for
Visual Studio 2019* terminal as admin:

```bash
~/tcc-autonomous-ship/src/main_ws/src> colcon build --merge -install
```

2. On the newly created install directory, source the workspace:

```bash
~/tcc-autonomous-ship/src/main_ws/install> call setup.bat
```

3. Next, run the launch file. This will create rosbags in the same directory. Therefore, the
recommendation is to run it in **src/main_ws/install/share/pydyna_simple/db**, which
is intended to store rosbags.

```bash
~/tcc-autonomous-ship/src/main_ws/install/share/pydyna_simple/db> ros2 launch pydyna_simple pydyna_simple.launch.py
```

4. In order to verify *topics*, the user may run:

```bash
~> ros2 topic list -t
```

5. To get a graph of *topics* and *nodes*, the user may run:

```bash
~> rqt_graph
```

6. With the _pydyna_simple node_ active, the user can, from the command line, start the simulation with the **init_simul** _service_, send _topics_ for **rudder_angle** and **propeller_rotation** and listen to **state**; each one of them in a separate terminal. In the example below, "{}" means taht the default values for InitValues will be used.

    a. start simulation by making a  _request_ to **init_simul**:
    ```bash
    ~> ros2 service call /init_simul path_following_interfaces/srv/InitValues "{}"
    ```
    
    b. publish 0 (example) to **rudder_angle**:
    ```bash 
    ~> ros2 topic pub --once /rudder_angle std_msgs/msg/Float32 "{data: 0}"
    ```
    
    c. publish 1 (example) to **propeller_rotation**:

    ```bash
    ~> ros2 topic pub --once /propeller_rotation std_msgs/msg/Float32 "{data: 1}"
    ```
    
    d. subscribe to **state**:
    
    ```bash 
    ~> ros2 topic echo /state
    ```

### *path_following* package  

To install *ROS2* and pydyna, follow
the steps in the [*ROS2 Galactic* docs](https://docs.ros.org/en/galactic/index.html) and [TPN page](https://doccode.tpn.usp.br/projetos/tpnship) (need VPN access) respectively. Then, the user must clone this repository. The first two steps are identical to the ones in the previous section.

1. To build packages, run the following command in **src/main_ws/src** with the x64 Prompt for Visual Studio 2019 terminal as admin:

```bash 
~/tcc-autonomous-ship/src/main_ws/src> colcon build --merge- install
```

2. On the newly created install directory, source the workspace:

```bash 
~/tcc-autonomous-ship/src/main_ws/install> call setup.bat
```

3. Next, run the launch file. This will create _rosbags_ in the same directory. Therefore, the recommendation is to run it in **src/main_ws/install/share/path_following/db** which is intended to store _rosbags_.

```bash 
~/tcc-autonomous-ship/src/main_ws/install/share/path_following/db> ros2 launch path_following path_following.launch.py
```

4. In order to verify *topics*, the user may run:

```bash
~> ros2 topic list -t
```

5. To get a graph of *topics* and *nodes*, the user may run:

```bash
~> rqt_graph
```

6. Just like for the _pydyna_simple node_, the user can publish and subscribe to different topics, or call services; to verify if they are working accordingly.

7. With all the nodes working, the user can visualize the vessel through _Venus_ on <http://localhost:6150>

8. Once the server is up and running, the user can send **HTTP** requests, giving the _initial conditions_ and _waypoints_, for example, using _Insomnia_ client. Once this is done, the user can send a request to start the simulation, in the same way. This is explained and illustrated in [this section](#features>path_following)
        
## Logs, plots and data
        
After running a simulation using a package, go to the package's installation and enter the *share* folder. There, you will find generated logs, data and eventually generated plots, of the last simulation. Below, the folders that contain these files are presented for each package.

### *pydyna_simple* package
        
- **/** &#8594; *pydyna_simple* installation *share* directory:
    - **/logs** &#8594; contains custom logs, logs generated by the *pydyna_simple* node and pydyna reports;
    - **/db** &#8594; contains *rosbags*.
        
### *path_following* package
        
- **/** &#8594; *path_following* installation *share* directory:
    - **/logs** &#8594; contains custom logs, logs generated by each node and pydyna reports;
    - **/plots** &#8594; contains generated plots;
    - **/db** &#8594; contains desired waypoints and rosbags.

## Useful scripts

We made some scripts to facilitate the process of setting up the environment, building and running the packages. In order to use these scripts, it is necessary to follow these two steps:

 1. In helpers/configpublic.bat: fill all *placeholder* values with the actual paths;
 2. Change the name configpublic to config.
 
 #### Source Code 5 - **configpublic.bat**
 ```batch
@REM ROS2 installation directory, where setup.bat is located
set underlay_path="placeholder"
@REM ROS2 worskpace source directory
set ws_src_path="placeholder"
@REM ROS2 workspace install directory, where local_setup.bat is located
set overlay_path="placeholder"
@REM ROS2 workspace directory
set main_ws_path="placeholder"

@REM pydyna_simple share directory: db folder
set pydyna_pkg_db_path="placeholder"
@REM pydyna_simple share directory: db>rosbags folder
set pydyna_pkg_rosbags_path="placeholder"

@REM path_following share directory: logs folder
set path_pkg_logs_path="placeholder"
@REM path_following share directory: db folder
set pydyna_pkg_db_path="placeholder"

@REM directory where http json payloads are being kept (only when using curl)
set payloads_path="placeholder" 
```

### *pydyna_simple* package
 
#### To build all the packages, run the following inside X64 Native Tools Comand Prompt for VS:
```batch
   ~/tcc-autonomous-ship/helpers> call vsbuildall.bat
```
#### To source the worskpace (set environment variables relative to your workspace), always run the following when starting a new terminal (process):
```batch
   ~/tcc-autonomous-ship/helpers> call overlay.bat
```
#### To run the *pydyna_simple* package, run the following in any terminal:
```batch
   ~/tcc-autonomous-ship/helpers> call pydyna.bat
```
### *path_following* package
        
#### To build all the packages, run the following inside X64 Native Tools Comand Prompt for VS:
```batch
   ~/tcc-autonomous-ship/helpers> call vsbuildall.bat
```
#### To source the worskpace (set environment variables relative to your workspace), always run the following when starting a new terminal (process):
```batch
   ~/tcc-autonomous-ship/helpers> call overlay.bat
```
#### To run the *path_following* package, run the following in any terminal:
```batch
   ~/tcc-autonomous-ship/helpers> call path.bat
```

## Project details

Our monograph, paper and slides are inside the *reports* folder.

[Monograph here](https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/reports/Monograph.pdf).
[Paper here](https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/reports/Paper.pdf).
[Slides here](https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/reports/Slides.pdf).

## Important notes

<b>\*<sup>1</sup></b> DDS stands for Data Distribution Service. *ROS2* uses a DDS implementation to do it's communication. In theory, *ROS2* already comes with a default DDS and there would be no necessity of further investigation. In practice however, we encountered problems and had to use a third-party DDS. We used *RTI Connext DDS*. To use it, we asked for a student's licence and followed the instructions provided.<br> 

## Additional material on *ROS2*

*ROS2* documentation and tutorials can be [found here](https://docs.ros.org/en/galactic/index.html). A *ROS2* CLI cheatsheet can be [found here](https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/notes/ros2_notes/cli_cheats_sheet.pdf). Our *ROS2* notes can be [found here](https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/notes/ros2_notes/ros2_notes.txt).

## Authors

Bruno Scaglione and Pedro Marzagão are the developers of the project. Here is Bruno's [linkedin profile](https://www.linkedin.com/in/bruno-scaglione-4412a0165). Here is Pedro's [linkedin profile](https://www.linkedin.com/in/pedro-marzagao).
