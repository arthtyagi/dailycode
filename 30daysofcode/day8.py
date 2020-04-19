##22.5 POINTS FOR THIS SOLUTION

if __name__=="__main__":
    n= int(input().strip())
    phoneBook={}
    for i in range(n):
        name, number = input().split()
        phoneBook[name]=number
    for i in range(n):
        S= input()
        if S in phoneBook.keys():
            print(f"{S}={phoneBook[S]}")
        else: print("Not found")
