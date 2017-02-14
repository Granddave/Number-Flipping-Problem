key = 67023
validNumbers = [0,1,2,5,6,8,9]
count = 0
answer = 0

# ex [1,2,3] -> [3,2,1]
def mirrorList(num):
    tempNum = [0,0,0,0,0]
    for i in range(1,6):
        tempNum[ 5 - i ] = num[i - 1]
    return tempNum

def checkIfRotatable(num):
    if (num == '3' or num == '4' or num == '7'):
        return 0
    else:
        return 1

def rotateOneNum(num):
    if (num == '6'):
        return '9'
    elif (num == '9'):
        return '6'
    else:
        return str(num)

# ex [8,5,1,0,6] -> [9,0,1,5,8]
def flipList(num):
    num = mirrorList(num)
    for i in range(0,5):
        if checkIfRotatable(num[i]) == 0:
            return 0
    for i in range(0,5):
        num[i] = rotateOneNum(num[i])
    return num

# Pad number n with zeros. Example: zeropad(7,3) == '007'
def zeropad(n,zeros=5):
    nstr = str(n)
    while len(nstr) < zeros:
        nstr = "0" + nstr
    return nstr

# checks if all items in list are unique
def allUnique(x):
    seen = list()
    return not any(i in seen or seen.append(i) for i in x)

# main function that check if a number meet the requirements
def check(number):
    global count
    global answer

    if not allUnique(str(number)):
        return

    num = list(zeropad(str(number)))
    newNum = [0,0,0,0,0]
    answer = [0,0,0,0,0]


    # Flips flippable numbers
    newNum = flipList(num)
    if (newNum == 0):
        return

    # Turn str list to int list
    num = [int(i) for i in num]
    newNum = [int(i) for i in newNum]

    # list to int
    num = int(''.join(map(str,num)))
    newNum = int(''.join(map(str,newNum)))

    answer = newNum - key

    if answer < 0:
        return

    count = count + 1


def main():
    for i in range(00000,100000):
        check(i)
        if answer == i:
            print("GOT IT! it's ", i)

    print ("Total valid numbers:", count)


if __name__ == '__main__':
	main()
