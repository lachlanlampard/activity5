# colours to help distinguish if letter was changed
class bcolors:
    GREEN = '\033[92m'
    WHITE = '\033[0m'

# ex1_text
ex1_text = "fc hoh, fow ct grgxqdfcsz zocsz? nxg qoa ixgg dfct ixcjnq sczfd? wg nxg pbnsscsz do fnrg n pnxdq nd kfnxbcg't pbnkg. dfg cjgn ct do hxcsz wfnd qoa wnsd do gnd nsj znlgt dfnd qoa wnsd do pbnq. nsj fnrg n bod oi ias dozgdfgx! iggb ixgg do csrcdg loxg pgopbg. fopg do tgg qoa dfgxg! kfggxt, nbckg"

# ex2_text
ex2_text = "evfsgm aj vgfjicf oekf mrvud qqzvea"

# ex_1 letter replacement map
ex1_alphabet = {
	'k' : 'c',
	'f' : 'h',
	'g' : 'e',
	'x' : 'r',
	't' : 's',
	'd' : 't',
	'c' : 'i',
	'q' : 'y',
	'o' : 'o',
	'a' : 'u',
	'n' : 'a',
	'b' : 'l',
	'j' : 'd',
	'r' : 'v',
	's' : 'n',
	'z' : 'g',
	'i' : 'f',
	'l' : 'm',
	'h' : 'b',
	'w' : 'w',
	'p' : 'p',
}

def monoalpha_cipher(new_alphabet, ex1_text):
	for letter in ex1_text:
		new_letter = new_alphabet.get(letter)
		if new_letter:
			print(bcolors.GREEN + new_letter, end = '')
		else:
			print(bcolors.WHITE + letter, end = '')

def shift(s, n):
     return ''.join(chr((ord(char) - 97 - n) % 26 + 97) for char in s)

def poly_alphabetic(ex2_text):
	count = 0
	for letter in ex2_text:
		if letter.isalpha():
			count +=1
			if count % 4 == 1:
				new_letter = shift(letter, 4)
				print(new_letter, end = '')
			if count % 4 == 2:
				new_letter = shift(letter, 2)
				print(new_letter, end = '')
			if count % 4 == 3:	
				new_letter = shift(letter, 12)
				print(new_letter, end = '')
			if count % 4 == 0:
				new_letter = shift(letter, 18)
				print(new_letter, end = '')
		else:
			print(letter, end = '')

print('EXERCISE 1')
monoalpha_cipher(ex1_alphabet, ex1_text)
print(' ')
print(bcolors.WHITE)
print('EXERCISE 2')
poly_alphabetic(ex2_text)
print(' ')


