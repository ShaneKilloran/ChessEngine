#imports
import random
class Node:
    def __init__(self, board,move, value):
        self.board = board
        self.move = move
        self.value = value
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def show(self):
        print(f"Board: {self.board}  Move: {self.move}  Val: {self.value}  Children: {self.children}")
        print()

    def peek_path(self):
        i = 1
        node = self
        while 1:
            print(f"Move {i}: {node.move} ")
            if not node.children:
                return

            ran = random.choice(node.children)
            node = node.children[ran]
            i += 1
