import pytest
import numpy as np

from util.connect_four import ConnectFour

# Test board initialization
def test_board_initialization():
    game = ConnectFour()
    assert (game.player_one_board == np.zeros((6,7))).all()
    assert (game.player_two_board == np.zeros((6,7))).all()

# Test state detection (win via horizontal, vertical, and diagonals)
@pytest.skip("Awaiting Implementation")
@pytest.mark.parametrize("board, expected_res", [[]])
def test_state_detection(board, expected_res):
    pass

# Test move selection (Legal and illegal)
@pytest.skip("Awaiting Implementation")
@pytest.mark.parametrize("board, move, expected_cond", [[]])
def test_move_selection(board, move, expected_res):
    pass