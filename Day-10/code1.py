#finally clause

try:
    file = open("example.txt","r")
    #some kind of code to raise an exception

except FileNotFoundError:
    print("file not found!")

finally:
    file.close()
    print("file closed.")