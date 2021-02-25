from itertools import permutations
import random
class Pontos:    
    def populacaoInicial(self,listPermut):
        populacao = []
        cont = 0
        for j in listPermut:
            if n < 5:
                if j[0][0] == "a":
                    cont+=1
                    populacao.append(j)
            else:
                populacao.append(j)
                cont+=1
            if cont == 100:
                break
        return populacao
    
    def distanciaTotal(self,pontosEntrega):
            distanciaTotal = 0
            i = 0
            while i < len(pontosEntrega) - 1:
                distanciaTotal += abs(pontosEntrega[i][1] - pontosEntrega[i+1][1]) + abs(pontosEntrega[i][2] - pontosEntrega[i+1][2])
                
                if i+1 == len(pontosEntrega)-1:
                    distanciaTotal += abs(pontosEntrega[0][1] - pontosEntrega[i+1][1]) + abs(pontosEntrega[0][2] - pontosEntrega[i+1][2])
                                   
                i+=1    
            return distanciaTotal
    


class Fitness(Pontos):
    def __init__(self, popu):
        self.distancia = 0
        self.fitness = 0.0
        self.population = super().populacaoInicial(popu)
        

    def aptidao(self):
        populacaoFitness = []
        for i in range(len(self.population)):
            self.distancia = super().distanciaTotal(self.population[i])
            self.fitness = 1/self.distancia
            populacaoFitness.append(self.fitness)
        
        return populacaoFitness
    
    def torneio(self):
        self.pais = self.population    
        pais = [] 
        apti = self.aptidao()
        for _ in range(100):
            pai1 = random.randrange(0,len(apti))
            pai2 = random.randrange(0,len(apti))
            if apti[pai1] >= apti[pai2]:            
                pais.append(self.pais[pai1])
            else:
                pais.append(self.pais[pai2])
        return pais
    
    def mutacao(self,novaPopulacao):
        chaceMutacao = random.random()
        indice1 = random.randrange(1,n)
        indice2 = random.randrange(1,n)
        filhoMudado = random.randrange(0,100)
        if chaceMutacao <= 0.4:
            for _ in range(1):
                novaPopulacao[filhoMudado][indice1], novaPopulacao[filhoMudado][indice2]  = novaPopulacao[filhoMudado][indice2], novaPopulacao[filhoMudado][indice1] 
        return novaPopulacao     

    
    def crossover(self):
        pais = self.torneio()
        pai1 = []
        pai2 = []
        filho1 = []
        filho2 = []
        novaPopulacao = []
        i = 0
        while i < len(pais):
            pai1 = list(pais[i])
            pai2 = list(pais[i+1])
            if n - 1 != 1:
                pontoCrossover = random.randrange(1,n-1)
            else:
                pontoCrossover = 1

            for w1 in range(1,pontoCrossover):                
                for z1 in range(pontoCrossover,n):
                    if pai1[w1] == pai2[z1]:
                        pai2[w1], pai2[z1] = pai2[z1], pai2[w1]
                
            for j in range(n):
                if j < pontoCrossover:
                    filho1.append(pai1[j])
                else:
                    filho1.append(pai2[j])

            pai1 = list(pais[i])
            pai2 = list(pais[i+1])
            
            for w in range(1,pontoCrossover):
                for z in range(pontoCrossover,n):
                    if pai2[w] == pai1[z]:
                        pai1[w], pai1[z] = pai1[z], pai1[w]

            for k in range(n):
                if k < pontoCrossover:
                    filho2.append(pai2[k])
                else:
                    filho2.append(pai1[k])
            
            i+=2
            novaPopulacao.append(filho1)
            novaPopulacao.append(filho2)
            filho1 = []
            filho2 = []
        return self.mutacao(novaPopulacao)
        
print("A primeira linha contêm o número de pontos de entrega, as próximas linhas você colocará os pontos de entrega e sua posição, exemplo: a 1 2. Lembrando que o primeiro ponto sempre é o ponto 'a', já que ele é o ponto de partida.")
print("Exemplo de entrada:")
print("4")
print("a 1 2")
print("2 5 6")
print("3 2 2")
print("4 0 2")

while True:
    n = input()
    if n != "":
        n = int(n)
        listaPontos = []
        for i in range(n):
            pontos = list(input().split())
            pontos[1] = int(pontos[1])
            pontos[2] = int(pontos[2])
            listaPontos.append(pontos)
        permut = []
        cont = 0
        for p in permutations(listaPontos):
            permut.append(p)
            cont += 1
            if cont == 20:
                break
        menordistancia = 1000000
        menordistanciaAnt = 0
        parada = 0
        saida = []

        while True:
            a = Fitness(permut)
            permut = a.crossover()
            for j in range(len(permut)):
                if a.distanciaTotal(permut[j]) < menordistancia:
                    menordistancia = a.distanciaTotal(permut[j])
                    saida = permut[j]
            if menordistancia == menordistanciaAnt:
                parada += 1   
            else:
                parada = 0
            if parada == 100:
                break

            menordistanciaAnt = menordistancia
        contador = 1
        for l in saida:
            print(contador,"° ponto",l[0][0])
            contador+=1
        print("")
        print("Distância: ",menordistancia)
        print("")
    else:
        break


    

