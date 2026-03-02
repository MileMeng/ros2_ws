import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import serial
import threading
import queue
import time


class RGBSerialSubscriber(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info(f'{node_name} 启动！')

        # 串口配置（根据你实际设备修改）
        self.ser = serial.Serial(
            port='/dev/ttyACM0',
            baudrate=921600,
            timeout=0.01
        )

        self.queue = queue.Queue()

        self.subscription = self.create_subscription(
            String,
            'rgb_wave',
            self.rgb_callback,
            10
        )

        self.tx_thread = threading.Thread(target=self.serial_send_thread, daemon=True)
        self.tx_thread.start()

    def rgb_callback(self, msg):
        self.queue.put(msg.data)

    def serial_send_thread(self):
        while rclpy.ok():
            if not self.queue.empty():
                data = self.queue.get()
                self.ser.write((data + '\n').encode())
                self.get_logger().info(f"{data}")
            else:
                time.sleep(0.01)


def main():
    rclpy.init()
    node = RGBSerialSubscriber("rgb_serial_subscriber")
    rclpy.spin(node)
    rclpy.shutdown()
