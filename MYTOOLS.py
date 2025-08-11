PI_INT = ""
E_INT = ""

def pi_real(n):

    if 0 < n < 100:
        casas_desejadas = int(PI_INT[:n])
        casa_decimal = casas_desejadas * (10 ** (-n))
        pi = 3 + casa_decimal
        print(pi)

    else:
        print("Escolha um número válido para o 'n'.")

def e_real(n):

    if 0 < n < 100:
        casas_desejadas = int(E_INT[:n])
        casa_decimal = casas_desejadas * (10 ** (-n))
        e = 2 + casa_decimal
        print(e)

    else:
        print("Escolha um número válido para o 'n'.")



