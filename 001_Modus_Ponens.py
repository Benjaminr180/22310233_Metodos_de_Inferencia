# modus_ponens.py
# Ejemplo de Modus Ponens
# Regla: Si P → Q y se cumple P, entonces concluimos Q.

def modus_ponens(premisa: tuple[str, str], hecho: str) -> str | None:
    """
    premisa: tupla (P, Q) que representa 'Si P entonces Q'
    hecho: proposición que sabemos que es verdadera (P)
    retorna: Q si aplica Modus Ponens, en caso contrario None
    """
    P, Q = premisa
    if hecho.lower() == P.lower():
        return Q
    return None

def ejemplo():
    # Ejemplo clásico: Si llueve, me mojo. Llueve. ⇒ Me mojo.
    P = "llueve"
    Q = "me mojo"

    conclusion = modus_ponens((P, Q), hecho="llueve")

    print("Premisa 1: Si llueve entonces me mojo. (P → Q)")
    print("Premisa 2: Llueve. (P)")
    if conclusion:
        print("Conclusión:", conclusion)  # Se espera "me mojo"
    else:
        print("No se pudo aplicar Modus Ponens.")

if __name__ == "__main__":
    ejemplo()
