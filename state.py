"""Contains class for towers' state tracking.
Block refers to a single part of a single tower;
Tower refers to a stack of blocks;
Width refers to a block width;
Height refers to a maximum count of blocks in all towers,
"""
from typing import List, Optional


Matrix = List[List[int]]


class State:
    """State of game."""
    _TOWERS_COUNT = 3
    _TOWERS_MARGIN = 2  # distance between towers

    def __init__(
            self,
            height: int = 1,
            state_matrix: Matrix = None,
            solved: bool = False
        ):
        """Create state of tower
        :param height: count of blocks of tower
        :param state_matrix: height * _TOWERS_COUNT matrix with size of blocks
            if now specified, matrix will be created using height value
        :param solved: if True matrix and no state_matrix specified,
            state_matrix will be created as already solved
        """
        assert height > 0, f'Illegal number of levels ({height})'
        self._height = height
        if state_matrix is not None:
            blocks = set(item for row in state_matrix for item in row)
            assert blocks == set(range(self._height + 1)), \
                f'Invalid state matrix: {state_matrix}'  # set of blocks inconsistent
            assert all(list(col) == sorted(col) for col in zip(*state_matrix)), \
                f'Invalid state matrix: {state_matrix}'  # matrix is not sorted vertically
            assert sum(1 for row in state_matrix for item in row if item) == self._height, \
                f'Invalid state matrix: {state_matrix}'  # count of blocks inconsistent
            self._state_matrix = state_matrix
        else:  # build state with one tower
            tower_idx = State._TOWERS_COUNT - 1 if solved else 0  # if solved populate last tower
            self._state_matrix = []
            for row in range(self._height):
                level = []
                for col in range(State._TOWERS_COUNT):
                    level.append(row + 1 if col == tower_idx else 0)
                self._state_matrix.append(level)
                
    @property
    def state_matrix(self):
        return self._state_matrix

    @property
    def height(self):
        return self._height

    def __str__(self):
        """State representation
        Sample output for State():
           [||]        ||         ||     
          [ || ]       ||         ||     
         [  ||  ]      ||         ||     
        =================================
        """
        output = ''
        tower_space = State._TOWERS_MARGIN + self._height * 2 + 4
        for row in self._state_matrix:
            for block in row:
                layer = f'[{" "*block}||{" "*block}]' if block else '||'
                output += f'{layer:^{tower_space}}'
            output += '\n'
        output += '=' * tower_space * State._TOWERS_COUNT
        return output

    def __eq__(self, right) -> bool:
        return self._state_matrix == right.state_matrix

    @staticmethod
    def _transpose(matrix: Matrix) -> Matrix:
        """Transpose matrix. Intended to use in self.move
        :param matrix: matrix to be transposed (intentionally state_matrix)
        :return: transposed matrix
        """
        return [list(col) for col in zip(*matrix)]

    @staticmethod
    def _first_nonzero(array: List[int]) -> Optional[int]:
        """Returns index of first nonzero element in array
        :param array: target array
        :return: index or None if all elements are zero
        """
        for idx, value in enumerate(array):
            if value:
                return idx

    def move(self, src: int, dst: int) -> 'State':
        """Moves top level from src to dst
        :param src: index of source column
        :param dst: index of destination column
        """
        columns = self._transpose(self._state_matrix)
        src_top = self._first_nonzero(columns[src])
        dst_top = self._first_nonzero(columns[dst])
        if src_top is None:
            raise RuntimeError('Source is empty')
        if dst_top and columns[src][src_top] > columns[dst][dst_top]:
            raise RuntimeError('Wrong move')
        if dst_top is None:
            dst_top = len(columns[dst])
        columns[dst][dst_top - 1] = columns[src][src_top]  # move block on top of dst
        columns[src][src_top] = 0  # remove block from top of src
        self._state_matrix = self._transpose(columns)
        return self


def main():
    state = State(height=5)
    print(state)
    state.move(0, 1)
    state.move(0, 2)
    state.move(1, 2)
    print(state)


if __name__ == '__main__':
    main()
