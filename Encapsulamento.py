# Encapsulamento tem o objetivo de proteger os dados internos 
# de uma classe. Em um sistema de saúde, isso garante que informações 
# sensíveis, como prontuários médicos, sejam acessadas apenas por 
# métodos controlados.

class Paciente:
    def __init__(self, id_paciente, nome, idade, prontuario):
        self._id_paciente = id_paciente  # Atributo privado
        self._nome = nome                # Atributo privado
        self._idade = idade              # Atributo privado
        self._prontuario = prontuario    # Atributo privado

    def atualizar_idade(self, nova_idade):
        if nova_idade > 0:
            self._idade = nova_idade
        else:
            print("Idade inválida.")

    def acessar_prontuario(self):
        return f"Prontuário de {self._nome}: {self._prontuario}"

# Testes
paciente = Paciente(101, "Carlos Almeida", 45, "Histórico: Hipertensão arterial.")
paciente.atualizar_idade(46)  # Atualização válida de idade
print(paciente.acessar_prontuario())  # Exibe o prontuário

paciente.atualizar_idade(0)  # Teste de validação com idade inválida
paciente.atualizar_idade(50)  # Atualização válida de idade
print(f"Nova idade de {paciente._nome}: {paciente._idade}")  # Acessa a nova idade
