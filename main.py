from validator import isbn13
while True:
    print("Input ISBN-13 number: ")
    try:
        n = int(input())
        print(isbn13(n))
    except ValueError:
        print("Invalid")
