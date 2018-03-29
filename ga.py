import random
import numpy

tam_pop = 10 	#N de individuos na populacao: 10
tx_c = 0.99	#Taxa de cruzamento
tx_m = 0.01 #Taxa de mutacao
custao = 1000

def fc(pop,individuo,matrix): # Funcaoo de Custo de cada individuo
	custo = 0
	for x in range(5):
		if(x != 4):
			custo += matrix[int(pop[individuo][x])][int(pop[individuo][x+1])]
		for y in range(5):
			if(pop[individuo][x] == pop[individuo][y] and x != y):
				custo += 20
	return custo


def init_pop(): #Iniciando uma populacao
	
	#sorteando 5 numeros aleatorios diferentes de 0-5 (visita os vertices)
	pop_t = random.sample(range(0, 5), 5)
	
	#sortea mais 9 (tamamnho da pop)
	for x in range(9):

		#sorteia mais 5 os vertices
		individuo = random.sample(range(0, 5), 5)
		
		#numpy biblioteca utilizada, objetivo concatenar
		pop_t = numpy.r_[pop_t,individuo]
	
	#ate o return passamos de representação vetorial para matricial
	pop = numpy.zeros((10,5))
	for x in range(tam_pop):
		for y in range(5):
			pop[x][y] = pop_t[x*5+y]
	return pop

#Selecao
def selecao(pop,matrix):
	#roleta
	summ = 0.
	c_ind = numpy.zeros((10))
	
	#Preparacao das porcentagens de cada individuo, para sorteio da roleta
	
	for i in range(10):
		c_ind[i] = 1./fc(pop,i,matrix)
		summ += 1./fc(pop,i,matrix)
	p_tot = 0
	for i in range(10):
		c_ind[i] = ((100* c_ind[i])/summ)
		p_tot+= c_ind[i]
		c_ind[i] = format(c_ind[i], '.2f')
	p_tot = format(p_tot,'.2f')
	
	#Sorteio da roleta

	lucas = random.randint(0,100) # os caras aqui sao frescos, dsclp
	i=0
	while((lucas-c_ind[i])>0):
		lucas -= c_ind[i]
		i+=1
	
	return i


if __name__ == '__main__':
	#Representacao matricial do grafo(matriz(x,y) onde x e y sao vertices do grafo)
	matrix = numpy.matrix = ([[-1,2,9,3,5],[2,-1,4,3,8],[9,4,-1,7,3],[3,3,7,-1,3],[5,8,3,3,-1]])
	pop = init_pop()
	selecao(pop,matrix)
	#selecao
	#Cruzamento

