elf = open("./babyrev",'rb').read()
flag = bytearray(32)
flag[27] = '1'
flag[28] = '5'
flag[29] = '9'

SHUFFLE = list(elf[0x3060:0x3080])
XOR = bytearray(elf[0x3080:0x30a0])
known_char = {
	27:'1',
	28:'5',
	29:'9'
}
while not all(flag):

	for i in known_char.keys():
		index = SHUFFLE.index(chr(i))
		flag[index] = known_char[i]
		del known_char[i]

		flag[index] = flag[index]^XOR[index]
		known_char[index] = flag[index]

print(flag)