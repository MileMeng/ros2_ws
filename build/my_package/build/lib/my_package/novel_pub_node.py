import rclpy
from rclpy.node import Node
import requests
from example_interfaces.msg import String
from queue import Queue

class NovelPublisher(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info(f'{node_name},启动！')
        self.novels_queue = Queue()
        self.novel_publisher_ = self.create_publisher(String, 'novel', 10)
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        if self.novels_queue._qsize()>0:
            line = self.novels_queue.get()
            msg = String()
            msg.data = line
            self.novel_publisher_.publish(msg)
            self.get_logger().info(f"发布了: {msg}")

    def download_novel(self, url):
        response = requests.get(url)
        response.encoding = 'utf-8'
        text = response.text
        self.get_logger().info(f"从 {url} 下载了小说，长度为 {len(text)}")
        for line in text.splitlines():
            self.novels_queue.put(line)


def main():
    rclpy.init()
    node = NovelPublisher("novel_publisher")
    node.download_novel("https://www.gutenberg.org/files/11/11-0.txt")  # Example URL for "Pride and Prejudice"
    rclpy.spin(node)
    rclpy.shutdown()