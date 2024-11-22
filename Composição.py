# Composição permite construir classes complexas. 
# Por exemplo, um Hospital pode ser composto por várias 
# unidades que possuem diferentes equipamentos e profissionais.

class Unidade:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

class Hospital:
    def __init__(self, nome):
        self.nome = nome
        self.unidades = []

    def adicionar_unidade(self, unidade):
        self.unidades.append(unidade)

    def listar_unidades(self):
        print(f"Unidades do hospital {self.nome}:")
        for unidade in self.unidades:
            print(f"- {unidade.nome} ({unidade.tipo})")

# Testes
hospital = Hospital("Hospital Geral")
uti = Unidade("Unidade de Terapia Intensiva", "UTI")
emergencia = Unidade("Emergência", "Atendimento de Urgência")
radiologia = Unidade("Radiologia", "Exames de imagem")
pediatria = Unidade("Pediatria", "Atendimento infantil")

hospital.adicionar_unidade(uti)
hospital.adicionar_unidade(emergencia)
hospital.adicionar_unidade(radiologia)
hospital.adicionar_unidade(pediatria)

hospital.listar_unidades()

# Adicionando um hospital diferente para demonstrar reutilização
hospital_regional = Hospital("Hospital Regional")
laboratorio = Unidade("Laboratório de Análises Clínicas", "Exames")
cirurgia = Unidade("Centro Cirúrgico", "Cirurgias de média e alta complexidade")

hospital_regional.adicionar_unidade(laboratorio)
hospital_regional.adicionar_unidade(cirurgia)

print("\n")
hospital_regional.listar_unidades()
