import mysql.connector
import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

janela.title('Cadastro De Pessoas')

label_nome = tk.Label(text="Nome Completo :")
label_nome.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)


entry_nome = tk.Entry()
entry_nome.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_tipo_cpf = tk.Label(text="CPF :")
label_tipo_cpf.grid(row=3, column=0, padx=10, pady=10,
                    sticky='nswe', columnspan=2)

entry_cpf = tk.Entry()
entry_cpf.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)


label_idade = tk.Label(text="Idade :")
label_idade.grid(row=5, column=0, padx=10, pady=10,
                 sticky='nswe', columnspan=4)


entry_idade = tk.Entry()
entry_idade.grid(row=6, column=0, padx=10, pady=10,
                 sticky='nswe', columnspan=4)


label_sexo = tk.Label(text="Selecione o Sexo :")
label_sexo.grid(row=7, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

combobox_selecionar_tipo = ttk.Combobox(values="Masculino Feminino")
combobox_selecionar_tipo.grid(
    row=7, column=5, padx=10, pady=10, sticky='nswe', columnspan=4)


label_peso = tk.Label(text="Peso Do Paciente :")
label_peso.grid(row=8, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

entry_peso = tk.Entry()
entry_peso.grid(row=9, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_imc = tk.Label(text="IMC :")
label_imc.grid(row=10, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

entry_imc = tk.Entry()
entry_imc.grid(row=11, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

botao_inserir_tabela = ttk.Button(text="Inserir Dados")
botao_inserir_tabela.grid(row=11, column=10, padx=10,
                          pady=10, sticky='nswe', columnspan=4)

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='',
)
cursor = conexao.cursor()

nome_paciente = ""
cpf_paciente = ""
idade_paciente = ""
sexo_paciente = ""
peso_paciente = ""
imc_paciente = ""
comando = f'INSERT INTO pacientes (nome_paciente, cpf_pacientes, idade_pacientes, sexo_pacientes, peso_pacientes, imc_pacientes) VALUES ("{nome_paciente}", "{cpf_paciente}", "{idade_paciente}", "{sexo_paciente}", "{peso_paciente}", "{imc_paciente}")'
cursor.execute(comando)
conexao.commit()  # edita o banco de dados

janela.mainloop()
