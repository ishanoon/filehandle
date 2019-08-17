file = open('brands.txt', 'w')
# the parameter 'w' in the open method allows you to write into a non exiting file

file.write('Python \n')
file.write('Java \n')
file.write('Javascript')
#the write method allow for writing to the new file created in python

file.close()