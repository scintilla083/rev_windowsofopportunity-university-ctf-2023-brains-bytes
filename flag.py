arr = [156, 150, 189, 175, 147, 195, 148, 96, 162, 209, 194, 207, 156, 163, 166, 104, 148, 193, 215, 172, 150, 147, 147, 214, 168, 159, 210, 148, 167, 214, 143, 160, 163, 161, 163, 86, 158]
flag = ['H']

i = 0
while i < len(arr):
	nxt = arr[i] - ord(flag[i])
	flag.append(chr(nxt))
	flag_str = ''.join(map(str, flag))
	print(flag_str)
	i+=1
