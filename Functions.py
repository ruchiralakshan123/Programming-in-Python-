#Function definition
def my_function():
    print("Hello from a function")
#Function invocation    
my_function()

#Empty Functions
def empty_func():
   pass
empty_func()

#Positional Arguments
def calc(qty, item, price):
      print("The "+ item + " cost/s" , (qty*price), "rupees")
calc(2,'Apples', 20,50)

#Keyword Arguments
def calc(qty, item, price):
      print("The "+ item + " cost/s", (qty*price), "rupees")
calc(qty=5, item="Oranges",price=10)

#  Default Parameters
def greet(name, msg="How are you?"):
   print(name + ", " + msg)
greet("John")
greet("John", "Good Evening")
greet("Good Evening")


#Arbitrary Arguments
def add(*args):
    #sum() is an inbuilt function to sum up a list
    total=(sum(args))
    print("The sum : " ,total)
def greet(msg, *names):
    for name in names:
        print(msg + ", " + name)
#Calling add() function
add(1,4,5)
#Calling greet() function
greet("Hello","John","Maggie","Lucy")


#The return Statement
def totalPrice(quantity, price):
  """
  This function return a single value; The total price
  """
  return quantity*price


def getItemDetails():
  """
  getItemDetails function return three values: a Tuple of (stock, name, price). 
  but you can receive them as three separate results as well.
  """
  return 15,"Bread",80.00
  
  
def showItemDetails(quantity,name,price,total):
  """
  showItemDetails function returns nothing; It displays the details in screen. 
  So the return statement is optional
  """
  print("Qty: {} Item: {} Unit Price: {} Total Price: {}".format(quantity,name,price,total))
#Receiving returning result as a Tuple
#details = getItemDetails()
#print (details)
#Receiving returning result as separaet results
stock, itemName , price = getItemDetails()
quantity = 10
total = totalPrice(quantity,price)
showItemDetails(quantity,itemName,price,total)


#Docstrings
def calc(quantity, price):
    """Returns the product of quantity and price"""
    return quantity*price
print (calc.__doc__)