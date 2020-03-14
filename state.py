"""Containes class for towers' state tracking.
Level refers to a single layer of a single tower;
Tower refers to a stack of layers;
Width refers to a layer width;
Height refers to a count of layers in tower;
Max level refers to a maximum count of layers in all towers,
i.e. count of layers in game.
"""
from typing import List


class State:
    """State of game."""
    _TOWERS_COUNT = 3
    _TOWERS_MARGIN = 2  # distance between towers

    def __init__(
            self,
            max_level: int = 3,
            state_matrix: List[List[int]] = None,
            solved: bool = False
        ):
        """Create state of tower
        :param max_level: count of blocks of tower
        :param state_matrix: max_level * _TOWERS_COUNT matrix with size of blocks
        if now specified, matrix will be created using max_level value
        :param solved: if True matrix and no state_matrix sqeified,
        state_matrix will be creted as already solved
        """
        assert max_level > 0, f'Illegal number of levels ({max_level})'
        self._max_level = max_level
        if state_matrix is not None:
            blocks = set(item for row in state_matrix for item in row)
            assert blocks == set(range(self._max_level + 1)), \
                f'Invalid state matrix: {state_matrix}'  # set of blocks inconsistent
            assert all(list(col) == sorted(col) for col in zip(*state_matrix)), \
                f'Invalid state matrix: {state_matrix}'  # matrix is not sorted vertically
            assert sum(1 for row in state_matrix for item in row if item) == self._max_level, \
                f'Invalid state matrix: {state_matrix}'  # count of blocks inconsistent
            self._state_matrix = state_matrix
        else:  # build state with one tower
            tower_idx = State._TOWERS_COUNT - 1 if solved else 0  # if solved populate last tower
            self._state_matrix = []
            for row in range(self._max_level):
                level = []
                for col in range(State._TOWERS_COUNT):
                    level.append(row + 1 if col == tower_idx else 0)
                self._state_matrix.append(level)
                
    def __str__(self):
        """State representation
        Sample output for State():
           [||]        ||         ||     
          [ || ]       ||         ||     
         [  ||  ]      ||         ||     
        =================================
        """
        output = ''
        tower_space = State._TOWERS_MARGIN + self._max_level * 2 + 4
        for row in self._state_matrix:
            for block in row:
                layer = f'[{" "*block}||{" "*block}]' if block else '||'
                output += f'{layer:^{tower_space}}'
            output += '\n'
        output += '=' * tower_space * State._TOWERS_COUNT
        return output

    def move(self, src: int, dst: int) -> None:
        """Moves top level from src to dst
        :param src: where to pick from
        :param dst: where to place at
        """
        pass

def main():
    obj1 = State()
    print(obj1)
    print(State(solved=True))
    print(State(max_level=5))
    print(State(
        max_level=3,
        state_matrix=[
            [0, 0, 0],
            [1, 0, 0],
            [3, 2, 0]]))


if __name__ == '__main__':
    main()
