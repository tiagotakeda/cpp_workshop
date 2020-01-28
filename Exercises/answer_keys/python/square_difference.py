import math

def sqrdif(r):

    larger_area = r*r*2*2
    smaller_area = math.sqrt(2)*math.sqrt(2)*r*r
    return larger_area - smaller_area

def main():

    radius = int(input("Give the radius of the circle: "))
    print("The difference of the areas of the squares is:", sqrdif(radius))

if __name__ == "__main__":
    main()