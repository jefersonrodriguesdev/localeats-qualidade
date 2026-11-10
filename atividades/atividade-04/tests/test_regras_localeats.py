import pytest
from src.regras_localeats import pedido_atingiu_valor_minimo

# Responsável: Jeferson Rodrigues
def test_pedido_atinge_valor_minimo_com_sucesso():
    # Arrange
    valor = 30.00
    # Act
    resultado = pedido_atingiu_valor_minimo(valor)
    # Assert
    assert resultado is True

# Responsável: Jeferson Rodrigues
def test_pedido_recusado_abaixo_do_minimo():
    # Arrange
    valor = 29.99
    # Act
    resultado = pedido_atingiu_valor_minimo(valor)
    # Assert
    assert resultado is False

# Responsável: Jeferson Rodrigues
def test_rejeita_valor_negativo_com_excecao():
    # Arrange
    valor_invalido = -5.00
    # Act & Assert
    with pytest.raises(ValueError, match="O valor não pode ser negativo!"):
        pedido_atingiu_valor_minimo(valor_invalido)