from models.calcular import Calcular
def main()-> None:
    pontos:int=0
    jogar(pontos)
def jogar(pontos:int)-> None:
    dificuldade: int = int(input('informe o nivel de dificuldade[1,2,3 0u 4]:'))
    calc: Calcular = Calcular(dificuldade)
    print('informe o resultado para a seguinte operaçao:')
    calc.mostrar_operacao()
    resultado: int = int(input())
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'voce tem{pontos} pontos(s).')
        continuar: int = int(input('deseja continuar no jogo?[1 - sim, 0 - não] '))
    if continuar:
            jogar(pontos)
    else:
        print(f'voce finalizou com {pontos} pontos(s).')
        print('ate a proxima')



if __name__=='__main__':
    main()



