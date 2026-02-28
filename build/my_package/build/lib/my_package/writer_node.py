from my_package.my_node import PersonNode
import rclpy
class WriterNode(PersonNode):
    def __init__(self, name: str, age: int, book: str, food: str) -> None:
        super().__init__(name, age)  # 初始化父类，准备调用
        self.book = book
        self.food = food
        # print(f'{self.name} is eating {food}, age {self.age}, writing {self.book}')
        self.get_logger().info(f'{self.name} is eating {self.food}, age {self.age}, writing {self.book}')


def main():
    rclpy.init()
    writer = WriterNode("Alice", 35, "My Life Story", "pizza")
    writer.eat("pizza")
    rclpy.spin(writer)
    rclpy.shutdown()
