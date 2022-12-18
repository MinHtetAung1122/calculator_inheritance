class Calculate:
    def __init__(self,input1,input2):
        self.input1 = input1
        self.input2 = input2 
    def plus (self):
        return self.input1 + self.input2
    def minus (self):
        return self.input1 - self.input2
    def devision (self):
        return self.input1 / self.input2
    def multiple (self):
        return self.input1 * self.input2

while True:
    num1 = int(input("pls enter a number : "))
    num2 = int(input("pls enter a number : "))

    x = Calculate(num1,num2)

    print(" 1 = plus , 2 = minus , 3 = multiply , 4 = divdie")
    operator =int(input())

    if operator == 1 :
        result = x.plus()
        print(f"{num1} plus {num2} is {result}")

    elif operator ==2 :
        result = x.minus()
        print(f"{num1} minus {num2} is {result}")
    elif operator == 3 :
        result = x.multiple()
        print(f"{num1} multiply {num2} is {result}")
    elif operator == 4 :
        result = x.devision()
        print(f"{num1} devided {num2} is {result}")

    next_calculation = input ("do u want to go next(yes or no) :  ").lower()
    if next_calculation == "no" :
        print ("bye")
        break
    else :
        print("invalid input")