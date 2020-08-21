# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_book = {}

for i in range(0,n):
    line = input()
    name = line.strip().split()[0]
    ph_no = line.strip().split()[1]
    phone_book[name] = ph_no

while True:
    try:
        query = input()
        if query in phone_book:
            print(f"{query}={phone_book.get(query)}")
        else:
            print("Not found")
    except:
        break

