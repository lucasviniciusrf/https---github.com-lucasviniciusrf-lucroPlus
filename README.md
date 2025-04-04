Aplicação de Controle de Vendas e Gastos com PyQt5
1. Estrutura Geral
A aplicação possui três janelas (UIs) carregadas a partir de arquivos .ui criados no Qt Designer:
- venda.ui: Janela principal para registro das vendas.
- gastos.ui: Janela secundária para registro dos gastos.
- lucroFinal.ui: Janela de exibição do lucro final.
2. Conversão Segura de Texto para Número
A função tentar_converter_float(valor) tenta converter um texto (string) para número decimal (float). Caso o valor seja inválido (ex: texto com letras), retorna None. Isso evita que o programa trave com erros de conversão.

def tentar_converter_float(valor):
    try:
        return float(valor)
    except ValueError:
        return None

3. Registro de Vendas
Na janela venda.ui, os usuários inserem três valores de vendas. Esses valores são coletados, convertidos em float e armazenados na lista global 'valores' como tuplas.
Funções envolvidas:
- funcao_principal(): Coleta e armazena os valores.
- calcular_soma(): Soma todos os valores registrados e imprime o total.
4. Registro de Gastos
Na janela gastos.ui, os usuários inserem três valores relacionados a gastos. Estes são validados, convertidos e armazenados na lista 'somaGastos'.
Funções envolvidas:
- vemsegundaJanela(): Mostra a janela de gastos e coleta os dados.
- calculoDosGastos(): Soma os gastos inseridos e imprime o resultado.
5. Cálculo de Lucro Final
Após registrar as vendas e os gastos, o botão correspondente mostra a janela lucroFinal.ui e realiza o cálculo do lucro final:
lucro_final = soma_vendas - soma_gastos
O resultado é exibido em um label dentro da interface com formatação monetária (R$).
Função envolvida:
- ultimoProcesso()
6. Conexão dos Botões
Os botões nas interfaces estão conectados às respectivas funções usando o método connect do PyQt5.
Resumo das Listas
- valores: Armazena tuplas com valores de venda.
- somaGastos: Armazena tuplas com valores de gastos.
Essas listas são usadas para realizar as somas totais e o cálculo do lucro final.
