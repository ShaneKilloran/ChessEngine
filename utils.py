#!/usr/bin/env python
import chess
import chess.svg
import numpy as np
import math

values = {
    "p": 1,
    "r": 5,
    "n": 3,
    "b": 3,
    "q": 9,
    "k": 0,
}

def get_pieces (pieceMap, colour):
    pieces = []
    for piece in pieceMap.values():
        if colour == 1 and piece.symbol().isupper():
            pieces.append(piece.symbol())
        elif colour == -1 and piece.symbol().islower():
            pieces.append(piece.symbol())

    return pieces



def total_value(pieceList):
    total = 0
    for piece in pieceList:
        piece = piece.lower()
        total += values[piece]
    return total

# normalize value of board
# -1 = black winning
#  1 = white winning
def sigmoid(x):
    sig = math.exp(-np.logaddexp(0, -x))
    return sig / 0.5 - 1



def evaluate_board(board):
    pieceMap = board.piece_map()
    listPiecesW = get_pieces(pieceMap, 1) # 1 = white
    listPiecesB = get_pieces(pieceMap, -1) # -1 = black

    # get value of white's pieceList
    whiteVal = total_value(listPiecesW)

    # get value of black's pieceList
    blackVal = total_value(listPiecesB)

    return sigmoid(whiteVal-blackVal)
