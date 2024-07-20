from datetime import datetime


data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

print(data_e_hora_em_texto)

