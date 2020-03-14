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
	_TOWERS_MARGIN = 1  # distance between towers

	class Layer:
		"""One level of tower"""
		def __init__(self, width: int = 1, pos: int = 0):
			self._width = width
			self.pos = pos

		@property
		def width(self):
			return self._width

		def __str__(self):
			w = self._width
			return f'[{" "*w}||{" "*w}]'

		def __lt__(self, right: 'Layer') -> bool:
			return self._width < right.width

		def __eq__(self, right: int) -> bool:
			return self._width == right

	def __init__(
		self,
		max_level: int = 3,
		towers: List[List[int]] = None,
		solved: bool = False
	):
		assert max_level > 0, f'Illegal number of levels ({max_level})'
		self._max_level = max_level
		self._towers = [[0 for _ in range(self._max_level)] 
							for _ in range(State._TOWERS_COUNT)]
		if towers is not None:
			layers = set(layer for tower in towers for layer in tower)
			assert layers == set(range(1, self._max_level + 1)), \
				f'Illegal layers: {layers}'
			for tower_idx, tower in enumerate(towers):
				for width_idx, width in enumerate(sorted(tower, reverse=True)):
					width_idx = self._max_level - width_idx - 1  # going backwards
					self._towers[tower_idx][width_idx] = State.Layer(width)
		else:
			for idx in range(self._max_level):
				if solved:  # populate only last tower
					self._towers[-1][idx] = State.Layer(idx)
				else:  # populate only first tower
					self._towers[0][idx] = State.Layer(idx)

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
		for level in range(self._max_level):
			for tower in range(State._TOWERS_COUNT):
				item = self._towers[tower][level]
				output += f'{str(item) if item else "||":^{tower_space}}'
			output += '\n'
		output += '=' * tower_space * State._TOWERS_COUNT
		return output

	def move(self, src: int, dst: int) -> None:
		"""Moves top level from src to dst
		:param src: where to pick from
		:param dst: where to place at
		"""
		self._towers[src]

def main():
	obj1 = State()
	print(obj1)
	print(State(solved=True))
	print(State(max_level=5))
	print(State(max_level=3, towers=[[2, 1], [3], []]))
	print(State(max_level=6, towers=[[5, 3, 6, 4, 1, 2], [], []]))
	

if __name__ == '__main__':
	main()
