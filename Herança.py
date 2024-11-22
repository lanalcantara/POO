# Herança permite criar classes derivadas 
# para diferentes tipos de profissionais de saúde, 
# reutilizando atributos e métodos da classe base.

class ProfissionalSaude:
    def __init__(self, nome):
        self.nome = nome


class Medico(ProfissionalSaude):
    def atender_paciente(self):
        print(f"Médico {self.nome} está atendendo um paciente com sintomas de febre.")

    def registrar_prescricao(self, paciente, prescricao):
        print(f"Prescrição registrada para o paciente {paciente}: {prescricao}")


class Enfermeiro(ProfissionalSaude):
    def atender_paciente(self):
        print(f"Enfermeiro {self.nome} está realizando a troca de curativos do paciente.")

    def registrar_prescricao(self, paciente, prescricao):
        print(f"Enfermeiros não têm permissão para prescrever medicamentos. Plano sugerido: {prescricao}")


# Exemplo de uso
medico = Medico("Dr. Pedro")
medico.atender_paciente()  # Médico atendendo paciente
medico.registrar_prescricao("Clara", "Ibuprofeno 600mg")  # Médico registrando prescrição

enfermeiro = Enfermeiro("Enf. Beatriz")
enfermeiro.atender_paciente()  # Enfermeiro realizando procedimento
enfermeiro.registrar_prescricao("Lucas", "Troca de curativo diário")  # Enfermeiro sugerindo um plano
