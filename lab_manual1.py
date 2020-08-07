#To check whether a string belongs to a given grammer or not

a = input("Enter string:")
n = len(a)

if (a[0]=="a" and (a[n-1]=="a" or a[n-1]=="b") and a[n-2]=="c"):
    for i in range(n-2):
        if(a[i]!="b"):
            print("\nString is not accepted")
            exit(0)
    print("String is accepted")
else:
    print("String is not accepted")
