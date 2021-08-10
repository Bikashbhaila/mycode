#!/usr/bin/env python3
import argparse

parser_m = argparse.ArgumentParser(description="Enter name and day")

acc_adj = ["John Doe", "Jane Doe", "Monday", "Tuesday", "Wednesday"]

parser_m.add_argument("adj", choices=acc_adj, help="Word for name and day")

parser_m.add_argument("-a", metavar="ADVERB", default="--",help="Helper words like this, that, etc.")
angle_parseer = parser_m.parse_args()

print(f"You name is {angle_parseer.a} and its {angle_parseer.adj}")

# name_input = input("What is your name? ").strip()
# day_input = input("Please enter day of the week: ").strip()

# input_str = "Hello, " + name_input + "!" + " Happy " + day_input +"!"
# print(input_str)

# print("Hello,", name_input, "!", "Happy", day_input, "!")
