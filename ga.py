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
	pop_t = random.sample(range(0, 5), 5)
	for x in range(9):
		individuo = random.sample(range(0, 5), 5)
		pop_t = numpy.r_[pop_t,individuo]
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
	for i in range(10):
		c_ind[i] = 1./fc(pop,i,matrix)
		summ += 1./fc(pop,i,matrix)
	print('soma '+str(summ))
	p_tot = 0
	for i in range(10):
		print(c_ind[i])
		c_ind[i] = ((100* c_ind[i])/summ)
		p_tot+= c_ind[i]
	print(c_ind[0])
	print(p_tot)
if __name__ == '__main__':
	#Representacao matricial do grafo(matriz(x,y) onde x e y sao vertices do grafo)
	matrix = numpy.matrix = ([[-1,2,9,3,5],[2,-1,4,3,8],[9,4,-1,7,3],[3,3,7,-1,3],[5,8,3,3,-1]])
	pop = init_pop()
	print(pop[0])
	print('custo' + str(fc(pop,0,matrix)))
	selecao(pop,matrix)
	#selecao
	#Cruzamento

