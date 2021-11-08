#**********************  LeeAndrewC_CSCI1470_Prog5  *********************
#
# Name: Andrew Lee
#
# Course: CSCI 1470.01
#
# Assignment: Program #5
#
# Algorithm(or a brief purpose of the assignment):
#   def a function for each of the five operations that returns the answer for each operation
#   start the exam loop that will keep giving exams until the user tells it to stop
#   for each question in the exam, get two random ints and a random operation
#   take a user answer and compare it to the answer returned by the operation function
#   store the user score and display it at the end of the exam
#   ask the user if they want to do another exam
#
#**********************************************************
from random import seed
from random import randint

takeExam = 'y'
seed()
operations = ["+", "-", "*", "/", "%"]

# adds two numbers
def sum_addition(num1, num2):
    userAnswer = int(input("\t{0} + {1} = ".format(num1, num2)))
    if (userAnswer == (num1 + num2)):
        print("Correct Answer")
        return 1
    else:
        print("Incorect Answer")
        return 0
# subtracts num2 from num1
def sum_subtraction(num1, num2):
    userAnswer = int(input("\t{0} - {1} = ".format(num1, num2)))
    if (userAnswer == (num1 - num2)):
        print("Correct Answer")
        return 1
    else:
        print("Incorect Answer")
        return 0
# multiplies two numbers
def product(num1, num2):
    userAnswer = int(input("\t{0} * {1} = ".format(num1, num2)))
    if (userAnswer == (num1 * num2)):
        print("Correct Answer")
        return 1
    else:
        print("Incorect Answer")
        return 0
# integer divides num1 by num2
def quotient(num1, num2):
    userAnswer = int(input("\t{0} / {1} = ".format(num1, num2)))
    if (userAnswer == (num1 // num2)):
        print("Correct Answer")
        return 1
    else:
        print("Incorect Answer")
        return 0
# integer remainder num1 by num2
def modulo(num1, num2):
    userAnswer = int(input("\t{0} % {1} = ".format(num1, num2)))
    if (userAnswer == (num1 % num2)):
        print("Correct Answer")
        return 1
    else:
        print("Incorect Answer")
        return 0

while takeExam == 'y':
    score = 0
    for x in range(1, 11):
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        operation = randint(0, 4)
        print("Question {}: ".format(x))
        if operations[operation] == "+":
            score += sum_addition(num1, num2)
        elif operations[operation] == "-":
            score += sum_subtraction(num1, num2)
        elif operations[operation] == "*":
            score += product(num1, num2)
        elif operations[operation] == "/":
            score += quotient(num1, num2)
        elif operations[operation] == "%":
            score += modulo(num1, num2)
        else:
            answer = -1
            print("ERROR, Operation not selected")

    print("You successfully completed the exam!")
    print("You scored a {}%!".format(score*10))
    print()

    takeExam = input("Enter y to take another exam, enter n to stop: ")