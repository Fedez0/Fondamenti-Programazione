class studente:
    def __init__(self,nome,cognome):
        self.nome=nome
        self.cognome=cognome
        self.listaVoti=[]
    def aggiungiVoto(self,voto):
        self.listaVoti.append(voto)

class studenteUniversitario(studente):
    def __init__(self,nome,cognome,matricola):
        super().__init__(nome,cognome)
        self.matricola=matricola
    def getNominativi(self):
        return [self.cognome,self.nome]
    def aggiungiVoto(self,voto):
        super().aggiungiVoto(voto)


if __name__ == '__main__':
    student = studenteUniversitario('rico','germi','390')
    student.aggiungiVoto(30)
    print(student.getNominativi())

