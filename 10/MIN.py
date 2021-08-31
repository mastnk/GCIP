import numpy as np

W1 = np.zeros( (3,3) )
b1 = np.zeros( (3,1) )

W2 = np.zeros( (3,3) )
b2 = np.zeros( (3,1) )

##### desing those values #####
W1[0,0] = 0; W1[0,1] = 0; W1[0,2] = 0;
W1[1,0] = 0; W1[1,1] = 0; W1[1,2] = 0;
W1[2,0] = 0; W1[2,1] = 0; W1[2,2] = 0;

b1[0,0] = 0;
b1[1,0] = 0;
b1[2,0] = 0;

W2[0,0] = 0; W2[0,1] = 0; W2[0,2] = 0;
W2[1,0] = 0; W2[1,1] = 0; W2[1,2] = 0;
W2[2,0] = 0; W2[2,1] = 0; W2[2,2] = 0;

b2[0,0] = 0;
b2[1,0] = 0;
b2[2,0] = 0;
##### desing those values #####

x = np.random.rand( 3,1 )

c = np.asarray( [-1,-1,-1], dtype=np.int32 ).reshape( (3,1) )
c[np.argmin(x)] = +1

y = np.sign( np.dot( W1, x ) + b1 ).astype(np.int32)
z = np.sign( np.dot( W2, y ) + b2 ).astype(np.int32)

print( 'x:', x.transpose() )
print( 'y:', y.transpose() )
print( 'z:', z.transpose() )
print( 'c:', c.transpose() )

if( np.all( z==c ) ):
    print('OK')
else:
    print('NG')
