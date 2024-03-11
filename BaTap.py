import array


def cau1():
    s = "Tran Minh Quan"
    print(s)


def cau2(begin, end):
    for i in range(begin, end):
        if i % 2 != 0:
            print(i)


def cau3a(begin, end):
    sum = 0
    for i in range(begin, end+1):
        sum += i
    print(sum)


def cau3b(begin, end):
    sum = 0
    for i in range(begin, end+1):
        sum += i
    print(sum)


def cau4a(mydict):
    for key in mydict.keys():
        print(key)


def cau4b(mydict):
    for values in mydict.values():
        print(values)


def cau4c(mydict):
    for key in mydict.keys():
        print("key: %s - values: %d" % (key, mydict[key]))


def cau5():
    courses = [131, 141, 142, 212]
    names = ["Maths", "Physics", "Chem", "Bio"]
    for i in range(0, len(courses)):
        print("%s - %d" % (names[i], courses[i]))


def cau6a():
    sum = 0
    s = "jabbawocky"
    nguyenam = ["u", "e", "o", "a", "i"]
    for i in range(0, len(s)):
        if s[i] not in nguyenam:
            sum += 1
    print(sum)


def cau6b():
    sum = 0
    s = "jabbawocky"
    nguyenam = ["u", "e", "o", "a", "i"]
    for i in range(0, len(s)):
        if s[i] in nguyenam:
            continue
        else:
            sum += 1
    print(sum)


def cau7():
    a = 10
    for i in range(-2, 3):
       try:
           print("%d / %d = %0.1f" % (a, i, (a / i)))
       except ZeroDivisionError:
           print("Can’t divided by zero")

if __name__ == "__main__":
    mydict = {
        "a": 1,
        "b":2,
        "c":3,
        "d":4
        }
    cau1()
    cau2(1, 10)
    print("Tong cac so tu 1 den 10:")
    cau3a(1, 10)
    print("Tong cac so tu 1 den 6:")
    cau3b(1, 5)
    print("Toan bo key trong mydict")
    cau4a(mydict)
    print("Toan bo values trong mydict")
    cau4b(mydict)
    print("Tat ca cac gia tri va khoa:")
    cau4c(mydict)
    print("Cac khoa hoc va mon hoc:")
    cau5()
    print(" Tong cac so phu am:")
    cau6a()
    print("Tong cac so phu am theo lenh tiep tuc:")
    cau6b()
    print(" Ket qua:")
    cau7()