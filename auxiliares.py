def get_min(no):
    while no.esquerda is not None:
        no = no.esquerda
    return no


 