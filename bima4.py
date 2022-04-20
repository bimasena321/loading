import time

simpan = '='
bima = 0

for x in range(101):
	time.sleep(0.2)
	print(f'\rTunggu {x}% [{simpan}]', end='',flush = True)
	bima += 1
	if bima == 3:
		bima = 0
		simpan += '='
print('\nselesai:)')