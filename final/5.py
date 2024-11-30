
fr = int(input("from: "))
to = int(input("to: "))

if to < fr :
    print("incorrect values")
    exit(1)
while fr <= to:
    print(fr)
    fr += 1