fruitFile = open('fruits.txt', 'r')
#import the fruit.txt file into python
content = fruitFile.readlines()
#read the content of the file

print(content)

fruitFile.close()
#close the file to allow any changes to be applied

#removes the nextline in from the list
contentRemove = [item.rstrip('\n') for item in content]
print(contentRemove)
#prints the lenghts of the content
for items in contentRemove:
    print(len(items))
