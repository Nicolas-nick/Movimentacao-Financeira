import csv

def Movimento_de_dados():
    Registros = []
    with open('Dados.csv',  'r', encoding='utf-8', newline='') as Arquivo:
        leitor = csv.DictReader(Arquivo, delimiter = ';')
    
        for Linha in leitor:
            Linha_normal = {Chave.lower(): Valor for Chave, Valor in Linha.items()}
            
            Registro = {
                'Data': Linha_normal ['data'],
                'Conta': Linha_normal ['conta'],
                'Tipo': Linha_normal['tipo'],
                'Valor': float(Linha_normal ['valor']),
                'Descrição': Linha_normal ['descricao']
            }
            Registros.append(Registro)
        return Registros

def Processando_Movimentos(Registros):
    Total_C = 0
    Total_D = 0
    Lancamento = 0 
    Inconsistencias = []
    Saldos = {}
    Fechamento_Diario = {}
    Vistos = set()
    Duplicados = []
    
    for Registro in Registros:
        Lancamento += 1 
        
        Conta = Registro['Conta']
        Tipo = Registro ['Tipo'].strip().upper()
        Valor = Registro ['Valor']
        Data = Registro ['Data']
        Descricao = Registro ['Descrição']
    
        Chave = (Data, Conta, Tipo, Valor, Descricao)
        
        if Chave in Vistos:
            Duplicados.append(
                f"lançamento Duplicado Detectado: {Chave}"
            )
            continue
        
        else:
            Vistos.add(Chave)
        
        if Conta not in Saldos:
            Saldos[Conta] = 0 
            
        if Conta not in Fechamento_Diario:
            Fechamento_Diario[Conta] = {}
            
        if Tipo == 'C':
            Total_C += Valor
            Saldos[Conta] += Valor
        
        elif Tipo == 'D':
            Total_D += Valor
            Saldos[Conta] -= Valor
            
        else:
            Inconsistencias.append(
                f"Tipo Inválido '{Tipo}' na conta: {Conta} na data: {Data}"
            )
            continue
        
        Fechamento_Diario[Conta][Data] = Saldos[Conta]
        
        if Saldos[Conta] < 0:
            Inconsistencias.append(
                f"Conta: {Conta}, Ficou negativada na data: {Data}. Saldo atual: {Saldos[Conta]:.2f}"
            )
    return{
        'Saldos': Saldos,
        'Total_C': Total_C,
        'Total_D': Total_D,
        'Lancamento': Lancamento,
        'Inconsistencia': Inconsistencias,
        'Fechamento_Diario': Fechamento_Diario,
        'Duplicados': Duplicados
    }
    
def Relatorio(Resultado):
    print('-=-'*20)
    print('SALDO POR CONTA'.center(60))
    print('-=-'*20)
    
    for Conta in sorted(Resultado['Saldos'].keys()):
        print(f"{Conta}: {Resultado['Saldos'][Conta]:.2f}")
        print('--'*10)
    
    
    print(f"\nTotal de Credito: {Resultado['Total_C']:.2f}")
    print(f"Total de Debitos: {Resultado['Total_D']:.2f}")
    print(f"Quantidade de lançameto: {Resultado['Lancamento']}\n")
    
    if Resultado['Inconsistencia']:
        print('-=-'*20)
        print('INCONCISTENCIAS ENCONTRADAS'.center(60))
        print('-=-'*20)
        for I in Resultado['Inconsistencia']:
            print(f'{I}')
        
           
    else:
        print('Nenhuma incincistencia encontrada.')
    
    print('\n')  
    print('-=-'*20)
    print('FECHAMENTO DIÁRIO POR CONTA'.center(60))
    print('-=-'*20)           
    
    for Conta in sorted(Resultado['Fechamento_Diario'].keys()):
        print(f'\n Conta: {Conta}')
        print('='*20)
        
        for Data in sorted(Resultado['Fechamento_Diario'][Conta].keys()):
            Saldo = Resultado['Fechamento_Diario'][Conta][Data]
            print(f'{Data}: {Saldo:.2f}')
    
    print('\n')        
    print('-=-'*20)
    print('LANÇAMENTO DUPLICADOS'.center(60))
    print('-=-'*20)     
    
    if Resultado['Duplicados']:
        
        for D in Resultado['Duplicados']:
            print(D)
           
    else:
        print('Nunhum lançamento duplicado encontrado')
    
if __name__ == '__main__':
    Registros = Movimento_de_dados()
    Resultado = Processando_Movimentos(Registros)
    Relatorio (Resultado)
