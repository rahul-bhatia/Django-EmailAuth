from random import randrange

pw=""
text="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*!@#$%^()-_>.,<?/|}[{]~`"

for i in range(8):
	pw+=text[randrange(len(text))]
	print(pw)

print("Final password :",pw)