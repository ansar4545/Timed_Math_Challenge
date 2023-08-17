import random 
import time

OPERATORS = ["+", "-", "*"]
MIN_VALUE = 3
MAX_VALUE = 12
TOTAL_QUESTIONS = 5

def problem_generator():
    left = random.randint(MIN_VALUE,MAX_VALUE)
    right = random.randint(MIN_VALUE,MAX_VALUE)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)

    return expr,answer

wrong = 0
input("press Enter to start!!")
print("----------------------")

start_time = time.time()
for _ in range(TOTAL_QUESTIONS):
    expr,answer = problem_generator()
    while True:
        guess = input(f"problem #{_+1} : {expr} = " )
        if guess == str(answer):
            break
        wrong = wrong + 1

end_time = time.time()
total_time = round(end_time - start_time,2)

print("-------------------")

print("Good Work!! You have finished the quiz in ",total_time,"seconds")
print(f"your accuracy is {100-wrong}%")