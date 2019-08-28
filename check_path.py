import pickle
import utils
from MiniMax import MiniMax
from Node import Node


pickle_in = open("root.pickle","rb")
root = pickle.load(pickle_in)

mm = MiniMax(root)
mm.minimax(root)
