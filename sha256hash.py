import hashlib
import sys


def sha256(filename):
	h = hashlib.sha256()
	with open(filename, 'rb') as file:
		chunk = 0
		while chunk != b'':
			chunk = file.read(1024)
			h.update(chunk)
	return h.hexdigest()


message = sha256(sys.argv[1])

with open(sys.argv[1] + ".txt", "w") as f:
	f.write(message)