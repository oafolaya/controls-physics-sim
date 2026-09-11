# Simple Controls/Physics Simulation Framework in Pygame and Numpy
A modular physics and controls simulation framework built from scratch in Python using NuPy and Pygame.

The project was created to explore the mechanics of dynamic simulation, constraint solving, and feedback control rather than relying on an existing phsyics engine. The framework supports point-mass dynamics, numerical integration, feedback controllers, Jacobian-based constraints, collision boundaries, and real-time visualization. 

## Implemented Features
- Point Mass Object
- Basic 2D Rendering using Pygame
- PID Control
- Jacobian-based constraint solving
- Fixed Point Constraints
- Distance Constraints
- Baumgarte stabilization 
- Real-time visualization using Pygame
- Numerical integration of system dynamics
- PID/PD feedback control
- Static boundary collision constraints

## Example Simulations

## PD Position Control
A point mass is driven toward a target position using PD feedback control while the simulation handles force application, numerical integration, and visualization.

## Constrained Pendulum
Two point masses are connected using a distance constraint, with one mass fixed in space to create pendulum-like motion under gravity.

## Project Structure
The simulation framework separates the major components of the system into modules, including:
- Dynamic objects
- Controllers
- Numerical integrators
- Constraints
- Simulation/World logic
- Rendering

This structure enables experimentation with different controllers, physical systems, and constraints without rewriting the core simulation loop.

## Future Extensions
Possible future expansions include:
- Full rigid-body rotational dynamics
- Revolute and fixed joints with joint limits
- Articulated mechanism and robotic linkages
- Additional control algorithms
- Controller performance logging and metrics
- Improved camera and visualization tools


