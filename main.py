from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3
import os

numero_id = 0


banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database=''
)


def deletar_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT idpacientes From pacientes")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM pacientes WHERE idpacientes=" + str(valor_id))
    banco.commit()


def gerar_pdf():
    cursor = banco.cursor()

    comando_SQL = "SELECT * FROM pacientes"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("Fichas_pacientes.pdf", pagesize=A3)
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(100, 1150, "Pacientes Cadastrados:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10, 1100, "ID")
    pdf.drawString(50, 1100, "Nome")
    pdf.drawString(130, 1100, "Celular")
    pdf.drawString(220, 1100, "Email")
    pdf.drawString(275, 1100, "Data")
    pdf.drawString(330, 1100, "Peso")
    pdf.drawString(380, 1100, "Imc")
    pdf.drawString(430, 1100, "Altura")
    pdf.drawString(510, 1100, "GCorporal")
    pdf.drawString(620, 1100, "Massa Livre")

    for i in range(0, len(dados_lidos)):
        y = y + 70
        pdf.drawString(10, 1100 - y, str(dados_lidos[i][0]))
        pdf.drawString(50, 1100 - y, str(dados_lidos[i][1]))
        pdf.drawString(165, 1100 - y, str(dados_lidos[i][2]))
        pdf.drawString(220, 1100 - y, str(dados_lidos[i][3]))
        pdf.drawString(385, 1100 - y, str(dados_lidos[i][4]))
        pdf.drawString(480, 1100 - y, str(dados_lidos[i][5]))
        pdf.drawString(550, 1100 - y, str(dados_lidos[i][6]))
        pdf.drawString(400, 1100 - y, str(dados_lidos[i][7]))
        pdf.drawString(480, 1100 - y, str(dados_lidos[i][8]))
        pdf.drawString(590, 1100 - y, str(dados_lidos[i][9]))

    pdf.save()
    print("PDF FOI GERADO COM SUCESSO!")


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.lineEdit_6.text()
    linha7 = formulario.lineEdit_7.text()
    linha8 = formulario.lineEdit_8.text()
    linha9 = formulario.lineEdit_9.text()
    linha10 = formulario.lineEdit_10.text()

    print("Nome Completo", linha1)
    print("Celular", linha2)
    print("Email", linha3)
    print("Data Nascimento", linha5)
    print("Peso", linha6)
    print("IMC", linha7)
    print("Altura", linha8)
    print("Gordura Corporal", linha9)
    print("Massa Livre De Gordura", linha10)
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO pacientes (nome_completo, celular, email, dtnascimento, peso, imc, altura, gcorporal, mlgordura) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )"
    dados = (str(linha1)), (str(linha2)), (str(linha3)), (str(linha5)), (str(
        linha6)), (str(linha7)), (str(linha8)), (str(linha9)), (str(linha10))
    cursor.execute(comando_SQL, dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_5.setText("")
    formulario.lineEdit_6.setText("")
    formulario.lineEdit_7.setText("")
    formulario.lineEdit_8.setText("")
    formulario.lineEdit_9.setText("")
    formulario.lineEdit_10.setText("")


def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM pacientes"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    print(dados_lidos[0][0])

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(10)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 10):
            segunda_tela.tableWidget.setItem(
                i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def editar_dados():
    global numero_id

    linha = segunda_tela.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT idpacientes From pacientes")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute(
        "SELECT * FROM pacientes WHERE idpacientes=" + str(valor_id))
    pacientes = cursor.fetchall()
    tela_editar.show()
    tela_editar.lineEdit.setText(str(pacientes[0][0]))
    tela_editar.lineEdit_2.setText(str(pacientes[0][1]))
    tela_editar.lineEdit_3.setText(str(pacientes[0][2]))
    tela_editar.lineEdit_4.setText(str(pacientes[0][3]))
    tela_editar.lineEdit_5.setText(str(pacientes[0][4]))
    tela_editar.lineEdit_6.setText(str(pacientes[0][5]))
    tela_editar.lineEdit_7.setText(str(pacientes[0][6]))
    tela_editar.lineEdit_8.setText(str(pacientes[0][7]))
    tela_editar.lineEdit_9.setText(str(pacientes[0][8]))
    tela_editar.lineEdit_10.setText(str(pacientes[0][9]))
    numero_id = valor_id


def salvar_dados():

    global numero_id

    nome_completo = tela_editar.lineEdit_2.text()
    celular = tela_editar.lineEdit_3.text()
    email = tela_editar.lineEdit_4.text()
    dtnascimento = tela_editar.lineEdit_5.text()
    peso = tela_editar.lineEdit_6.text()
    imc = tela_editar.lineEdit_7.text()
    altura = tela_editar.lineEdit_8.text()
    gcorporal = tela_editar.lineEdit_9.text()
    mlgordura = tela_editar.lineEdit_10.text()
    
    cursor = banco.cursor()
    cursor.execute("UPDATE pacientes SET nome_completo = '{}', celular = '{}', email = '{}', dtnascimento ='{}',  peso ='{}',  imc ='{}',  altura ='{}',  gcorporal ='{}',  mlgordura ='{}' WHERE idpacientes = {}".format(
        nome_completo, celular, email, dtnascimento, peso, imc, altura, gcorporal, mlgordura, numero_id))
    banco.commit()
    
    tela_editar.close()
    segunda_tela.close()
    chama_segunda_tela()


app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
segunda_tela = uic.loadUi("listar_pacientes.ui")
tela_editar = uic.loadUi("menu_editar.ui")
tela_editar.pushButton.clicked.connect(salvar_dados)
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(gerar_pdf)
segunda_tela.pushButton_2.clicked.connect(deletar_dados)
segunda_tela.pushButton_3.clicked.connect(editar_dados)


formulario.show()
app.exec()
