PI_INT = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
E_INT = "7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

def pi_real(n):

    if 0 < n < 100:
        casas_desejadas = int(PI_INT[:n])
        casa_decimal = casas_desejadas * (10 ** (-n))
        pi = 3 + casa_decimal
        
        return pi

    else:
        print("Escolha um número válido para o 'n'.")

def e_real(n):

    if 0 < n < 100:
        casas_desejadas = int(E_INT[:n])
        casa_decimal = casas_desejadas * (10 ** (-n))
        e = 2 + casa_decimal
        
        return e

    else:
        print("Escolha um número válido para o 'n'.")



