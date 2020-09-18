class Move:
	faces = "UDLRFB"

	def __init__(self, face, modifier):
		if face in Move.faces and type(modifier) is int:
			if modifier == 0:
				self.face = None
			else:
				self.face = face
			self.modifier = modifier % 4
		else:
			self.face = None
			self.modifier = None

	def name(self):
		if self.modifier == 0:
			return ""
		elif self.modifier == 1:
			concat = ""
		elif self.modifier == 2:
			concat = "2"
		elif self.modifier == 3:
			concat = "'"
		else:
			return None
		return self.face + concat

	def faceopposite(self):
		return Move.opposite(self.face)

	@classmethod
	def opposite(cls, face):
		if face == "L":
			return "R"
		elif face == "R":
			return "L"
		elif face == "U":
			return "D"
		elif face == "D":
			return "U"
		elif face == "F":
			return "B"
		elif face == "B":
			return "F"
		else:
			return None

	@classmethod
	def cancel(cls, move1, move2):
		if move1.face == move2.face:
			return Move(move1.face, move1.modifier + move2.modifier)
		else:
			return Move(None, None)