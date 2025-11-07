from datetime import datetime, date

data_entrada = input("Digite uma data (dd/mm/aaaa): ")

def DiferencaDatas (data):
    data_tratada = datetime.strptime(data, "%d/%m/%Y").date()
    hoje = date.today()
    diferenca = hoje - data_tratada
    print(f"Teve {diferenca.days} dias entre a data e hoje.")

DiferencaDatas(data_entrada)