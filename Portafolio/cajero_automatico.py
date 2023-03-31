valor_total = 0

print("----Bienvenido al cajero automatico----")
print("----Que quieres hacer?----")

print("1. Consultar Saldo")
print("2. Meter Saldo")
print("3. Sacar Saldo")
print("4. Enviar Saldo")

index_decision = int(input())

def ConsultarSaldo():
    print("Quieres consultar tu saldo? Y/N:")

    decision = str(input())

    valor_total_string = valor_total

    if decision == "y":
        print("Tu saldo total es:" "" + str(valor_total_string))
    else:
        "Cerrando cajero..."

def MeterDinero():
    print("Cuanto dinero quieres meter? :")

    valor_nuevo = int(input())

    valor_actualizado = valor_total + valor_nuevo

    try:
        print("Tu saldo total es:" + "" + str(valor_actualizado))
    except:
        print("Cerrando cajero...")

def SacarDinero():
    print("Cuanto dinero quieres sacar? :")

    valor_faltante = int(input())

    valor_actualizado2 = valor_total + valor_faltante

    try:
        print("Tu saldo total es:" + "" + str(valor_actualizado2))
    except:
        print("Cerrando cajero...")

def EnviarDinero():
    print("Cuanto dinero quieres enviar? :")

    valor_de_envio = int(input())

    valor_actualizado3 = valor_total + valor_de_envio

    try:
        print("Tu saldo total es:" + "" + str(valor_actualizado3))
    except:
        print("Cerrando cajero...")

if index_decision == 1:
    ConsultarSaldo()
elif index_decision == 2:
    MeterDinero()
elif index_decision == 3:
    SacarDinero()
else:
    EnviarDinero()