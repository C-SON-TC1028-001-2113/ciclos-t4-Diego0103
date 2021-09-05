def pares(num1,num2):
    if num1<num2 and num1%2==0:
        for i in range(num1,num2+1,2):
            print(i)
    elif num1<num2 and num1%2!=0:
        for i in range(num1+1,num2+1,2):
            print(i)
    elif num1>num2 and num2%2==0:
        for i in range(num2,num1+1,2):
            print(i)
    elif num1>num2 and num2%2!=0:
        for i in range(num2+1,num1+1,2):
            print(i)
            

def main():
    valor1=int(input("Valor 1: "))
    valor2=int(input("Valor 2: "))
    if valor1==valor2 and valor1%2!=0:
        print("No hay pares")
    elif valor1>0 and valor2>0:
        pares(valor1,valor2)
    

if __name__=='__main__':
    main()
