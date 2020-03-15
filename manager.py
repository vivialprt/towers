"""Contains game cycle manager."""
import sys
from state import State


class Manager:
    """Solves towers' puzzle.
    """
    def __init__(self, height: int = 3):
        """
        :param height: height of tower
        """
        self._height = height
        self._state = State(max_level=height)
        self._solved_state = State(max_level=height, solved=True)

    def solve(self, verbose: bool = True) -> None:
        """Algorythm for solving
        :param verbose: if True prints every solving step
        """
        print(self._state)


def main():
    key = 'y'
    while key in'y':
        # TODO input check (bounds, 0, digits)
        n = int(input('Enter number of levels: '))
        game = Manager(height=n)
        game.solve()
        key = input('Play once again?[Y/n]: ').lower()
        while key not in 'yn':
            key = input('Play once again?[Y/n]: ').lower()
    print('Thanks for playing!')
    sys.exit(0)


if __name__ == '__main__':
    main()
