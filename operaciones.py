  

def suma (a, b):
    return (a+b)

if __name__=="__main__":

    print(suma(2,8))


def resta (a, b):
    return (a-b)

if __name__=="__main__":
    print(resta(9,2))




def multi (a, b):
        return (a*b)

if __name__=="__main__":
    print(multi(10,5))
    


def division (a, b,aceptado):
    
    try:
        if a == 0 and not aceptado :
        
         print("No se puede dividir entre 0")
    except ValueError:
            print("Va perfecto")    
        
            return (a/b)
    
    
if __name__=="__main__":
    print(division(12,6))
     

   
   