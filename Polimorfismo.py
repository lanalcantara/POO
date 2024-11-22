# Polimorfismo permite tratar os diferentes profissionais de saúde de forma 
# uniforme ao realizar atividades comuns, como atendimento.

class Medico:
    def __init__(self, nome, crm, especialidade):
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade

    def atender(self):
        return f"Médico {self.nome} (CRM: {self.crm}) está atendendo na especialidade {self.especialidade}."


class Enfermeiro:
    def __init__(self, nome, coren, setor):
        self.nome = nome
        self.coren = coren
        self.setor = setor

    def atender(self):
        return f"Enfermeiro(a) {self.nome} (COREN: {self.coren}) está atendendo no setor {self.setor}."


class TecnicoRadiologia:
    def __init__(self, nome, registro, equipamento):
        self.nome = nome
        self.registro = registro
        self.equipamento = equipamento

    def atender(self):
        return f"Técnico de Radiologia {self.nome} (Registro: {self.registro}) está operando o equipamento {self.equipamento}."


def teste_atendimento(profissional):
    print(profissional.atender())


# Código Principal
medico = Medico("Dr. Ana", "CRM67890", "Pediatria")
enfermeiro = Enfermeiro("Enf. Marcos", "COREN98765", "UTI")
tecnico = TecnicoRadiologia("Téc. Laura", "RAD112233", "Tomógrafo")

print("Testando o Médico:")
teste_atendimento(medico)

print("\nTestando o Enfermeiro:")
teste_atendimento(enfermeiro)

print("\nTestando o Técnico de Radiologia:")
teste_atendimento(tecnico)
