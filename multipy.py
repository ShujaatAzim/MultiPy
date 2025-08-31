print("===      MultiPy         ===")
print("===   By Shujaat Azim    ===")
print("\n")

requested_int = int(input("Enter an integer between 1 and 10: "))
print("\n")

while requested_int > 10 or requested_int < 1:
    requested_int = int(input("Please enter an integer between 1 and 10: "))
    
for x in range(1, requested_int + 1):
  row = ""
  for y in range(1, requested_int + 1):
    row = row + str(x * y) + "\t"
  print(row)