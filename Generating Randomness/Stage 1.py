string = ""

while len(string) < 100:
    user = input("Print a random string containing 0 or 1:\n\n")
    for s in user:
        if s == "0" or s == "1":
            string += s
    if len(string) < 100:
        print(f"Current data length is {len(string)}, {100 - len(string)} symbols left")
print("Final data string:")
print(string)

