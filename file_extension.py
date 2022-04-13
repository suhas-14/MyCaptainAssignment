#file extension

file_name = input("Enter the filename: ")

exten = file_name.split('.')

print("The extension of the file name is: ", exten[-1:])