# ex4_tab.py

def main():

    for i in range(1, 11):
        print(f"\nTabuada do {i}:")
        for j in range(1, 11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")


if __name__ == "__main__":     
    main() 