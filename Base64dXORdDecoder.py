key=''
enced=''
def xor_enc(string,key):
	res = ''
	for x in range(0,len(string)):
		res += chr(ord(string[x]) ^ ord(key[x%len(key)]))
	return res
dec = xor_enc(enced.decode('base64'),key)
print dec