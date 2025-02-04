x = int(input("Enter your age: "))

def age(num):
    if num >= 18:
        print("შენი ასაკი: " +str(num) + "სრულწლოვანიხართ")
    else:
        print("შენი ასაკი: " + str(num) + "არ ხართ სრულწლოვანი")    

age(x)