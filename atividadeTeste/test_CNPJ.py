import pytest

from PySide6.QtCore import Qt

from consulta_CNPJ import AplicacaoConsultaCNPJ


@pytest.fixture
def app(qtbot):

    test_app = AplicacaoConsultaCNPJ()
    qtbot.addWidget(test_app)
    return test_app


def test_cnpj_bendito(app, qtbot):
    qtbot.keyClicks(app. cnpj_entrada, '02513147000100')
    qtbot.mouseClick(app.botao_consultar, Qt.LeftButton)

    assert app.campo_nome.text() == 'BENDITO LTDA'


def test_status(app, qtbot):
    qtbot.keyClicks(app.cnpj_entrada, '02513147000100')
    qtbot.mouseClick(app.botao_consultar, Qt.LeftButton)

    assert app.campo_situacao.text() == 'ATIVA'


def test_cep(app, qtbot):
    qtbot.keyClicks(app.cnpj_entrada, '02513147000100')
    qtbot.mouseClick(app.botao_consultar, Qt.LeftButton)

    assert app.campo_cep.text() == '89.256-000'


def test_cnpj_invalid_number(app, qtbot):
    qtbot.keyClicks(app.cnpj_entrada, '1')
    qtbot.mouseClick(app.botao_consultar, Qt.LeftButton)

    assert app.rotulo_resultado.text() == 'CNPJ inválido.'
