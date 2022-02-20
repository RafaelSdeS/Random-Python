import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
}

def arithmetic_arranger(x, y = False):

# Variables 
    n1 = 0
    t1 = ""
    t2 = ""
    space = ""
    tres = ""
    i = 0
    length1 = 0
    length2 = 0
    lengthS = 0



    while i < len(x):
        if len(x) >= 6:
             print("Error: Too many problems.")
             break
             
        else:
            part = x[i]
            splited = part.split()
    
            n1 = splited[0]
            op = splited[1]
            n2 = splited[2]

            try:
                float(n1)
                float(n2)
            except:
                print("Error: Numbers must only contain digits.")
                break
            else:
                try:
                 res  = ops[op](int(n1),int(n2))
                except KeyError:
                 print("Error: Operator must be '+' or '-'.")
                 break
                else:
                 res  = ops[op](int(n1),int(n2))
                 lengthr = len(str(res))

                 if len(n1) > 4 or len(n2)>4:
                     print("Error: Numbers cannot be more than four digits.")
                     break
                 else:

#Regulating the length of the spaces between numbers so that they are in line when printed
                  if len(n1) > len(n2): length1 = len(n1) - len(n2)
                  else: 
                      length1 = 0

                  if len(n1) == len(n2): 
                     length1 = 0
                     length2 = 0

                  if len(n1) < len(n2): length2 = len(n2) - len(n1)
                  else:
                      length2 = 0

                  if len(n1)>= len(n2): lengthS = len(n1)
                  if len(n1) <= len(n2): lengthS = len(n2)

#The template of the print
                  t1 +=  (6 + length2)*" " + n1
                  t2 += (4)*" " + op + " " + n2
                  space += 4*" " + (2 + lengthS)*"-"
                  tres += (6 + lengthS - lengthr)*" " + str(res)
    
                  i += 1

    print(t1)
    print(t2)
    print(space)    
    if(y):
     print(tres)

arithmetic_arranger(['32 + 8', "50 - 51", "1000 - 5000", "1 - 10", "5 + 11"])
