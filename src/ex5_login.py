# ex5_login.py

def main():

    senha_correta = "python123" 
    
    tentativa = "" 

    vezes = 0
    
    while tentativa != senha_correta: 

        vezes += 1

        if vezes > 3:
            print("Número máximo de tentativas excedido. Acesso negado.")
            return

        tentativa = input("Digite a senha: ") 
    
    print("Acesso liberado!") 


if __name__ == "__main__":     
    main() 