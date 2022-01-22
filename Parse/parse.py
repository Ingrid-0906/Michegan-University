import urllib.request, urllib.parse, urllib.error

file = urllib.request.urlopen()

counts = dict()

for line in file:
	words = line.decode().split()
	counts[words] = counts.get(words, 0) + 1

print(counts)
