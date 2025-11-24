# ex6_funcoes.py

def saudacao(nome): 
    return f"Olá, {nome}!" 
    
def quantofalta(idade):

    return f"Faltam {100 - idade} anos completar 100 anos." 


def main():

    usuario = input("Digite seu nome: ")
    idade = int(input("Qual a sua idade? "))

    print(saudacao(usuario)) 
    print(quantofalta(idade))

    

if __name__ == "__main__":     
    main() 