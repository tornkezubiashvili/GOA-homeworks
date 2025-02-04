x = int(input("Enter num: "))

def numbers(num):
    if num > 0:
        print("შედეგი:" + str(num) + "დადებითია")
    elif num == 0:
        print("შედეგი:" + str(num) + "ტოლია 0")
    else:
        print("შედეგი: " + str(num) + "უარყოფითია")


numbers(x)