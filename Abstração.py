# A abstração foca nos aspectos essenciais de um objeto, 
# ocultando detalhes de implementação. A classe abstrata 
# define a estrutura que suas subclasses devem seguir.

from abc import ABC, abstractmethod

class ProfissionalSaude(ABC):
    def __init__(self, nome, registro, especialidade):
        self.nome = nome
        self.registro = registro
        self.especialidade = especialidade

    @abstractmethod
    def atender_paciente(self):
        pass

    @abstractmethod
    def registrar_prescricao(self, paciente, prescricao):
        pass

# Subclasse representando um médico
class Medico(ProfissionalSaude):
    def atender_paciente(self):
        return f"Dr(a). {self.nome} está atendendo o paciente."

    def registrar_prescricao(self, paciente, prescricao):
        return f"Prescrição registrada para {paciente}: {prescricao}."

# Subclasse representando um enfermeiro
class Enfermeiro(ProfissionalSaude):
    def atender_paciente(self):
        return f"Enfermeiro(a) {self.nome} está monitorando sinais vitais do paciente."

    def registrar_prescricao(self, paciente, prescricao):
        return f"Enfermeiro(a) {self.nome} não pode prescrever medicamentos, apenas seguir o plano médico."

# Testes
medico = Medico("João Silva", "CRM12345", "Cardiologia")
enfermeiro = Enfermeiro("Maria Santos", "COREN67890", "Cuidados Intensivos")

# Testando o método atender_paciente
print(medico.atender_paciente())  # Médico atendendo
print(enfermeiro.atender_paciente())  # Enfermeiro monitorando

# Testando o método registrar_prescricao
print(medico.registrar_prescricao("Carlos Almeida", "Losartana 50mg"))  # Médico prescrevendo
print(enfermeiro.registrar_prescricao("Carlos Almeida", "Curativos diários"))  # Enfermeiro não pode prescrever

