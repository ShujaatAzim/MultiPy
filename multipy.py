#!/usr/bin/env python3

print("=========       MultiPy        =========")
print("=========    By Shujaat Azim   =========")
print("\n")

requested_int = input("Enter an integer between 1 and 10: ")

while not requested_int.isdigit() or int(requested_int) > 10 or int(requested_int) < 1:
    requested_int = input("Please enter an integer between 1 and 10: ")
    
print("\n")

for x in range(1, int(requested_int) + 1):
  row = ""
  for y in range(1, int(requested_int) + 1):
    row = row + str(x * y) + "\t"
  print(row)

print("\n")