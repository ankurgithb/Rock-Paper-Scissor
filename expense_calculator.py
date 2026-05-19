import pandas as pd #type:ignore 

data = [ ]

print("Enter your data below, Type 'stop' to exit:- ")

while True:

    name = input("Enter the name: ")

    if name.lower() == 'stop':
        break

    category = input("Enter the category: ")
    amount = int(input("Enter the amount: "))

    data.append({
        "Name" : name,
        "Category": category,
        "Amount": amount
    })

    df = pd.DataFrame(data)

print("Current Expenses :-")
print(df)
total = df["Amount"].sum()
print("Total Spent = ", total)