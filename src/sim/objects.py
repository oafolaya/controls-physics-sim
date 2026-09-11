from abc import ABC, abstractmethod
import numpy as np

class PointMass():
    def __init__(self, mass=10.0, position = [0.0, 0.0, 0.0], velocity = [0.0, 0.0, 0.0], restitution = 0.6, radius = .1):
        self.mass = float(mass) 
        self.x_position = float(position[0])
        self.y_position = float(position[1])
        self.z_position = float(position[2])
        self.x_velocity = float(velocity[0])
        self.y_velocity = float(velocity[1])
        self.z_velocity = float(velocity[2])
        self.x_angular_position = float(0)
        self.y_angular_position = float(0)
        self.z_angular_position = float(0)
        self.x_angular_velocity = float(0)
        self.y_angular_velocity = float(0)
        self.z_angular_velocity = float(0)
        self.moment_of_inertia = float(0)

        self.accumulated_force = np.array([0.0, 0.0, 0.0])
        self.target_position = None
        self.restitution = float(restitution)
        self.radius = float(radius)
        
    def get_state(self): # form state vector
        state = np.array([self.x_position, 
                        self.y_position, 
                        self.z_position,  
                        self.x_velocity, 
                        self.y_velocity, 
                        self.z_velocity])
        state = np.array(state).reshape([len(state), 1])
        return state
    
    def get_position(self):
        position = np.array([self.x_position, self.y_position, self.z_position])
        return position

    def get_velocity(self):
        velocity = np.array([self.x_velocity, self.y_velocity, self.z_velocity])
        return velocity

    def set_state(self, state): # state must be vector of size 6
        state = np.array(state, dtype=float)
        self.x_position = state.item(0)
        self.y_position = state.item(1)
        self.z_position = state.item(2)
        self.x_velocity = state.item(3)
        self.y_velocity = state.item(4)
        self.z_velocity = state.item(5)
    
    def set_position(self, position):
        position = np.array(position, dtype=float)
        self.x_position = position.item(0)
        self.y_position = position.item(1)
        self.z_position = position.item(2)
    
    def set_velocity(self, velocity):
        velocity = np.array(velocity, dtype=float)
        self.x_velocity = velocity.item(0)
        self.y_velocity = velocity.item(1)
        self.z_velocity = velocity.item(2)
        
    def get_mass(self):
        return self.mass
    
    def get_inverse_mass(self):
        return 1/self.mass
    
    def add_force(self, force):
        self.accumulated_force = self.accumulated_force + force
    
    def clear_forces(self):
        self.accumulated_force = np.array([0, 0, 0], dtype=float)

    def set_target_position(self, target_position):
        target_position = np.array(target_position, dtype=float)
        self.target_position = target_position
    
    def set_restitution(self, restitution):
        self.restitution = float(restitution)

    def set_radius(self, radius):
        self.radius = float(radius)


class RigidBody():
    def __init__(self, mass=10,moment_of_inertia=10, position = [0, 0, 0],
                velocity = [0, 0, 0], angular_position = [0,0,0],
                angular_velocity = [0, 0, 0], restitution = 0.6):
        self.accumulated_force = np.array([0, 0, 0], dtype=float)
        self.accumulated_torque = np.array([0, 0, 0], dtype=float)
        self.mass = float(mass)
        self.x_position = float(position[0])
        self.y_position = float(position[1])
        self.z_position = float(position[2])
        self.x_velocity = float(velocity[0])
        self.y_velocity = float(velocity[1])
        self.z_velocity = float(velocity[2])
        self.x_angular_position = float(angular_position[0])
        self.y_angular_position = float(angular_position[1])
        self.z_angular_position = float(angular_position[2])
        self.x_angular_velocity = float(angular_velocity[0])
        self.y_angular_velocity = float(angular_velocity[1])
        self.z_angular_velocity = float(angular_velocity[2])
        self.moment_of_inertia = float(moment_of_inertia)
        self.target_position = None
        self.target_angular_position = None
        self.restitution = float(restitution)


    def get_state(self): # form state vector
        state = np.array([self.x_position, 
                        self.y_position, 
                        self.z_position,  
                        self.x_velocity, 
                        self.y_velocity, 
                        self.z_velocity,
                        self.x_angular_position,
                        self.y_angular_position,
                        self.z_angular_position,
                        self.x_angular_velocity,
                        self.y_angular_velocity,
                        self.z_angular_velocity])
        state = np.array(state).reshape([len(state), 1])
        return state

    def set_state(self, state): # state must be vector of size 6
        state = np.array(state, dtype=float)
        self.x_position = state.item(0)
        self.y_position = state.item(1)
        self.z_position = state.item(2)
        self.x_velocity = state.item(3)
        self.y_velocity = state.item(4)
        self.z_velocity = state.item(5)
        self.x_angular_position = state.item(6)
        self.y_angular_position = state.item(7)
        self.z_angular_position = state.item(8)
        self.x_angular_velocity = state.item(9)
        self.y_angular_velocity = state.item(10)
        self.z_angular_velocity = state.item(11)

    def set_position(self, position):
        position = np.array(position, dtype=float)
        self.x_position = position.item(0)
        self.y_position = position.item(1)
        self.z_position = position.item(2)
    
    def set_velocity(self, velocity):
        velocity = np.array(velocity, dtype=float)
        self.x_velocity = velocity.item(0)
        self.y_velocity = velocity.item(1)
        self.z_velocity = velocity.item(2)

    def set_angular_position(self, angular_position):
        position = np.array(angular_position, dtype=float)
        self.x_position = position.item(0)
        self.y_position = position.item(1)
        self.z_position = position.item(2)
    
    def set_angular_velocity(self, angular_velocity):
        velocity = np.array(angular_velocity, dtype=float)
        self.x_velocity = velocity.item(0)
        self.y_velocity = velocity.item(1)
        self.z_velocity = velocity.item(2)
        
    def get_mass(self):
        return self.mass
    
    def get_inverse_mass(self):
        return 1/self.mass
    
    def get_inertia_inverse(self):
        return 1/self.moment_of_inertia
    
    def add_force(self, force):
        force = np.array(force, dtype=float)
        self.accumulated_force = self.accumulated_force + force
    
    def clear_force(self):
        self.accumulated_force = np.array([0, 0, 0])

    def add_torque(self, torque):
        torque = np.array(torque, dtype=float)
        self.accumulated_torque = self.accumulated_force + torque
    
    def clear_torque(self,):
        self.accumulated_torque = np.array([0, 0, 0], dtype=float)

    def set_target_position(self, target_position):
        target_position = np.array(target_position, dtype=float)
        self.target_position = target_position
    
    def set_restitution(self, restitution):
        self.restitution = float(restitution)