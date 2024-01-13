import os

def clear():
    if os.name == 'nt': os.system("cls")
    else: os.system("clear")


def menu(title: str, params: list):
    bars(size=50)
    print(f"{title:^50}")
    bars(size=50)
    for index, value in enumerate(params):
        print(f"[{index}] - {value}")
    bars(size=50)

def get_input(msg: str):
    r =  input(msg)
    bars(size=50)
    return r

def print_table(data, columns: list, title: str):
    bars()
    print(f"{title:^150}")
    bars()
    for row in data:
        for ind, col in enumerate(columns): print(f"{col}: {row[ind]:<25}", end=" | ")
        print("\n")
    bars()

def bars(size = 150):
    print("-"*size)