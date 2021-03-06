# test the pattern matching of Python new feature
# tutorial: https://www.python.org/dev/peps/pep-0636

# use v 3.10.0a6

x = 10

match x:
  case 5:
    print('match 5')
    
  case 10:
    print('got 10')
  
  case _:
    print('default')
    
    
# test structure

x = [2,3]

print(x)
match x:
  case [2,3]:
    print ("case [2,3]")
  
  case (2,3):
    print ("case (2,3)")
  
  case _:
    print('not match')
    
    
# match will extract info
# _ is wildcard

match x:
  case [x1, x2]:
    print('match', x1 , x2)
  case _:
    print ('not')


# [1,2,3,4] match [x1, x2]??
x = [1,2,3,4]
match x:
  case [x1, x2]:
    print('match', x1 , x2)
  case _:
    print ('not')
    
    
# extract many values
match x:
  case [x1, *x2]:
    print('*x2 match', x2)

# tupple to array 
x = (1, 100)
match x:
  case [x1, x2]:
    print('match', x1 , x2)
  case _:
    print ('not')
    
    
# capturing a sub pattern
x = ['go', 'north']

print ('-- or pattern  --  ("north" | "south" | "east" | "west")')
match x:
  case ["go", ("north" | "south" | "east" | "west")]:
    print('match ok')
    
print ('-- capture sub pattern')
match x:  
 case ["go", ("north" | "south" | "east" | "west") as direction]:
   print('capture dirrection:', direction)