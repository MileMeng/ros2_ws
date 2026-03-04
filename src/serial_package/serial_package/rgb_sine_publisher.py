#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import math
import time

class RGBSinePublisher(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info(f'{node_name} 启动！')
        self.publisher_ = self.create_publisher(Int32MultiArray, 'rgb_wave', 10)
        self.start_time = time.time()
        self.timer = self.create_timer(0.01, self.timer_callback)  # 10 Hz

    def timer_callback(self):
        t = time.time() - self.start_time
        r = int(127.5 * math.sin(2.0 * t) + 127.5)
        g = int(127.5 * math.sin(2.3 * t + 1.0) + 127.5)
        b = int(127.5 * math.sin(2.7 * t + 2.0) + 127.5)
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        msg = Int32MultiArray()
        msg.data = [r, g, b]
        self.publisher_.publish(msg)
        self.get_logger().info(f"{msg.data}")

def main():
    rclpy.init()
    node = RGBSinePublisher("rgb_sine_publisher")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()