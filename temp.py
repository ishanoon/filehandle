temperatureFile = open('temperature.txt','w')

temperatures=[10,-20,-289,100]

def writer(temperatures):
    with open('temps.txt', 'w') as file:
        for temps in temperatures:
            if temps > -273.15:
                Feh = temps * 9/5 + 32
                file.write(str(Feh) + '\n')

writer(temperatures)




temperatureFile.close()