class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def talk(self):
        return "..."


class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def talk(self):
        return "O cachorro latiu!"


class Cavalo(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def talk(self):
        return "O cavalo relinchou!"


class Preguica(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def talk(self):
        return "A pregruiça roncou!"


class Veterinaria:
    
    def examinar(self, animal):
        print(animal.talk())


class Zoologico:
    def __init__(self):
        self.nomes = []
    
    def inserir(self, animal):
        self.nomes.append(animal)
    

    


cachorro = Cachorro("Zack", 7)
cavalo = Cavalo("Persa", 12)
preguica = Preguica("Pablo", 18)  



zoo = Zoologico()
zoo.inserir(cachorro)
zoo.inserir(cavalo)
zoo.inserir(preguica)


vet = Veterinaria()
vet.examinar(cavalo)
vet.examinar(cachorro)
vet.examinar(preguica)



for i in zoo.nomes:
    print(i.nome, i.idade,  ' : ', i.talk())