                                #Projeto 04 - Simulador de votação:
#Crie um programa que simule um sistema de votação, ele deve receber votos até que o usuário diga que não tem mais ninguém para votar.
#esse programa precisa ter duas funções:
#~> 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o ano de nascimento de uma pessoa que será digitado pelo usuário,
#retornando umvalor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
#~> 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que viráda função autoriza_voto()) 
#e o voto que é o número que a pessoa votou. Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, 
#caso o contrário a 2° função deve validar o número que a pessoa escolheu, ela pode escolher de 1 a 5 (crie 3 candidatos para a votação):
#● 1, 2 ou 3 - Votos para os respectivos candidatos, ● 4- Voto Nulo, ● 5 - Voto em Branco.
#Sua função votacao() tem que calcular e mostrar: ● O total de votos para cada candidato;
#● O total de votos nulos; ● O total de votos em branco; ● Qual candidato venceu a votação.

from time import sleep #bliblioteca que permite pausar a amostragem na execução do programa.

def linhas(): # linhas de separação.
    print(f'=-'*40)
 

def autoriza_voto(): #função usada para validar a idade.
    from datetime import date #biblioteca que vai calcular a idade tendo o ano atual como base.
    anoVig = date.today().year #função 'today' considera a data de hoje.
    nasc = int(input('Insira sua data de nascimento "AAAA": ')) #para ser exato o resultado, é necessário colocar o ano em formato AAAA. 
    idade = anoVig - nasc
    
    if idade < 16:                              #se o usuário tiver menos de 16 anos, o sistema o impede de votar.
        return f'VOTO NEGADO'
    elif 16 >= idade < 18 and idade > 70:       #se tiver idade maior que 16 anos e menor que 18 anos, ou maior que 70 anos, o voto é opcional.
        return f'VOTO OPCIONAL'
    else:
        return f'VOTO OBRIGATÓRIO'              #voto é obrigatório para maiores que 18 anos e menores que 70 anos.

def votacao(voto): # Função para a votação dos candidatos e os respectivos contadores.
    candidato1 = 0      #contadores zerados receberão valores somados a cada voto.
    candidato2 = 0
    candidato3 = 0
    nulo = 0
    branco = 0 
    while True: #while irá pontuar se o usuário tem ou não idade para votar.
        while True: 
            if autoriza_voto() == 'VOTO NEGADO': #se o voto for negado, o programa mostrará a msg de aviso, e voltará a solicitar idade.
                print( f'Sua idade impede sua participação. Voto Negado.')
            else:                               #se for permitido o voto, o programa seguirá com a execução.
                break    
        voto = int(input('''
        [1] - Hans Landa
        [2] - King Shultz
        [3] - Kevin Hoocker Killer
        [4] - Nulo
        [5] - Branco
        '''))
        linhas()
        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1
        elif voto == 4:
            nulo += 1
        elif voto == 5:
            branco += 1
        elif 1 < voto > 5 :
            print(f'Opção não cadastrada! Tente novamente.')#se o valor digitado for diferente dos indicados de 1 a 5, o sistema avisará o erro.

        seguir = input(f'Continuar votação ? [S/N] ').upper() #nessa variável, o usuário define se segue ou não recebendo votos, é indeterminado. 
        if seguir == 'N':                                       #digitando 'N', o programa concluirá a execução, mostrando os reseultados.
            break   
    print(f'Apurando os Votos')
    sleep(1)
    linhas()
    print(f'''
                APURAÇÃO DE FINALIZADA

        Votos Hans Landa:               {candidato1}

        Votos King Shultz:              {candidato2}

        Votos Kevin Hoocker Killer:     {candidato3}

        Votos Nulos:                    {nulo}

        Votos Brancos:                  {branco}
''') 
    sleep(1)  
    linhas()
    if candidato2 < candidato1 > candidato3:
        return f'Hans Landa é o melhor vilão!'
    elif candidato3 < candidato2 > candidato1:
        return f'King Shultz é o melhor vilão!'
    elif candidato1 < candidato3 > candidato2:
        return f'Kevin Hoocker Killer é o melhor vilão!'
    
#programa principal (*vi que o Gustavo Guanabara colocou o programa inicial no fim e catei a idéia.)
linhas()
print(f'''
    ~> Quentin Tarantino é um excelente cineastra, dentre seus filmes, 
            separei TRÊS dos mais icônicos vilões de duas obras. 
                    Qual deles você mais ama odiar? <~
''')

linhas()
print(votacao(autoriza_voto))