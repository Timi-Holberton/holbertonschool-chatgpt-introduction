#!/usr/bin/python3
import sys

def factorial(n):
	"""
	factorial - Calcule de manière récursive la factorielle d'un entier
	non négatif n. La factorielle de 0 est 1 par convention.

	@n: Entier non négatif dont on veut calculer la factorielle. Si n = 0,
	la fonction retourne 1.

	Return: La factorielle de n (n!), un entier positif.
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
