from modulo import *

if __name__ == "__main__":
    #instanciar o objeto da subclasse
    h = Filho('','','','',0.0,0.0,'')
    
    #entrada de dados
    h.nome = input('Digite o nome: ')
    h.email = input('Digite o e-mail: ')
    h.profissao = input('Digite a profissão: ')
    h.olhos = input('Digite a cor dos olhos: ')
    h.peso = input('Digite o peso: ').replace(',', '.')
    h.altura = input('Digite a altura: ').replace(',', '.')
    h.cor_cabelo = input('Digite a cor do cabelo: ')

    print('\n ')
    h.exibir_cartao_visita()
    h.exibir_fisico()
    print('\n ')