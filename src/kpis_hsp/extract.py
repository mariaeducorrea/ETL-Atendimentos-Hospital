from db_connection import connection
import csv

def export_data():
    conn = connection()
    cur = conn.cursor()

    query = """
    select  id_fia, data_atendimento, hora_inicio, idade_paciente from sigh.ficha_amb_int 
    where data_atendimento between '2020-01-01' and '2023-12-31' 
    order by data_atendimento asc;
    """
    
    cur.execute(query)

    rows = cur.fetchall()
    
    csv_file = "C:/Users/Administrador/desktop/kpis_hsp/dados/date.csv"


    with open(csv_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id_fia","data_atendimento", "hora_inicio", "idade_paciente"])
        writer.writerows(rows)

    print("Consulta finalizada.")


    cur.close()
    conn.close()


export_data()
