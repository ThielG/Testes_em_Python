import pytest

from PySide6.QtCore import Qt

from consulta_endereco import MainWindow


@pytest.fixture
def app(qtbot):

    test_app = MainWindow()
    qtbot.addWidget(test_app)
    return test_app


def test_address(app, qtbot):
    qtbot.keyClicks(app.campo_cep, '89256000')
    qtbot.mouseClick(app.botao_consultar, Qt.LeftButton)

    assert app.label_logradouro.text() == 'Logradouro: Rua Max Wilhelm'
    assert app.label_bairro.text() == 'Bairro: Vila Baependi'
    assert app.label_localidade.text() == 'Localidade: Jaraguá do Sul'
    assert app.label_uf.text() == 'UF: SC'


def test_clear_address(app, qtbot):
    qtbot.keyClicks(app.campo_cep, '89256000')
    qtbot.mouseClick(app.botao_consultar, Qt.LeftButton)
    qtbot.mouseClick(app.botao_limpar, Qt.LeftButton)

    assert app.label_logradouro.text() == ''
    assert app.label_bairro.text() == ''
    assert app.label_localidade.text() == ''
    assert app.label_uf.text() == ''
