#მომხმარებელს შეეკითხეთ რიცხვი შემდეგ შექმენით ფუნქცია რომელსაც ექნება პარამეტრი რომელსაც არგუმენტად გადაეცემა მომხლარებლის შემოტანილი რიცხვი შემდეგ კი თუ 18 ზე უთხრას რომ სრულწლოვანია თუარადა არარის
x = int(input("Enter your age: "))

def age(num):
    if num >= 18:
        print("შენი ასაკი: " +str(num) + "სრულწლოვანიხართ")
    else:
        print("შენი ასაკი: " + str(num) + "არ ხართ სრულწლოვანი")    

age(x)