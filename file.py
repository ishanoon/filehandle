wordsfile = open('names.txt','r')
# open method allows you to import files in python
content = wordsfile.read()
#the read method allows you to read an imported file in python
print(content)

#seek method allows you to begin at the brginning of the file rather than where you have executes to
wordsfile.seek(0)
#readlines method allows you to print the content of the in a list
contentlist = wordsfile.readlines()

print(contentlist)

#the rstrip method allow you to remove elements you dont want from your file 
contentRemove = [item.rstrip('\n') for item in contentlist]

print(contentRemove)
#without the close methods you changes to the file content would not be save
wordsfile.close()