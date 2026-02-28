import espeakng
import rclpy
from rclpy.node import Node
import requests
from example_interfaces.msg import String
from queue import Queue
import threading
import time

class NovelSublisher(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info(f'{node_name},启动！')
        self.novels_queue = Queue()
        self.novel_subscription_ = self.create_subscription(String, 'novel', self.novel_callback, 10)
        self.speech_thread = threading.Thread(target=self.speak_thread)
        self.speech_thread.start()

    def novel_callback(self, msg):
        self.novels_queue.put(msg.data)


    def speak_thread(self):
        speaker = espeakng.Speaker()
        speaker.voice = 'en'
        while rclpy.ok(): # 检测当前ros上下文是否ok
            if not self.novels_queue.empty():
                text = self.novels_queue.get()
                self.get_logger().info(f"正在朗读: {text}")
                speaker.say(text) # 朗读
                speaker.wait() # 等待朗读完成
            else:
                time.sleep(1) #休眠1s

def main():
    rclpy.init()
    node = NovelSublisher("novel_subscriber")
    rclpy.spin(node)
    rclpy.shutdown()