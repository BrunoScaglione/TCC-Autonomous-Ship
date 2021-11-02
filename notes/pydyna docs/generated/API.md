<h1 id="pydyna">pydyna</h1>


<h2 id="pydyna.pydyna_7_2_3.create_simulation">create_simulation</h2>

```python
create_simulation(*args)
```

This function is the main API entry-point to create a new ``Simulation`` session.

__Parameters__

- __``p3d_or_json_file`` [optional] (string) __: the p3d or json filename containing the hydrodynamics model description to be loaded. If not provided, loads a default hydrodynamics model.

__Returns__

 ``Simulation``

<h2 id="pydyna.pydyna_7_2_3.destroy_simulation">destroy_simulation</h2>

```python
destroy_simulation(sim)
```

This function terminates a `Simulation` session.

__Parameters__

- __``sim`` (Simulation) __: the simulation instance to destroy

<h2 id="pydyna.pydyna_7_2_3.Simulation">Simulation</h2>

```python
Simulation(self, *args, **kwargs)
```
Main class to interact with a simulation. Use ``create_simulation()`` and ``destroy_simulation()`` for instance creation/deletion.
<h3 id="pydyna.pydyna_7_2_3.Simulation.catenaries">catenaries</h3>

Property (CatenaryDict): Dictionary of catenaries (id : Caternary)
<h3 id="pydyna.pydyna_7_2_3.Simulation.current">current</h3>

Property (Current): Environment current
<h3 id="pydyna.pydyna_7_2_3.Simulation.dt">dt</h3>

Property (float): Time interval for the integration step (s)
<h3 id="pydyna.pydyna_7_2_3.Simulation.fenders">fenders</h3>

Property (FenderDict): Dictionary of fenders (id : Fender)
<h3 id="pydyna.pydyna_7_2_3.Simulation.line_ordering">line_ordering</h3>

Property (string List): Original ordering of the lines as encountered in the P3d file
<h3 id="pydyna.pydyna_7_2_3.Simulation.max_steps">max_steps</h3>

Property (int): Number of steps to integrate in fast-time mode
<h3 id="pydyna.pydyna_7_2_3.Simulation.p3d_file">p3d_file</h3>

Property (string): P3d file used to generate this simulation
<h3 id="pydyna.pydyna_7_2_3.Simulation.thisown">thisown</h3>

The membership flag
<h3 id="pydyna.pydyna_7_2_3.Simulation.time_step">time_step</h3>

Property (int): Current integration time step
<h3 id="pydyna.pydyna_7_2_3.Simulation.vessels">vessels</h3>

Property (VesselDict): Dictionary of vessels Keys: (id : Vessel)
<h3 id="pydyna.pydyna_7_2_3.Simulation.wave">wave</h3>

Property (Wave): Environment wave
<h3 id="pydyna.pydyna_7_2_3.Simulation.wind">wind</h3>

Property (Wind): Environment wind
<h3 id="pydyna.pydyna_7_2_3.Simulation.step">step</h3>

```python
Simulation.step(self)
```
Runs an integration step.
<h3 id="pydyna.pydyna_7_2_3.Simulation.reset">reset</h3>

```python
Simulation.reset(self)
```
Resets the simulation to the initial condition just after it has been created.
<h2 id="pydyna.pydyna_7_2_3.Vessel">Vessel</h2>

```python
Vessel(self, *args, **kwargs)
```
Models an ownship with its hydrodynamical properties.
<h3 id="pydyna.pydyna_7_2_3.Vessel.anchors">anchors</h3>

Property (AnchorDict): Dictionary of anchors (id : Anchor) attached to this Vessel
<h3 id="pydyna.pydyna_7_2_3.Vessel.angular_acceleration">angular_acceleration</h3>

Property (float[3]): Angular acceleration (rad/s^2)
<h3 id="pydyna.pydyna_7_2_3.Vessel.angular_position">angular_position</h3>

Property (float[3]): Angular position (counter-clockwise radians)
<h3 id="pydyna.pydyna_7_2_3.Vessel.angular_velocity">angular_velocity</h3>

Property (float[3]): Angular velocity (rad/s)
<h3 id="pydyna.pydyna_7_2_3.Vessel.breadth">breadth</h3>

Property (float): breadth (m)
<h3 id="pydyna.pydyna_7_2_3.Vessel.draught">draught</h3>

Property (float): draught (m)
<h3 id="pydyna.pydyna_7_2_3.Vessel.external_forces">external_forces</h3>

Property (ForceDict): Dictionary of external forces (id : Force) acting on this Vessel
<h3 id="pydyna.pydyna_7_2_3.Vessel.height">height</h3>

Property (float): height (m)
<h3 id="pydyna.pydyna_7_2_3.Vessel.id">id</h3>

Property (string): Vessel identification
<h3 id="pydyna.pydyna_7_2_3.Vessel.internal_forces">internal_forces</h3>

Property (ForceDict): Dictionary of internal forces (id : Force) acting on this Vessel
Force id can be one of the following built-in values:
  "wave1stOrder", "waveMeanDrift", "waveSlowDrift",
  "waveDriftDamp", "swell1stOrder", "swellMeanDrift", "swellSlowDrift",
  "swellDriftDamp", "thrusters", "sheer", "rudders", "externalForces",
  "wind", "current", "lines", "hydrostaticRestoration", "towing",
  "squatting", "straitChannels", "damping", "inertial", "interactions"

<h3 id="pydyna.pydyna_7_2_3.Vessel.length">length</h3>

Property (float): length (m)
<h3 id="pydyna.pydyna_7_2_3.Vessel.linear_acceleration">linear_acceleration</h3>

Property (float[3]): Keel Midship (KMS) local acceleration (m/s^2)
<h3 id="pydyna.pydyna_7_2_3.Vessel.linear_position">linear_position</h3>

Property (float[3]): Keel Midship (KMS) position (m)
<h3 id="pydyna.pydyna_7_2_3.Vessel.linear_velocity">linear_velocity</h3>

Property (float[3]): Keel Midship (KMS) local velocity (m/s)
<h3 id="pydyna.pydyna_7_2_3.Vessel.mass">mass</h3>

Property (float): mass (t)
<h3 id="pydyna.pydyna_7_2_3.Vessel.rudders">rudders</h3>

Property (RudderDict): Dictionary of rudders (id : Rudder) attached to this Vessel
<h3 id="pydyna.pydyna_7_2_3.Vessel.thisown">thisown</h3>

The membership flag
<h3 id="pydyna.pydyna_7_2_3.Vessel.thrusters">thrusters</h3>

Property (ThrusterDict): Dictionary of thrusters (id : Thruster) attached to this Vessel
<h3 id="pydyna.pydyna_7_2_3.Vessel.volume">volume</h3>

Property (float): volume (m^3)
<h3 id="pydyna.pydyna_7_2_3.Vessel.water_velocity">water_velocity</h3>

Property (float[3]): Local current velocity relative to the vessel-fixed coordinate system (m/s)
<h3 id="pydyna.pydyna_7_2_3.Vessel.weight">weight</h3>

Property (float): weight (kN)
<h3 id="pydyna.pydyna_7_2_3.Vessel.wind_velocity">wind_velocity</h3>

Property (float[3]): Global wind velocity (m/s)
<h2 id="pydyna.pydyna_7_2_3.Rudder">Rudder</h2>

```python
Rudder(self, *args, **kwargs)
```
Models the hidrodynamics of a rudder attached to a ``Vessel``.
<h3 id="pydyna.pydyna_7_2_3.Rudder.dem_angle">dem_angle</h3>

Property (float): Rudder demanded angle (counter-clockwise radians)
<h3 id="pydyna.pydyna_7_2_3.Rudder.eff_angle">eff_angle</h3>

Property (float): Rudder effective angle (counter-clockwise radians)
<h3 id="pydyna.pydyna_7_2_3.Rudder.id">id</h3>

Property (string): Rudder identification
<h3 id="pydyna.pydyna_7_2_3.Rudder.max_angle">max_angle</h3>

Property (float): Rudder maximum angle (counter-clockwise radians)
<h3 id="pydyna.pydyna_7_2_3.Rudder.thisown">thisown</h3>

The membership flag
<h2 id="pydyna.pydyna_7_2_3.Thruster">Thruster</h2>

```python
Thruster(self, *args, **kwargs)
```
Models the hidrodynamics of a propeller attached to a ``Vessel``.
<h3 id="pydyna.pydyna_7_2_3.Thruster.calc_rot_dynamics">calc_rot_dynamics</h3>

Property (bool): True if the rotation dynamics is to be calculated or False if it's calculated elsewhere
<h3 id="pydyna.pydyna_7_2_3.Thruster.dem_angle">dem_angle</h3>

Property (float): Thruster demanded azimuthal angle (counter-clockwise radians)
<h3 id="pydyna.pydyna_7_2_3.Thruster.dem_pitch">dem_pitch</h3>

Property (float): Thruster demanded pitch (adimensional)
<h3 id="pydyna.pydyna_7_2_3.Thruster.dem_power">dem_power</h3>

Property (float): Thruster demanded power (kW)
<h3 id="pydyna.pydyna_7_2_3.Thruster.dem_rotation">dem_rotation</h3>

Property (float): Thruster demanded rotation (RPS)
<h3 id="pydyna.pydyna_7_2_3.Thruster.dem_thrust">dem_thrust</h3>

Property (float): Thruster demanded thrust (kN)
<h3 id="pydyna.pydyna_7_2_3.Thruster.eff_angle">eff_angle</h3>

Property (float): Thruster effective azimuthal angle (counter-clockwise radians)
<h3 id="pydyna.pydyna_7_2_3.Thruster.eff_pitch">eff_pitch</h3>

Property (float): Thruster effective pitch (adimensional)
<h3 id="pydyna.pydyna_7_2_3.Thruster.eff_power">eff_power</h3>

Property (float): Thruster effective power (kW)
<h3 id="pydyna.pydyna_7_2_3.Thruster.eff_rotation">eff_rotation</h3>

Property (float): Thruster effective rotation (RPS)
<h3 id="pydyna.pydyna_7_2_3.Thruster.eff_thrust">eff_thrust</h3>

Property (float): Thruster effective thrust (kN)
<h3 id="pydyna.pydyna_7_2_3.Thruster.id">id</h3>

Property (string): Thruster identification
<h3 id="pydyna.pydyna_7_2_3.Thruster.max_angle">max_angle</h3>

Property (float):  Thruster maximum azimuthal angle (counter-clockwise radians)
<h3 id="pydyna.pydyna_7_2_3.Thruster.max_pitch">max_pitch</h3>

Property (float): Thruster maximum pitch (adimensional)
<h3 id="pydyna.pydyna_7_2_3.Thruster.max_power">max_power</h3>

Property (float): Thruster maximum power (kW)
<h3 id="pydyna.pydyna_7_2_3.Thruster.max_rotation">max_rotation</h3>

Property (float): Thruster maximum rotation (RPS)
<h3 id="pydyna.pydyna_7_2_3.Thruster.max_thrust">max_thrust</h3>

Property (float): Thruster maximum thrust (kN)
<h3 id="pydyna.pydyna_7_2_3.Thruster.thisown">thisown</h3>

The membership flag
<h3 id="pydyna.pydyna_7_2_3.Thruster.torque">torque</h3>

Property (float):  Thruster torque (kNm)
<h3 id="pydyna.pydyna_7_2_3.Thruster.vessel">vessel</h3>

Parent vessel -> Vessel
<h3 id="pydyna.pydyna_7_2_3.Thruster.water_velocity">water_velocity</h3>

Property (float[3]): Water velocity in the local system of reference (m/s)
<h2 id="pydyna.pydyna_7_2_3.Anchor">Anchor</h2>

```python
Anchor(self, *args, **kwargs)
```
Models the hydrodynamics of an anchor in a ``Vessel``.
<h3 id="pydyna.pydyna_7_2_3.Anchor.active">active</h3>

Property (bool): Anchor activation state
<h3 id="pydyna.pydyna_7_2_3.Anchor.chain_max_length">chain_max_length</h3>

Property (float): Anchor maximum chain length (m)
<h3 id="pydyna.pydyna_7_2_3.Anchor.depth">depth</h3>

Property (float): Anchor depth (m)
<h3 id="pydyna.pydyna_7_2_3.Anchor.holding_power">holding_power</h3>

Property (float): Anchor holding power (kN)
<h3 id="pydyna.pydyna_7_2_3.Anchor.id">id</h3>

Property (string): Anchor identification
<h3 id="pydyna.pydyna_7_2_3.Anchor.thisown">thisown</h3>

The membership flag
<h3 id="pydyna.pydyna_7_2_3.Anchor.weight">weight</h3>

Property (float):  Anchor weight (kN)
<h3 id="pydyna.pydyna_7_2_3.Anchor.winch_brake_capacity">winch_brake_capacity</h3>

Property (float): Anchor winch brake capacity (kN)
<h3 id="pydyna.pydyna_7_2_3.Anchor.winch_lift_capacity">winch_lift_capacity</h3>

Property (float): Anchor winch lift capacity (kN)
<h3 id="pydyna.pydyna_7_2_3.Anchor.winch_speed">winch_speed</h3>

Property (float): Anchor dropping (negative values) or raising (positive values) winch speed (m/s)
<h2 id="pydyna.pydyna_7_2_3.Force">Force</h2>

```python
Force(self, *args, **kwargs)
```
Models the application of a force to a ``Vessel``.
<h3 id="pydyna.pydyna_7_2_3.Force.force">force</h3>

Property (float[3]): Force vector (kN)
<h3 id="pydyna.pydyna_7_2_3.Force.id">id</h3>

Property (string): Force identification
<h3 id="pydyna.pydyna_7_2_3.Force.moment">moment</h3>

Property (float[3]): Force moment (kN)
<h3 id="pydyna.pydyna_7_2_3.Force.point">point</h3>

Property (float[3]): Force point of reference (local position with reference to the vessel Wamit center)
<h3 id="pydyna.pydyna_7_2_3.Force.thisown">thisown</h3>

The membership flag
<h2 id="pydyna.pydyna_7_2_3.Endpoint">Endpoint</h2>

```python
Endpoint(self, *args, **kwargs)
```
Models a point of interaction with a ``Vessel``.
<h3 id="pydyna.pydyna_7_2_3.Endpoint.force">force</h3>

Property (Force): Reference to the Force at the end of this interaction Endpoint (cannot be None)
<h3 id="pydyna.pydyna_7_2_3.Endpoint.position">position</h3>

Property (float[3]): Position of this interaction Endpoint in the global frame of reference (m)
<h3 id="pydyna.pydyna_7_2_3.Endpoint.thisown">thisown</h3>

The membership flag
<h3 id="pydyna.pydyna_7_2_3.Endpoint.velocity">velocity</h3>

Property (float[3]):  Velocity of this interaction Endpoint in the global frame of reference (m/s)
<h3 id="pydyna.pydyna_7_2_3.Endpoint.vessel">vessel</h3>

Property (Vessel): Reference to the Vessel at the end of this interaction Endpoint (can be None)
<h2 id="pydyna.pydyna_7_2_3.Catenary">Catenary</h2>

```python
Catenary(self, *args, **kwargs)
```
Models the hydrodynamics of a catenary line connected to a ``Vessel(s)``.
<h3 id="pydyna.pydyna_7_2_3.Catenary.active">active</h3>

Property (bool): Line activation state
<h3 id="pydyna.pydyna_7_2_3.Catenary.endpoint_a">endpoint_a</h3>

Property (Endpoint): Interaction endpoint A
<h3 id="pydyna.pydyna_7_2_3.Catenary.endpoint_b">endpoint_b</h3>

Property (Endpoint): Interaction endpoint B
<h3 id="pydyna.pydyna_7_2_3.Catenary.id">id</h3>

Property (string): Catenary identification
<h3 id="pydyna.pydyna_7_2_3.Catenary.length">length</h3>

Property (float): Line length
<h3 id="pydyna.pydyna_7_2_3.Catenary.thisown">thisown</h3>

The membership flag
<h2 id="pydyna.pydyna_7_2_3.Fender">Fender</h2>

```python
Fender(self, *args, **kwargs)
```
Models the hydrodynamics of a fender acting on a ``Vessel``.
<h3 id="pydyna.pydyna_7_2_3.Fender.active">active</h3>

Property (bool): Fender activation state
<h3 id="pydyna.pydyna_7_2_3.Fender.endpoint_a">endpoint_a</h3>

Property (Endpoint): Interaction endpoint A
<h3 id="pydyna.pydyna_7_2_3.Fender.endpoint_b">endpoint_b</h3>

Property (Endpoint): Interaction endpoint B
<h3 id="pydyna.pydyna_7_2_3.Fender.id">id</h3>

Property (string): Fender identification
<h3 id="pydyna.pydyna_7_2_3.Fender.length">length</h3>

Property (float): Line length
<h3 id="pydyna.pydyna_7_2_3.Fender.thisown">thisown</h3>

The membership flag
<h2 id="pydyna.pydyna_7_2_3.Wind">Wind</h2>

```python
Wind(self, *args, **kwargs)
```
Models the dynamics of an environment wind which acts on the ``Vessel(s)`` being simulated.
<h3 id="pydyna.pydyna_7_2_3.Wind.spectrum_angle">spectrum_angle</h3>

Property (float): Wind spectrum angle parameter (counter-clockwise radians)
<h3 id="pydyna.pydyna_7_2_3.Wind.spectrum_type">spectrum_type</h3>

Property (string): Wind spectrum type

Can be one of the following values:
  "HARRIS",
  "WILLS",
  "REGULAR",
  "API",
  "NPD",
  "OCHISHIN",
  "DAVENPORT",
  "QUEUFFEULOU" or
  "KAIMAL"

<h3 id="pydyna.pydyna_7_2_3.Wind.spectrum_velocity">spectrum_velocity</h3>

Property (float): Wind spectrum velocity parameter (m/s)
<h3 id="pydyna.pydyna_7_2_3.Wind.thisown">thisown</h3>

The membership flag
<h3 id="pydyna.pydyna_7_2_3.Wind.get_velocity">get_velocity</h3>

```python
Wind.get_velocity(self, t, in_vec)
```

Evaluates the wind velocity at time t and position (x, y, z).

__Parameters__

- __``t`` (float) __: the time (t)
- __``pos`` (float[3])__: the position in global coordinates (m)

__Returns__

```float[3]`` `: global velocity (m/s)

<h2 id="pydyna.pydyna_7_2_3.Current">Current</h2>

```python
Current(self, *args, **kwargs)
```
Models the dynamics of a water current which acts on the ``Vessel(s)`` being simulated.
<h3 id="pydyna.pydyna_7_2_3.Current.field_axis_x">field_axis_x</h3>

Property(float[n]) : position x-component (m) of the current field

<h3 id="pydyna.pydyna_7_2_3.Current.field_axis_y">field_axis_y</h3>

Property(float[m]) :  position y-component (m) of the current field

<h3 id="pydyna.pydyna_7_2_3.Current.field_velocity_x">field_velocity_x</h3>

Property(float[n*m]) : velocity x-component (m/s) of the current field

<h3 id="pydyna.pydyna_7_2_3.Current.field_velocity_y">field_velocity_y</h3>

Property(float[n*m]) : velocity y-component (m/s) of the current field

<h3 id="pydyna.pydyna_7_2_3.Current.gain">gain</h3>

Property (float): Multiplier for the velocity (adimensional)
<h3 id="pydyna.pydyna_7_2_3.Current.profile_angle">profile_angle</h3>

Property(float[n]) : angle (rad) of the corresponding profile depths

<h3 id="pydyna.pydyna_7_2_3.Current.profile_depth">profile_depth</h3>

Property(float[n]) : depth values (m) of the current profile

<h3 id="pydyna.pydyna_7_2_3.Current.profile_velocity">profile_velocity</h3>

Property(float[n]) : velocity (m/s) of the corresponding profile depths

<h3 id="pydyna.pydyna_7_2_3.Current.thisown">thisown</h3>

The membership flag
<h3 id="pydyna.pydyna_7_2_3.Current.get_velocity">get_velocity</h3>

```python
Current.get_velocity(self, t, in_vec)
```

Evaluates the current velocity at time t and position (x, y, z).

__Parameters__

- __``t`` (float) __: the time (s)
- __``pos`` (float[3])__: the position in global coordinates (m)

__Returns__

```float[3]`` `: global velocity (m/s)

<h2 id="pydyna.pydyna_7_2_3.Wave">Wave</h2>

```python
Wave(self, *args, **kwargs)
```
Models the dynamics of a wave in the water which acts on the ``Vessel(s)`` being simulated.
<h3 id="pydyna.pydyna_7_2_3.Wave.field_angle">field_angle</h3>

Property(float[n*m]) : angles (rad) of the wave field

<h3 id="pydyna.pydyna_7_2_3.Wave.field_axis_x">field_axis_x</h3>

Property(float[n]) : position x-component (m) of the wave field

<h3 id="pydyna.pydyna_7_2_3.Wave.field_axis_y">field_axis_y</h3>

Property(float[m]) :  position y-component (m) of the wave field

<h3 id="pydyna.pydyna_7_2_3.Wave.field_multiplier">field_multiplier</h3>

Property(float[n*m]) : multipliers (adimensional) of the wave field

<h3 id="pydyna.pydyna_7_2_3.Wave.thisown">thisown</h3>

The membership flag
<h3 id="pydyna.pydyna_7_2_3.Wave.get_height">get_height</h3>

```python
Wave.get_height(self, t, in_vec)
```

Evaluates the wave height at time t and position (x, y).

__Parameters__

- __``t`` (float) __: the time (s)
- __``pos`` (float[2])__: the position in global coordinates (m)

__Returns__

```float`` `: the wave height (m)

<h2 id="pydyna.pydyna_7_2_3.create_text_report">create_text_report</h2>

```python
create_text_report(filename)
```

Creates a text-based ``Report``.

__Parameters__

- __``filename`` (string) __: the report filename to be written

__Returns__

 ``Report``

<h2 id="pydyna.pydyna_7_2_3.destroy_report">destroy_report</h2>

```python
destroy_report(report)
```

Finishes a ``Report`` printing.

__Parameters__

- __``report`` (Report) __: the report instance to destroy

<h2 id="pydyna.pydyna_7_2_3.Report">Report</h2>

```python
Report(self, *args, **kwargs)
```
Main class to create a text report. See ``create_report()`` and ``destroy_report()" functions.
<h3 id="pydyna.pydyna_7_2_3.Report.filename">filename</h3>

Report filename -> string
<h3 id="pydyna.pydyna_7_2_3.Report.thisown">thisown</h3>

The membership flag
<h3 id="pydyna.pydyna_7_2_3.Report.write">write</h3>

```python
Report.write(self, *args)
```

*Overload 1:*
 Prints ``Vessel`` data (including rudders, thrusters, forces) for time t.

__Parameters__

- __``t`` (float) __: the time (s)
- __``e`` (Vessel) __: the vessel instance with its subobjects to be printed

|

- __*Overload 2__:*
 Prints ``Catenary`` line data for time t.

__Parameters__

- __``t`` (float) __: the time (s)
- __``e`` (Catenary) __: the line instance with its subobjects to be printed

|

- __*Overload 3__:*
 Prints ``Fender`` data for time t.

__Parameters__

- __``t`` (float) __: the time (s)
- __``e`` (Fender) __: the line instance with its subobjects to be printed

<h2 id="pydyna.pydyna_7_2_3.get_version">get_version</h2>

```python
get_version()
```

Retrives the API version.

__Returns__

 ``string``

