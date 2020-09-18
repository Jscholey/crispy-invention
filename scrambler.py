import random
from move import Move

class Scrambler:
	def __init__(self):
		pass

	def create_scramble(self):
		moves = []
		for i in range(30):
			face = random.choice(Move.faces)
			modifier = random.randrange(1, 4)
			new_move = Move(face, modifier)
			moves.append(new_move)
		try:
			move_string = " ".join([move.name() for move in moves])
		except TypeError:
			move_string = "N/A"

		return move_string


	def can_cancel(self, moves, new_move):
		pass
