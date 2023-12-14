import pytest

from PySide6.QtWidgets import QInputDialog
from PySide6.QtCore import Qt

from doToList import AppListaTarefas


@pytest.fixture
def app(qtbot):

    test_app = AppListaTarefas()
    qtbot.addWidget(test_app)
    return test_app


def test_start_empty(app, qtbot):
    assert app.lista_tarefas.count() == 0


def test_add_task(app, qtbot):
    qtbot.keyClicks(app.txt_tarefa, 'Test Task')
    qtbot.mouseClick(app.btn_adicionar, Qt.LeftButton)

    assert app.lista_tarefas.count() == 1
    assert app.lista_tarefas.item(0).text() == 'Test Task'


def test_delete_task(app, qtbot):
    qtbot.keyClicks(app.txt_tarefa, 'Test Task')
    qtbot.mouseClick(app.btn_adicionar, Qt.LeftButton)

    assert app.lista_tarefas.count() == 1

    app.lista_tarefas.setCurrentRow(0)
    qtbot.mouseClick(app.btn_remover, Qt.LeftButton)

    assert app.lista_tarefas.count() == 0


def test_conclude_task(app, qtbot):
    qtbot.keyClicks(app.txt_tarefa, 'Test Task')

    assert app.lista_tarefas.count() == 1

    app.lista_tarefas.setCurrentRow(0)
    qtbot.mouseClick(app.btn_concluir, Qt.LeftButton)

    assert app.lista_tarefas.item(0).cleckState() == Qt.Checked


def test_edit_task(app, qtbot, monkeypatch):
    qtbot.keyClicks(app.txt_tarefa, 'Test task')
    qtbot.mouseClick(app.btn_adicionar, Qt.LeftButton)

    assert app.lista_tarefas.count() == 1

    app.lista_tarefas.setCurrentRow(0)

    def fake_input_dialog(*args, **kwargs):
        return 'Edited Task', True

    monkeypatch.setattr(QInputDialog, 'getText', fake_input_dialog)
    app.editar_tarefa()

    assert app.lista_tarefas.item(0).text() == 'Edited Task'


def test_cancel_edit_task(app, qtbot, monkeypatch):
    qtbot.keyClicks(app.txt_tarefa, 'Test Task')
    qtbot.mouseClick(app.btn_adicionar, Qt.LeftButton)

    assert app.lista_tarefas.count() == 1

    app.lista_tarefas.setCurrentRow(0)
    monkeypatch.setattr(QInputDialog, 'getText', lambda *args, **kwarks: ('', False))
    app.editar_tarefa()

    assert app.lista_tarefas.item(0).text() == 'Test Task'


def test_edit_task_no_selection(app, qtbot, monkeypatch):
    monkeypatch.setattr(QInputDialog, 'getText', lambda *args, **kwarks: ('New Task', True))
    app.editar_tarefa()

    assert app.lista_tarefas.currentItem() is None
