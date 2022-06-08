import symbolicManipulation as sm 
import numpy as np 


expr1 =   sm.expression( [-1,0,1,2,-3], ['xyxy', 'a','b',  'y' , 'z' ] )
expr2 =   sm.expression( [4, 1, 2, 3, 10], ['xyxy', 'c','w',  'y' , '' ] )

expr3 =   sm.expression( [1,1] , ['x', 'a'] )
expr4 =   sm.expression( [1,1] , ['y', 'b'] )


print ('Expression 1: ',  expr1  ) 
print ('Expression 2: ',  expr2 ) 

print( 'Add expression 1 and expression 2 : ' , expr1.add(expr2) ) 

tempdict = {'x':1, 'y':2, 'a':10, 'b':0, 'y':10, 'z':1} ; 
print( 'Using: ', tempdict, ' Evaluate expression 1: ' , expr1.evaluate( tempdict  )  ) 


print( ) 
print( 'Multiply (a+x)(b+y) = ' , expr3.multiply(expr4) ) 

