from classes import *


while True:
   
    menu = int(input("Digite a opção: 1 - Velocidade do dog, 2 - Descubra a raça do dog, 3 - Sair"))
    
    if menu == 1:
              

        dog_tamanho = float(input("Digite o tamanho do dog em metros: "))
        dog_idade = float(input("Digite a idade do dog em anos: "))

        new_dog = Cachorro(dog_tamanho, dog_idade) #cria o objeto e joga as variáveis inputadas nos parâmetros herdados da classe

        new_dog.obter_velocidade(new_dog) #invoca o método do objeto, que imprime a velocidade na tela

        menu2 = int(input("Verificar de novo? 1 - Reiniciar, 2 - Sair"))

        if menu2 == 1:
            continue  

        if menu2 == 2:
            break

    elif menu == 2:

        print("Verificar qual a raça do cachorro por suas características")

        dog_brabeza = float(input("Digite o quão brabo o dog é de 0 à 10"))
        dog_tamanho = float(input("Digite o tamanho do dog em metros, de 0 à 2: "))
        dog_idade = 0

        new_dog = Cachorro(dog_tamanho, dog_idade, dog_brabeza)
           
        new_dog.obter_raca(new_dog) #invoca o método                

    else:
        break     
