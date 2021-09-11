import re
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

lst = ['000', '001', '010', '011', '100', '101', '110', '111']
my_dic_0 = {}
my_dic_1 = {}
for comb in lst:
    my_dic_0[comb] = len(re.findall(f'(?={comb}0)', string))
    my_dic_1[comb] = len(re.findall(f'(?={comb}1)', string))
for i in my_dic_0:
    print("{}: {},{}".format(i, my_dic_0[i], my_dic_1[i]))
