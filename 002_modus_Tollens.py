# modus_tollens.py
# Ejemplo de Modus Tollens
# Regla: Si P → Q y se cumple ¬Q, entonces concluimos ¬P.

def modus_tollens(premisa: tuple[str, str], no_q: str) -> str | None:
    """
    premisa: tupla (P, Q) que representa 'Si P entonces Q'
    no_q: negación de Q observada (ejemplo: 'no me mojo')
    retorna: ¬P si aplica Modus Tollens, en caso contrario None
    """
    P, Q = premisa
    # Si recibimos 'no Q', concluimos 'no P'
    if no_q.lower() in [f"no {Q.lower()}", f"¬{Q.lower()}", f"~{Q.lower()}"]:
        return f"no {P}"
    return None

def ejemplo():
    # Ejemplo clásico: Si llueve, me mojo. No me mojo. ⇒ No llueve.
    P = "llueve"
    Q = "me mojo"

    conclusion = modus_tollens((P, Q), no_q="no me mojo")

    print("Premisa 1: Si llueve entonces me mojo. (P → Q)")
    print("Premisa 2: No me mojo. (¬Q)")
    if conclusion:
        print("Conclusión:", conclusion)  # Se espera "no llueve"
    else:
        print("No se pudo aplicar Modus Tollens.")

if __name__ == "__main__":
    ejemplo()
