def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n*100

#This code breaks our ability to import enlarge from other files,
#
# #print('Hello")
# y = int(input("Please choose a number: "))
# print(y, enlarge(y))

if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print("HELLO")
    y = int(input("Please choose a number"))
    print(y, enlarge(y))