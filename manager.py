"""Contains game cycle manager."""
import sys
try:
    from .state import State
except ModuleNotFoundError:
    from state import State


class Manager:
    """Solves towers' puzzle.
    """
    def __init__(self, upper_bound: int = 25):
        """
        :param upper_bound: max height of tower
        """
        self._upper_bound = upper_bound
        self._state = State()

    def start(self) -> None:
        """Start game."""
        key = 'y'
        while key in 'y':
            key = self._update()
        print('Thanks for playing!')

    def _update(self) -> str:
        """Performs game cycle."""
        height = 0
        while height <= 0 or height > self._upper_bound:
            try:
                height = int(input(f'Enter number of levels (1 to {self._upper_bound}): '))
            except ValueError:
                pass
        self._state = State(height)
        self.solve()
        key = input('Play once again?[Y/n]: ').lower()
        while key not in 'yn':
            key = input('Play once again?[Y/n]: ').lower()
        return key

    def solve(self, verbose: bool = True) -> None:
        """Algorithm for recursive solving
        :param verbose: if True prints every solving step
        """
        def move_tower(state: State, height: int, src: int = 0, dst: int = 2) -> State:
            if height == 1:  # recursion end condition
                state = state.move(src, dst)
                if verbose:
                    print(str(state))
                return state
            else:
                tmp = 3 - src - dst  # 3 is tower indexes sum
                state = move_tower(state, height - 1, src, tmp)
                state = state.move(src, dst)
                if verbose:
                    print(str(state))
                state = move_tower(state, height - 1, tmp, dst)
                return state

        self._state = move_tower(self._state, self._state.height)


def main():
    game = Manager()
    game.start()


if __name__ == '__main__':
    main()
