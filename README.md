# Symbolic_Algebra

This is a package that preforms symbolic algebra manipulations using a dictionary. The key is an expression where as the coefficient is the value. For example, 3x^2y + 2 xy would be stored as dictionary { 'xxy': 3, 'xy': 2 } 


This class has the following methods: 
* init the expression &rarr; expression( list of coefficients, list of expressions as strings ) 
* copy &rarr; deep copy to a new instance of the expression 
* get_random_term &rarr; produces a random linear term 
* add &rarr; adds the two expressions together 
* subtract &rarr; subtracts second expression from the first expression 
* multiply &rarr; multiplies the two expressions together
* evaulate &rarr; calculates numerical result based on variable values 
* formatExpression &rarr; produces LaTeX output of current algebraic expression 
* simplifyRatio &rarr; simplify the ratio of two expressions. 


Overall, this class had been developed for the purposes of automating homework problem creation. The package here contains the main method and a file showing some examples of these methods. 
