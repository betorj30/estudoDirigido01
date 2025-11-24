def main():

    idade = int(input("Qual a sua idade? "))
    cidade = input("Qual a sua cidade? ") 
    
    if idade >= 60: 
        print("Você é idoso.") 
        
    elif idade >= 18: 
        print("Você é adulto.") 
        
    else: print("Você é menor de idade.") 

    print(f"Você mora em {cidade}.")

if __name__ == "__main__":     
    main() 