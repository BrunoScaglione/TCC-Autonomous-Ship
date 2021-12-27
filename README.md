<h1 align="center">
    Integrating a high fidelity ship maneuvering simulator with <i>ROS2</i> : a path-following case study
</h1>

<p align="center">
    Undergraduate Thesis for the obtention of the Mechatronics Engineering degree from the University of São Paulo (USP).
</p>

<p >
    This project develops the <i>pydyna_simple</i> package that encapsulates <i>pydyna's</i> maneuvering simulator in a <i>ROS2</i> node and enables taking advantage of it in the <i>ROS2</i> environment. There, it can be combined with multiple other packages natively and in modular fashion. In this structure, the project can also scale very well to a complex robotic system when more modules are added. The package proposition is done in the context of a proof-of-concept case study, where the aim is to provide enough demonstration of the capabilities that come along with the <i>ROS2</i> environment. It is a path-following scenario, similar to the ones in <i>fast-time</i> simulations done by TPN. The study case is encapsulated in the <i>path_following</i> package. Therefore, this repo holds two packages. An overview of these two packages is given below. 
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

## ROS2 terminology

- ***node:*** independent processes that are able to send and receive data from each other;
- ***topic:*** one of the means in which nodes can send (by publishing to a *topic*) and receive (subscribing to a *topic*) data;
- ***service:*** another mean of communication between *nodes* with a request and response pattern. Can be asynchronous or synchronous. In our application only asynchronous services are used;
- ***msg and srv files:*** *msg* files define the data structure for *topics* and *srv* files for services. There are standard libraries with basic data types and structures available for use, but custom implementations are also needed in the application;
- ***rosbag:*** tool that subscribes to topics and writes a bag file with the contents of all messages published on those specified topics. A bag file is essentially a *sqlite* database.

## Features

### *pydyna_simple* package

### *path_following* package

<p align="center">
    GNC architecture of the <i>path_following</i> package.
</p>

<div align="center">
    <img 
         src="https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/readme_resources/architecture.png" 
    >
</div>

<!-- - **/initialCondition** — POST request that sends the initial state of the vessel;
- **/waypoints** — POST request that sends the desired waypoints of the vessel;
- **/start** — GET request that starts the simulation;
- **/stop** — GET request that kills *pydyna* node;
- **/shutdown** — GET request that kills all the nodes, except for the backend. -->

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
* DDS implementation\*<sup>1</sup>;
* *OpenCV*;
* *CMake*;
* *Qt5*;
* *Graphviz*;
* *xmllint*;

## Folder structure

**/**:
  - **/some_folder1** &#8594; explanation:
      - **/some_folder1/some_folder2** &#8594; exaplanation:
          - some_file1 &#8594; explanation;
          - some_file2 &#8594; explanation.
      - **/some_folder1/some_folder3** &#8594; explanation:
          - some_file3 &#8594; explanation;
          - some_file4 &#8594; explanation.

## Getting started

### *pydyna_simple* package

### *path_following* package

* Explanation of the command here:

```bash
   some_command
```

* Explanation of the command here:

```bash
   some_command
```

## Useful scripts

### *pydyna_simple* package

### *path_following* package

## Project details

Our monograph, paper and slides are inside the *reports* folder.

[Monograph here](https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/reports/Monograph.pdf).
[Paper here](https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/reports/Paper.pdf).
[Slides here](https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/reports/Slides.pdf).

## Important notes

\*<sup>1</sup> — explanation of DDS problem here <br> 
\*<sup>2</sup> — explanation here

## Additional material on *ROS2*

ROS2 documentation and tutorials can be [found here](https://docs.ros.org/en/galactic/index.html). A ROS2 CLI cheatsheet can be [found here](https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/notes/ros2_notes/cli_cheats_sheet.pdf). Our ROS2 notes can be [found here](https://github.com/BrunoScaglione/TCC-Autonomous-Ship/blob/main/notes/ros2_notes/ros2_notes.txt).

## Authors

Bruno Scaglione and Pedro Marzagão are the developers of the project. Here is Bruno's [linkedin profile](https://www.linkedin.com/in/bruno-scaglione-4412a0165). Here is Pedro's [linkedin profile](https://www.linkedin.com/in/pedro-marzagao).
