1 python type of data always store inside memory(m/m refrence )but  not in the variable i.e a ka andar int ya string dta hai na ki a ka string or int hai

2 exception hwn we are working with number and string in garabge collection it will not work fast so it late garbage collection

why this 
Ctrl click to launch VS Code Native REPL
>>> l1=[1,2,3]
>>> l2=l1
>>> l1="chai"
>>> l2
[1, 2, 3]
>>> l1=[1,2,3]
>>> l2
[1, 2, 3]
>>> l1[0]=33
>>> l2
[1, 2, 3]
>>> l1
[33, 2, 3]
>>> 


whyThis?
>>> l1=[1,23]
>>> l1=[1,2,3]
>>> l2=l1
>>> l2
[1, 2, 3]
>>> l1
[1, 2, 3]
>>> l1[0]=44
>>> l1
[44, 2, 3]
>>> l2
[44, 2, 3]

why this
>>> h1=[1,2,3]
>>> h2=h1[:] //copy bn rhi hai
>>> h1[0]=11
>>> h1
[11, 2, 3]
>>> h2
[1, 2, 3]
>>> 


why this

>>> m=[1,2,3]
>>> n=m
>>> m==n
True
>>> m is n
True
>>> n=[1,2,3]
>>> m is n
False
>>> m == n
True
>>> 