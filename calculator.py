#Simple calculator to practise python fundamentals
#user prompts and stores as float
operator = input('Choose an operator (+ - * /): ')
num1 = float(input('Enter the 1st number: '))
num2 = float(input('Enter the 2nd number: '))

#arthemic operations
if operator == '+':
    answer = num1 + num2

elif operator == '-':
    answer = num1 - num2

elif operator == '*':
    answer = num1 * num2

elif operator == '/':
    answer = num1 / num2

else:
    print(f'{operator} is not a valid operator. Please choose from the operators listed')

#display calculation
print(f"{num1} {operator} {num2} = {answer}")