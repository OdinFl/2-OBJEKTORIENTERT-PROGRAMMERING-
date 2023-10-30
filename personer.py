class Personer:
    """Lager en klasse for å beskrive navn, etternavn og fødselsåret til en person
    """
    def __init__(self, navn:str, etternavn:str, fødselsår:int) -> None:
        self.navn = navn
        self.etternavn = etternavn
        self.fødselsår = fødselsår

odin = Personer("Odin", "Flatberg", 2005)
print(odin)
print(odin.navn)
print(odin.etternavn)
print(odin.fødselsår)