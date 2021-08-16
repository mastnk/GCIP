print( 'Enter your ID: ', end='' )
txt = input().strip()
print()

ascii = [ ord(t) for t in txt ]
s = sum(ascii) % 256
print( 'Your code:', s )
