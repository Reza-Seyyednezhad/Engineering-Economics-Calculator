from formulas import P_A, P_F, A_F, A_P, F_A, F_P, i_P_F, n_F_P

mylist = []

while True:
    user = str(input("enter values(P/F or F/P or A/F or ..., i, Start Year(n)), split with comma(,) and Do not write Parentheses: "))
    if user == "":
        break
    elif len(tuple(user.split(','))) > 3:
        continue
    else:
        if isinstance(user.split(',')[0], str) and isinstance(user.split(',')[1], (float, int)) and isinstance(user.split(',')[2], (float, int)):
            mylist.append(tuple(float(x) if x.isdigit() else str(x) for x in user.split(',') ))

f = open("./Note.txt", 'w')
f.writelines(mylist)
f.close()
# print(mylist)
Sum = 0
for item in mylist:
    method, i, startYear = item
    if method == "P/F":
        F_input = float(input("Enter F:"))
        Sum += F_input * P_F(i, startYear)[0]
    elif method == "F/P":
        P_input = float(input("Enter P:"))
        Sum += P_input * F_P(i, startYear)[0]
    elif method == "P/A":
        A_input = float(input("Enter A:"))
        Sum += A_input * P_A(i, startYear)[0]
    elif method == "A/P":
        P_input = float(input("Enter P:"))
        Sum += P_input * A_P(i, startYear)[0]
    elif method == "F/A":
        A_input = float(input("Enter A:"))
        Sum += A_input * F_A(i, startYear)[0]
    elif method == "A/F":
        F_input = float(input("Enter F:"))
        Sum += F_input * A_F(i, startYear)[0]
    else:
        continue

print(Sum)

