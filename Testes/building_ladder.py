def ladder(h, d):

    h = int(h)
    tmp = 1

    for i in range(h):
        for j in range(tmp):
            print(d, end= ' ')
        print("")
        tmp += 1

def main():

    height, digit = input("Give a height value and a type of digit: ").split()

    ladder(height, digit)

if __name__ == "__main__":
    main()