from PyQt5 import uic, QtWidgets

# Criar uma lista global para armazenar os valores inseridos
valores = []
somaGastos = []

def tentar_converter_float(valor):
    try:
        return float(valor)  # Tenta converter para float
    except ValueError:
        return None  # Retorna None se falhar

def funcao_principal():
    # Obter os valores dos campos de texto
    linha1 = venda.lineEdit.text()
    linha2 = venda.lineEdit_2.text()
    linha3 = venda.lineEdit_3.text()

    # Tentar converter os valores para float
    valor1 = tentar_converter_float(linha1)
    valor2 = tentar_converter_float(linha2)
    valor3 = tentar_converter_float(linha3)

    # Verificar se todos os valores são válidos
    if valor1 is not None and valor2 is not None and valor3 is not None:
        # Adicionar os valores inseridos à lista
        valores.append((valor1, valor2, valor3))
        
        # Limpar os campos de texto para novos valores
        venda.lineEdit.setText("")
        venda.lineEdit_2.setText("")
        venda.lineEdit_3.setText("")
    else:
        print("Erro: Um ou mais valores inseridos não são válidos.")  # Exemplo de mensagem de erro

def calcular_soma():
    # Calcular a soma de todos os valores inseridos
    soma_total = sum([sum(item) for item in valores])  # soma cada tupla e depois soma total
    print(f"Soma total das vendas: {soma_total}")
    
def vemsegundaJanela():
    gastos.show()

    # Obter os valores inseridos nos campos de texto da segunda janela
    linhaGasto1 = gastos.lineEdit_4.text()
    linhaGasto2 = gastos.lineEdit.text()
    linhaGasto3 = gastos.lineEdit_2.text()

    # Tentar converter os valores para float
    gasto1 = tentar_converter_float(linhaGasto1)
    gasto2 = tentar_converter_float(linhaGasto2)
    gasto3 = tentar_converter_float(linhaGasto3)

    # Verificar se todos os valores são válidos
    if gasto1 is not None and gasto2 is not None and gasto3 is not None:
        # Adicionar itens à lista de gastos
        somaGastos.append((gasto1, gasto2, gasto3))
        
        # Limpar os campos de texto da segunda janela
        gastos.lineEdit_4.setText("")
        gastos.lineEdit.setText("")
        gastos.lineEdit_2.setText("")
    else:
        print("Erro: Um ou mais valores inseridos não são válidos.")  # Exemplo de mensagem de erro

def calculoDosGastos():
    # Calcular a soma dos gastos inseridos
    soma_total_gastos = sum([sum(item) for item in somaGastos])  # soma cada tupla de gastos e depois soma total
    print(f"Soma total dos gastos: {soma_total_gastos}")

# Função para calcular o lucro final (subtração das vendas pelos gastos)
def ultimoProcesso():
    lucroFinal.show()
    
    # Soma total das vendas
    soma_vendas = sum([sum(item) for item in valores])
    
    # Soma total dos gastos
    soma_gastos = sum([sum(item) for item in somaGastos])
    
    # Calcular lucro final
    lucro_final = soma_vendas - soma_gastos
    print(f"Lucro final: {lucro_final}")

    # Exibir o valor do lucro final na interface (campo de texto)
    lucroFinal.lucro_label.setText(f"Lucro: R${lucro_final:.2f}")  # Atualiza o label com o lucro

app = QtWidgets.QApplication([])

# Carregar a interface do usuário
venda = uic.loadUi("venda.ui")
gastos = uic.loadUi("gastos.ui")
lucroFinal = uic.loadUi("lucroFinal.ui")

# Conectar os botões às funções correspondentes
venda.pushButton.clicked.connect(funcao_principal)
venda.pushButton.clicked.connect(calcular_soma)
venda.pushButton_2.clicked.connect(vemsegundaJanela)
gastos.pushButton_3.clicked.connect(vemsegundaJanela)
gastos.pushButton_3.clicked.connect(calculoDosGastos)
gastos.pushButton_4.clicked.connect(ultimoProcesso)

# Exibir a interface do usuário
venda.show()
app.exec()
