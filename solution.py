import Fraction

def answer(pegs):
	n = len(pegs)

	if (not pegs) or n == 1:
		return [-1,-1]

	if n % 2 == 0:
		even = True
	else:
		even = False

	if even is True:
		sum = - pegs[0] + pegs[n - 1]

	else:
		sum = - pegs[0] - pegs[n -1]

	if n > 2:
		for i in xrange(1, n-1):
			sum += 2 * (-1) ** (i+1) * pegs[i]

	if even is True:
		x = Fraction(2 * (float(sum)/3))

	else:
		x = sum * 2

	if x < 2:
		return [-1,-1]

	r = x
	for i in xrange(0, n-2):
		d = pegs[i+1] - pegs[i]
		y = d - r

		if r < 1 or y < 1:
			return [-1,-1]

		else:
			r = y

	return [x.numerator, x.denominator]