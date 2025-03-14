import pandas as pd

#lendo o arquivo csv
dados = pd.read_csv('C:/Users/Administrador/Desktop/kpis_hsp/dados/date.csv')


##### tratamento dos dados #####

#convertendo coluna data_atendimento para datetime
dados['data'] = pd.to_datetime(dados['data_atendimento']).dt.date

#arredondando o horário
dados['hora'] = pd.to_datetime(dados['hora_inicio'], format='%H:%M:%S').dt.floor('h').dt.strftime('%H:00')


#extrair idade
def extrair_idade(idade):
    if pd.isna(idade): #verificar se é nulo o valor
        return None
    if isinstance(idade, (int, float)):
        return int(idade)
    partes = str(idade).split()
    if partes and partes[0].isdigit(): #verificar se o index 0 é numerico
        return int(partes[0]) #se for numerico retorna o mesmo
    else:
        return None

#categorizar idade
def idade_categoria(idade):
    idade_ex = extrair_idade(idade)
    if idade_ex is None:
        return 'Desconhecido'
    elif idade_ex <= 19:
        return 'Jovem'
    elif 20 <= idade_ex <= 59:
        return 'Adulto'
    else:
        return 'Idoso'

#extrair idade da coluna
dados['idade'] = dados['idade_paciente'].apply(extrair_idade)

#coluna categoria
dados['categoria'] = dados['idade'].apply(idade_categoria)

atendimentos = dados.groupby(['id_fia', 'data', 'hora', 'idade', 'categoria']).size().reset_index(name='quantidade')

with pd.ExcelWriter('C:/Users/Administrador/Desktop/kpis_hsp/dados/dados.xlsx') as file:
    atendimentos.to_excel(file, sheet_name='Atendimentos', index=False)

print('Arquivos salvos.')



