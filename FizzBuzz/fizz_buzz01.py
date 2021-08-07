#!/usr/bin/env python3

def readFile():
    with open("numfile.txt", "r") as input_file:
        numlist = []
        for num in input_file:
            numlist.append(int(num))
        return numlist

def playGame(numlist):
    fizz, buzz, fizzbuzz = 0, 0, 0
    for num in numlist:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            fizzbuzz +=1
        elif num % 3 == 0:
            print("Fizz")
            fizz +=1
        elif num % 5 == 0:
            print("Buzz")
            fizzbuzz+=1
        else:
            print(num)
    return  "Fizzes: {fizz} Buzzes: {buzz} FizzBuzzes: {fizzbuzz}"

def main():
    playGame(readFile())


if __name__ == "__main__":
    main()
