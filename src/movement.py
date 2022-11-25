import rclpy
from rclpy.node import Node
import time 
import numpy as np
import math
from geometry_msgs.msgs import Twist


class Trajectory_publisher(Node):

    def __init__(self):
        super().__init__('robot_control_node')
        self.vel.pub = self.create_publisher(Twist, 'cmd_vel',10)
        self.cmd = Twist()


    def timer_callback(self):
        bazu_trajectory_msg = JointTrajectory()
        bazu_trajectory_msg.joint_names = self.joints
        
        cmd.linear.x = 0.8
        cmd.angular.z=0.0
        vel_pub.publish(self.cmd)
    
        rclpy.spin_once(self)

def main(args=None):
    rclpy.init(args=args)
    
    rc_object = RobotControl()
    rclpy.spin(rc_object)
    joint_trajectory_object.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
