print("hola mundo")
a = 5 + 2


def exportable_function():
    for i in range():
        print(i)
    return "hola mundo"


print("hello world")


def BracketCombinations(num):

  combos = getCombos(num)

  # code goes here
  return len(combos)


def getCombos(num, stri=""):
  if len(stri) >= num * 2:
    return [stri]
  
  combos = []

  if stri.count("(") < num:
    combos += getCombos(num, stri + "(")

  if stri.count(")") < stri.count("("):
    combos += getCombos(num, stri + ")")

  return combos

    
  

# keep this function call here 
print(BracketCombinations(input()))