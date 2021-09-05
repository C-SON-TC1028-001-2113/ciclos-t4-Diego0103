def main():
    #escribe tu código abajo de esta línea
    height = int(input("Enter triangle height: "))
    for i in range(height+1):
        if i>0:
            print(" "*(height-i)+"*"*(i))


if __name__=='__main__':
    main()
