import numpy as np

##### desing those values #####
W = [0,0]
b = 0
##### desing those values #####

c = [+1, -1, -1, -1]
x = np.zeros( (2,4), dtype=np.int32 )

x[0,0] = +1 #x1
x[1,0] = +1 #x2

x[0,1] = +1 #x1
x[1,1] = -1 #x2

x[0,2] = -1 #x1
x[1,2] = +1 #x2

x[0,3] = -1 #x1
x[1,3] = -1 #x2

W = np.asarray(W)
y = np.sign( np.dot( W, x ) + b ).astype(np.int32)

for i in range(4):
    line = ''
    if( c[i] == y[i] ):
        line += 'OK: '
    else:
        line += 'NG: '

    line += '({:+d},{:+d}) -> {:+d} [{:+d}]'.format( x[0,i], x[1,i], y[i], c[i] )
    print( line )


