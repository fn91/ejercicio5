from fastapi import HTTPException

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
    


def division (a, b):
    
       
    if a==0:
       raise HTTPException(status_code=400, detail="Error no se puede dividir entre 0") 
    return (a/b)
    
    
if __name__=="__main__":
    print(division(12,6))
     

   
   