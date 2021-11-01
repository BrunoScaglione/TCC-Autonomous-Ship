# pydyna

An API (Application Programming Interface) for interacting with the core of the TPN numerical engine via Python.

---

## Installation 

Since the API is distributed as a wheel file, for installing the package in Python one should run the following line at the command prompt:

```bash
pip install pydyna_7_2_3-py3-none-any.whl
```

## Dependencies 

See `requirements.txt` file for a list of all packages dependencies or run the following line at the command prompt to get all the necessary packages installed:

```bash
pip install -r requirements.txt
```

## Usage

Next script shows a simple example of running a simulation of a vessel while giving 35 degrees of rudder and maximum throttle at the main propeller.

### Example 1: a simple simulation

```python
import pydyna
import math

print('Loading...')

try:
  sim = pydyna.create_simulation()

  ship = sim.vessels['0']
  rudder = ship.rudders['0']
  rudder.dem_angle = math.radians(35)
  propeller = ship.thrusters['0']
  propeller.dem_rotation = propeller.max_rotation

  steps = 1000

  for i in range(0, steps):
      print('Step: ' + str(i))
      sim.step()

  pydyna.destroy_simulation(sim)
except:
    print('Error loading simulation!')

```

---

### Example 2: visualization with [Venus]

 [Venus]: https://doccode.tpn.usp.br/projetos/tpnship/install/venus/doc/
 
```python

import pydyna
import venus.viewer
import venus.helpers
import venus.objects
import math

sim = pydyna.create_simulation('Container_355_51_145.p3d')

if sim:
    viewer = venus.viewer.Venus()
    ANGRA_DOS_REIS = venus.objects.GeoPos(-23.06255, -44.2772)
    viewer.set_viewport(ANGRA_DOS_REIS, 15)

    ship = sim.vessels['30']
    rudder = ship.rudders['0']
    propeller = ship.thrusters['0']
    propeller.dem_rotation = propeller.max_rotation
    rudder.dem_angle = math.radians(10)

    ship_view = venus.objects.Vessel(position = venus.helpers.RelPos(ship.linear_position[0], ship.linear_position[1]).to_geo(ANGRA_DOS_REIS),
                                     angle = 90 - math.degrees(ship.angular_position[2]),
                                     size = venus.objects.Size(40, 120))
    viewer.add(ship_view)

    steps = 10000

    for i in range(1, steps):
        print('Step ' + str(i))
        sim.step()
        ship_view.position = venus.helpers.RelPos(ship.linear_position[0], ship.linear_position[1]).to_geo(ANGRA_DOS_REIS)
        ship_view.angle = 90 - math.degrees(ship.angular_position[2])

    pydyna.destroy_simulation(sim)

```

