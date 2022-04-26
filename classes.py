class Animal: 
    def __init__(self, tamanho, idade, brabeza):
        self.tamanho = tamanho
        self.idade = idade 
        self.brabeza = brabeza
        
class Cachorro(Animal):

    def __init__(self, tamanho, idade, brabeza):
        self.tamanho = tamanho 
        self.idade = idade   
        self.brabeza = brabeza 

    def obter_velocidade(cls, self):
        velocidade = self.tamanho / self.idade
        print("Velocidade do dog: {} m/s.".format(velocidade))  

    def obter_raca(cls,self):
        raca = self.brabeza / self.tamanho

        if raca >=5:
            print("Pincher")    
        else:             
            print("Caramelo")

   
        

