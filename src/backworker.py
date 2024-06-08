'''
Estagios do pipeline: IF - ID - EX - MEM - WR

O trabalho 2 é o desenvolvimento de um simulador (qualquer linguagem) para o suporte multithreading SMT, IMT e BMT. Os
suportes IMT e BMT devem ser feitos tanto para arquitetura escalar quanto superescalar. Uma arquitetura de referência
sem suporte deve ser feita para escalar e superescalar. 

!! importante !!
Importante considerar efeitos de dependência de dados, conflitos de recursos e controle para elaboração do simulador.


Arquitetura: colocar tamanho para bando de registradores - nesse case ate 16 


Criar classe intrucoes, vai ter. Titulo, registradores ( saida, operador1 e operador 2 (Olhar risc v) )
PC = Um vetor de intrucoes 
Registradores em uso = outro vetor de interios para olhar quais registradores estao em uso

'''
import random

intrucoes_nome = ["ADD", "SUB"]
TAMANHO_REGISTRADORES = 16


def encher_contador_programa():

    for x in range(10):
        contador_de_programa.append(
            intrucoes(
                random.choice(intrucoes_nome),
                random.randint(0,15),
                random.randint(0,15),
                random.randint(0,15)
            )
        )



class intrucoes():
    def __init__(self, nome, saida, entrada1, entrada2):
        self.nome = nome
        self.saida = saida
        self.entrada1 = entrada1
        self.entrada2 = entrada2

    def listar_propriedades(self):
        print(self.nome,self.saida,self.entrada1,self.entrada2)
    

contador_de_programa = []
pipeline_escalar = [intrucoes]*5


print(contador_de_programa)
encher_contador_programa()

for x in contador_de_programa:
    x.listar_propriedades()

