def find_number(arg):
   numeros = []
   for x in arg:
       if(x.isnumeric()):
           numeros.append(int(x))
   valor = int(str(numeros[0]) + str(numeros[-1]))
   numeros.clear()
   return int(valor)

def change_word_to_num(arg):
    word_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    new_word = arg
    
    for idx, num in enumerate(word_nums, 1):
        if((new_word.find(num,0)) >= 0):
            new_word = new_word.replace(num, str(idx))
            
    valor = find_number(new_word) 
    #f.write(str(valor))
    #f.write("\n")
    return valor

total = 0
list1 = open("day1.txt", "r")
#f = open("prueba.txt", "w")

for element in list1:
    total += change_word_to_num(element) 
print(total)
#f.close()