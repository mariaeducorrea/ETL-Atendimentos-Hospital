import pandas as pd


dados = pd.read_csv('C:/Users/Administrador/desktop/kpis_hsp/dados/date_extract.csv')


#print(data)

#converte coluna data_atendimento para o tipo de dado datetime
dados['data_atd'] = pd.to_datetime(dados['data_atendimento'])   

#criar coluna apenas com a data (sem horário)
dados['data'] = dados['data_atd'].dt.date


###### Total de atendimentos por dia
#agrupar por data, estraindo somente data. Size() conta quantidade de aten. por data e usando .reset_index para criar os indices.
total_atd_dia = dados.groupby('data').size().reset_index(name='total_atd_dia')

###### Total de atendimentos por mês
#criar coluna apenas com o mes 
dados['mes'] = pd.to_datetime(dados['data']).dt.to_period('M')
#adicionar coluna com nome dos meses
dados['nome_mes'] = dados['data_atd'].dt.month_name()
#agrupa atendimentos por mes
total_atd_mes = dados.groupby(['mes','nome_mes']).size().reset_index(name='total_atd_mes')

###### Media total de atendimentos por hora
##crian coluna com hora
dados['hora_arredondada'] = pd.to_datetime(dados['hora_inicio'], format='%H:%M:%S').dt.floor('H').dt.strftime('%H:00')
#agrupa atendimentos por hora
total_atd_hora = dados.groupby(['mes','hora_arredondada']).size().reset_index(name='total_atd_hora')

###### Atendimentos por ano 



with pd.ExcelWriter('C:/Users/Administrador/desktop/kpis_hsp/dados/date_transform.xlsx') as file:
    total_atd_dia.to_excel(file, sheet_name='Atendimentos por Dia', index=False)
    total_atd_mes.to_excel(file, sheet_name='Atendimentos por Mês', index=False)
    total_atd_hora.to_excel(file, sheet_name='Atendimentos por Hora', index=False)