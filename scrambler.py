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
			moves = self.cancel(moves, new_move)
		
		move_string = " ".join([move.name() for move in moves])

		return move_string


	def cancel(self, moves, new_move):
		last_moves = []

		for move in moves:
			if last_moves == []:
				last_moves.append(move)
			elif last_moves[-1].face == move.faceopposite():
				last_moves.append(move)
			else:
				last_moves = [move]

		if len(last_moves) == 1:
			if new_move.face == last_moves[0].face:
				cancel_moves = Move.cancel(last_moves[0], new_move)
				if cancel_moves.modifier == 0:
					cancelled = []
				else:
					cancelled = [cancel_moves]
			else:
				cancelled = last_moves + [new_move]
		elif len(last_moves) == 2:
			if new_move.face == last_moves[0].face:
				cancel_moves = Move.cancel(last_moves[0], new_move)
				if cancel_moves.modifier == 0:
					cancelled = [last_moves[1]]
				else:
					cancelled = [cancel_moves, last_moves[1]]
			elif new_move.face == last_moves[1].face:
				cancel_moves = Move.cancel(last_moves[1], new_move)
				if cancel_moves.modifier == 0:
					cancelled = [last_moves[0]]
				else:
					cancelled = [last_moves[0], cancel_moves]
			else:
				cancelled = last_moves + [new_move]
		else:
			cancelled = last_moves + [new_move]



		return [moves[i] for i in range(len(moves) - len(last_moves))] + cancelled