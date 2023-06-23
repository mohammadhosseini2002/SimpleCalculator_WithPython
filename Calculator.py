#Create Simple Calculator With Python

User_Operator = input("Enter your Operator (+, -, *, /) --> ")

if User_Operator == "+":
    Plus_First_Number = int(input("Enter your First Number (Plus +) --> "))
    Plus_Second_Number = int(input("Enter your Second Number (Plus +) --> "))
    Plus_SUM = Plus_First_Number + Plus_Second_Number
    print("Plus Result --> " , Plus_SUM)