# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# lis=[i for i in range(1,20) if i%2]
# print(lis)
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 28],
    'Salary': [50000, 60000, 45000, 55000],
    'Department': ['HR', 'IT', 'Marketing', 'Finance']
})

df2 = pd.DataFrame({
    'Name': ['Bob', 'Charlie', 'David'],
    'Experience': [3, 5, 4]
})

m=pd.merge(df,df2)
print(m)