vowels=['a','i','o','u','e']
word = input("Enter your name you want to check:")
found=[]
for letter in word:
	if letter in vowels:
		if letter  not in found:
			found.append(letter)
for vowels in found:
	print(vowels)
