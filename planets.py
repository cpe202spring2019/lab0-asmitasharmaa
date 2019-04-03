#Asmita Sharma

def weight_on_planets():
    weight = input('What do you weigh on earth? ')
    print()
    
    w = int(weight)
    mars = 0.38 * w
    jupiter = 2.34 * w
    
    print('On Mars you would weigh', mars, 'pounds.\nOn Jupiter you would weigh', jupiter, 'pounds.')
    
   
if __name__ == '__main__':
   weight_on_planets()
