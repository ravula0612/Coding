def hello():
    return "hi!!"
hello
# output: <function __main__.hello()>
hello()
# output: hi!!
######################################
def fun1(name = "Anil"):
    print("Started:\n")
    def greet():
        print("I am greet() \n")
    def welcome():
        print("I am welcome() \n")
    print(" excuitng fun1()\n") 
    if name=="Anil":
        return greet
    else:
        return welcome
he = fun1()
he()
## output
#Started:

 #excuitng fun1()

#I am greet()        
