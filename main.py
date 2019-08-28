import chess
import chess.svg
import utils
from Node import Node
import tqdm
import pickle

# initialize board state
board = chess.Board("3k4/2n2B2/1KP5/2B2p2/5b1p/7P/8/8 b - - 0 0")

# make game tree
rootVal = utils.evaluate_board(board)
root = Node(board,'root',rootVal)


print(board)

#TODO: Fix bug that adds infinite move loops.
def makeTree(node,n):
    legal_moves = node.board.legal_moves

    if n == 0:
        print("End of N")
        return

    for move in legal_moves:
        newBoard = node.board.copy()
        newBoard.push(move)
        newVal = utils.evaluate_board(newBoard)

        newNode = Node(newBoard, move, newVal)
        node.add_child(newNode)
        makeTree(newNode,n-1)


makeTree(root,4)
pickle_out = open("root.pickle","wb")
pickle.dump(root, pickle_out)
pickle_out.close()

root.peek_path()
