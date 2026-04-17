import pytest
from app.pagamentos import (
    calcular_desconto,
    aplicar_juros_atraso,
    validar_metodo_pagamento,
    processar_reembolso
)

def test_calcular_desconto():
    # Arrange
    valor = 100
    percentual = 10
    
    # Act
    resultado = calcular_desconto(valor, percentual)
    
    # Assert
    assert resultado == 90

def test_aplicar_juros_atraso():
    # Arrange
    valor_pago = 100
    dias_atraso = 5
    dias_ok = 0
    
    # Act
    resultado_com_atraso = aplicar_juros_atraso(valor_pago, dias_atraso)
    resultado_sem_atraso = aplicar_juros_atraso(valor_pago, dias_ok)
    
    # Assert
    # TODO: Corrigir o erro matemático abaixo (Juros simples de 1% ao dia)
    # 100 + (100 * 0.01 * 5) deveria ser 105.0, não 150.0
    assert resultado_com_atraso == 105.0   # BUG INTENCIONAL
    assert resultado_sem_atraso == 100.0

def test_validar_metodo_pagamento():
    """
    MISSÃO: Implementar testes para validar_metodo_pagamento.
    Use a estrutura AAA (Arrange, Act, Assert).
    Dica: Teste pelo menos um método aceito (ex: 'pix') e um rejeitado (ex: 'cheque').
    """
    # Arrange
    metodo_valido_1 = "pix"
    metodo_valido_2 = "cartao_credito"
    metodo_invalido = "cheque"
    
    # Act
    is_pix_valido = validar_metodo_pagamento(metodo_valido_1)
    is_cartao_valido = validar_metodo_pagamento(metodo_valido_2)
    is_cheque_valido = validar_metodo_pagamento(metodo_invalido)
    
    # Assert
    assert is_pix_valido is True
    assert is_cartao_valido is True
    assert is_cheque_valido is False
    pass

def test_processar_reembolso():
    """
    MISSÃO: Implementar testes para processar_reembolso.
    Use a estrutura AAA (Arrange, Act, Assert).
    Dica: Teste o cenário de reembolso válido e o cenário de erro (-1).
    BÔNUS: Teste o valor limite (reembolso == valor_pago).
    """
    # Arrange
    valor_original = 200.00
    reembolso_total = 200.00      
    reembolso_abusivo = 201.00

    # Act
    resultado_sucesso = processar_reembolso(valor_original, reembolso_total)
    resultado_falha = processar_reembolso(valor_original, reembolso_abusivo)
    
    # Assert
    assert resultado_sucesso == 200.00
    assert resultado_falha == -1
    pass
