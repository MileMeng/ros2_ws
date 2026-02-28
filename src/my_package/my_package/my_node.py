import rclpy
from rclpy.node import Node

class PersonNode(Node):
    def __init__(self, name: str, age: int) -> None:
        super().__init__('node_123')
        self.name = name
        self.age = age
        print('PersonNode _init_ 方法被调用')

    def eat(self, food: str):
        """ 
        This method allows the person to eat a specific type of food.
        """
        # print(f'{self.name} is eating {food}.')
        self.get_logger().info(f'{self.name} is eating {food}.')

def main():
    rclpy.init()
    node = PersonNode("John", 30)
    node.eat('apple')
    rclpy.spin(node)
    rclpy.shutdown()

