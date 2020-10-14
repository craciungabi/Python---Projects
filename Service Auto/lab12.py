def suma_max_vec(lista):
    """
    :returns sum max
    :param lista:
    :return:
    """
    Fin = [lista[0]]
    maxi = max(lista[0], lista[1])
    Fin.append(maxi)
    for i in range(2, len(lista)):
        Fin.append(max(Fin[i - 1], Fin[i - 2] + lista[i]))

    return Fin[len(lista)-1]


print(suma_max_vec([2, 7, 5, 3, 4, 2, -111]))
