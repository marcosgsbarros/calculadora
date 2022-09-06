import os

class Calculadora:

    def soma(self, n1,n2):
        try:
            print(f'Resultado da soma: {n1 + n2}')
        except:
            print('Erro:Não foi possível realizar a soma')

    def subtracao(self, n1,n2):
        try:
            print(f'Resultado da subtração: {n1 - n2}')
        except:
            print('Erro:Não foi possível realizar a subtração')

    def divisao(self, n1,n2):
        try:
            print(f'Resultado da divisão: {n1 / n2}')
        except ZeroDivisionError as erro:
            print('Erro: não é possível realizar divisão por 0')
        except:
            print('Erro:Não foi possível realizar a divisão')

    def multiplicacao(self, n1,n2):
        try:
            print(f'Resultado da multiplicação: {n1 * n2}')
        except:
            print('Erro:Não foi possível realizar a multiplicação')

    def exponenciacao(self, n1,n2):
        try:
            print(f'Resultado da exponenciação: {n1 ** n2}')
        except:
            print('Erro:Não foi possível realizar a exponenciação')      

    def separa_num(self,operacao):
        num = ''
        for i in operacao:
            if i.isnumeric() or i =='.':
                num += i 
            else:
                break
        try:
            return int(num)
        except ValueError:
            pass
            try:
                return float(num)
            except ValueError:
                print('Erro: Não foi possível realizar operação revise o calculo')

    def retorna_indice(self,operacao):
        lista = ['+','-','/','*','**']
        for y in operacao:
            for x in lista:
                if x in operacao:
                    indice = operacao.index(x)
        return indice
        

    def separa_num2(self,operacao,ind):
        num2 = ''
        for i2 in operacao[ind:]:
            if i2.isnumeric() or i2 =='.':
                num2 += i2
        try:
            return float(num2)
        except:
            pass
        
    def chama_operacao(self,operacao):
        if '+' in operacao:
            self.soma(n1,n2)
        if '-' in operacao:
            self.subtracao(n1,n2)
        if '/' in operacao:
            self.divisao(n1,n2)
        if operacao.count('*') == 1:
            self.multiplicacao(n1,n2)
        if '**' in operacao:
            self.exponenciacao(n1,n2)
    
    def decisao(self,opcao):
        if opcao == '0':
            return True
        else:
            return False

    def limpar_tela(self,limpar):
        if limpar == '0':
            os.system('cls')
        else:
            pass


while True:
    classe = Calculadora()
    conta = input("Digite a conta: ")
    n1 = classe.separa_num(conta)
    n2 = classe.separa_num2(conta,classe.retorna_indice(conta))
    classe.separa_num(conta)
    classe.retorna_indice(conta)
    classe.separa_num2(conta,classe.retorna_indice(conta))
    classe.chama_operacao(conta)
    if classe.decisao(input('Deseja fazer mais calculos? Digite 0-SIM, ou aperte qualquer tecla para finalizar ')) == False:
        break
    classe.limpar_tela(input('Deseja limpar a tela? digite 0-SIM / ou aperte qualquer tecla para prosseguir '))
