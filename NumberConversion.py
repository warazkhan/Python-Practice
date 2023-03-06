#Given an integer,n, print the following values for each integer i from 1 to n :

#Decimal
#Octal
#Hexadecimal (capitalized)
#Binary


def print_formatted(number):
    spaceLength = len(str(bin(number))[2:])

    for i in range(1,number+1):

        print(str(i).rjust(spaceLength,' '),str(oct(i)[2:]).rjust(spaceLength,' '),str(hex(i)[2:]).upper().rjust(spaceLength,' '),str(bin(i)[2:]).rjust(spaceLength,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)