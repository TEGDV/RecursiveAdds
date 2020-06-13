def recursiveAdd(result):
    
    number = int(input('add a number:   '))
    result += number
    print(result)
    if input('do you wish to add other number? y/n      ') == 'y':
        result = recursiveAdd(result)
    
    return result    
    





if __name__ == "__main__":
    try:
        print('the final result is :   {}'.format(recursiveAdd(0)))
    except:
        print('Ocurrio un error')

        
 
        