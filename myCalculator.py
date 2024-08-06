class calc():
    def add(number_1, number_2):
        print( number_1+number_2)
    
    def sub(number_1, number_2):
        print (number_1-number_2)
    
    def multi(number_1,number_2):
        print (number_1*number_2)
    
    def div(number_1, number_2):
        if number_2 == 0:
            print("your second number is 0, division rule not allow that")
        else:
            number = (number_1/number_2)
            print (number)