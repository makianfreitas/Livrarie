# Livrarie

import os
import tempfile
import flet as ft
import sqlite3
from flet import FilePicker, FilePickerResultEvent

# Funções para obter os dados das tabelas
def get_disciplinas(professorId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT IdDisciplina, Nome, Descricao, ProfessorId FROM Disciplina WHERE ProfessorId = ?", (professorId,))  # Consulta os dados
    #cursor.execute("SELECT IdDisciplina, Nome, Descricao, ProfessorId FROM Disciplina")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_unique_disciplina_nome(disciplinaId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Nome FROM Disciplina WHERE IdDisciplina = ?", (disciplinaId,))  # Consulta os dados
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_unique_disciplina_descricao(disciplinaId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Descricao FROM Disciplina WHERE IdDisciplina = ?", (disciplinaId,))  # Consulta os dados
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_unique_disciplina_professorid(disciplinaId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT ProfessorId FROM Disciplina WHERE IdDisciplina = ?", (disciplinaId,))  # Consulta os dados
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_unique_professor_nome(professorId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Nome FROM Professor WHERE IdProfessor = ?", (professorId,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_alunos_egenharia():
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Nome FROM Aluno WHERE EG = 1")  # Consulta os dados
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_alunos_metodologia():
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Nome FROM Aluno WHERE MDS = 1")  # Consulta os dados
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_alunos_redes():
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Nome FROM Aluno WHERE RC = 1")  # Consulta os dados
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_alunos_informatica():
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Nome FROM Aluno WHERE IF = 1")  # Consulta os dados
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_alunos_probabilidade():
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Nome FROM Aluno WHERE PE = 1")  # Consulta os dados
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_alunos_economia():
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Nome FROM Aluno WHERE EC = 1")  # Consulta os dados
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_alunos_banco():
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Nome FROM Aluno WHERE BD = 1")  # Consulta os dados
    rows = cursor.fetchall()
    conn.close()
    return rows

def faz_engenharia_de_software(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT EG FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False
    
def faz_metodologia_de_desenvolvimento_de_sistemas(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT MDS FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False
    
def faz_redes_de_computadores(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT RC FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False
    
def faz_informatica(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT IF FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False
    
def faz_probabilidade_e_estatistica(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT PE FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False
    
def faz_economia(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT EC FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False
    
def faz_banco_de_dados(alunoId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT BD FROM Aluno WHERE IdAluno = ?", (alunoId,))
    row = cursor.fetchone()
    conn.close()
    if row[0] == 1:
        return True
    else:
        return False

def get_materiais(disciplinaId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT IdMaterial, Titulo, Arquivo FROM Material WHERE DisciplinaId = ?", (disciplinaId,))  # Consulta os dados
    rows = cursor.fetchall()
    conn.close()
    return rows if rows else None

def salvar_material(titulo, caminho_arquivo, disciplinaId):
    with open(caminho_arquivo, "rb") as arquivo:
        blob = arquivo.read()
    conn = sqlite3.connect("livrarie.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Material (Titulo, Arquivo, DisciplinaId) VALUES (?, ?, ?)", (titulo, blob, disciplinaId))
    conn.commit()
    conn.close()

def apagar_material_do_banco_de_dados(e):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Material WHERE IdMaterial = ?", (materialAtual,))
    conn.commit()
    conn.close()

def get_unique_material_titulo():
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Titulo FROM Material WHERE IdMaterial = ?", (materialAtual,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_unique_material_arquivo():
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Arquivo FROM Material WHERE IdMaterial = ?", (materialAtual,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

disciplinaAtual = -1
professorAtual = 1
alunoAtual = 5
materialAtual = -1

def main(page: ft.Page):
    navigation_stack = [] #Pilha de navegação

    def show_view(view):
        navigation_stack.append(view)
        page.views.clear()
        page.views.extend(navigation_stack)
        page.update()

    def go_back(e):
        if len(navigation_stack) > 1:
            navigation_stack.pop()
            page.views.clear()
            page.views.extend(navigation_stack)
            page.update()

    def refresh_alunos_engenharia():
        alunos_engenharia_list.controls.clear()
        for aluno in get_alunos_egenharia():
            alunos_engenharia_list.controls.append(
                ft.Container(
                    content=ft.Text(value=f'● {aluno[0]}', size=20, color=ft.colors.BLUE_200)
                )
            )
        page.update()
    alunos_engenharia_list = ft.Column()

    def refresh_alunos_metodologia():
        alunos_metodologia_list.controls.clear()
        for aluno in get_alunos_metodologia():
            alunos_metodologia_list.controls.append(
                ft.Container(
                    content=ft.Text(value=f'● {aluno[0]}', size=20, color=ft.colors.BLUE_200)
                )
            )
        page.update()
    alunos_metodologia_list = ft.Column()

    def refresh_alunos_redes():
        alunos_redes_list.controls.clear()
        for aluno in get_alunos_redes():
            alunos_redes_list.controls.append(
                ft.Container(
                    content=ft.Text(value=f'● {aluno[0]}', size=20, color=ft.colors.BLUE_200)
                )
            )
        page.update()
    alunos_redes_list = ft.Column()

    def refresh_alunos_informatica():
        alunos_informatica_list.controls.clear()
        for aluno in get_alunos_informatica():
            alunos_informatica_list.controls.append(
                ft.Container(
                    content=ft.Text(value=f'● {aluno[0]}', size=20, color=ft.colors.BLUE_200)
                )
            )
        page.update()
    alunos_informatica_list = ft.Column()

    def refresh_alunos_probabilidade():
        alunos_probabilidade_list.controls.clear()
        for aluno in get_alunos_probabilidade():
            alunos_probabilidade_list.controls.append(
                ft.Container(
                    content=ft.Text(value=f'● {aluno[0]}', size=20, color=ft.colors.BLUE_200)
                )
            )
        page.update()
    alunos_probabilidade_list = ft.Column()

    def refresh_alunos_economia():
        alunos_economia_list.controls.clear()
        for aluno in get_alunos_economia():
            alunos_economia_list.controls.append(
                ft.Container(
                    content=ft.Text(value=f'● {aluno[0]}', size=20, color=ft.colors.BLUE_200)
                )
            )
        page.update()
    alunos_economia_list = ft.Column()

    def refresh_alunos_banco():
        alunos_banco_list.controls.clear()
        for aluno in get_alunos_banco():
            alunos_banco_list.controls.append(
                ft.Container(
                    content=ft.Text(value=f'● {aluno[0]}', size=20, color=ft.colors.BLUE_200)
                )
            )
        page.update()
    alunos_banco_list = ft.Column()

    def refresh_materiais():
        def abrir_pdf(e):
            global materialAtual
            materialAtual = e.control.data
            arquivo_pdf = get_unique_material_arquivo()
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            temp_file.write(arquivo_pdf)
            temp_file.close()
            page.launch_url(f"file:///{temp_file.name}")
            print(materialAtual)
            def on_close(e):
                if os.path.exists(temp_file.name):
                    os.remove(temp_file.name)
            
            page.on_close = on_close

        def apagar_material(e):
            apagar_material_do_banco_de_dados(e)
            fechar_dialogo_apagar_material(e)
            refresh_materiais()
            page.snack_bar = ft.SnackBar(content=ft.Text('Material apagado com sucesso', size=20))
            page.snack_bar.open = True
            page.update()

        def abrir_dialogo_apagar_material(e):
            global materialAtual
            materialAtual = e.control.data
            print(materialAtual)
            page.overlay.append(dialogoApagarMaterial)
            dialogoApagarMaterial.open = True
            page.update()

        def fechar_dialogo_apagar_material(e):
            dialogoApagarMaterial.open = False
            page.update()

        dialogoApagarMaterial = ft.AlertDialog(
            title=ft.Text('Deseja apagar este material?', color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
            actions=[
                ft.TextButton('Sim', on_click=apagar_material),
                ft.TextButton('Não', on_click=fechar_dialogo_apagar_material)
            ]
        )

        materiais_list.controls.clear()
        if get_materiais(disciplinaAtual) != None:
            for material in get_materiais(disciplinaAtual):
                materiais_list.controls.append(
                    ft.Container(
                        content=ft.ListTile(
                            title=ft.Text(
                                material[1], 
                                size=25, 
                                color=ft.colors.BLUE_200, 
                                weight=ft.FontWeight.BOLD
                            ),
                            data=material[0],
                            on_click=lambda e: abrir_pdf(e),
                            trailing=ft.IconButton(
                                ft.icons.DELETE_ROUNDED, 
                                icon_color=ft.colors.RED_400,
                                data=material[0],
                                on_click=lambda e: abrir_dialogo_apagar_material(e)
                            )
                        ),
                        border_radius=ft.border_radius.all(12),
                        bgcolor=ft.colors.WHITE10
                    )
                )
        materiais_list.controls.append(
                ft.ElevatedButton(
                    content=ft.Text(
                        value='Adicionar material',
                        size=20,
                        color=ft.colors.BLUE_200
                    ),
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.WHITE10,
                        padding=ft.padding.all(20),
                        shape=ft.RoundedRectangleBorder(radius=12),
                        alignment=ft.alignment.center_left
                    ),
                    on_click=lambda e: show_view(adiciona_material_view()),
                    expand=True
                )
            )
        page.update()
    materiais_list = ft.Column()

    def refresh_disciplinas():
        def abrir_pagina_disciplina(e):
            global disciplinaAtual
            disciplinaAtual = e.control.data
            show_view(disciplina_professor_view())

        disciplina_list.controls.clear()  # Limpa a lista
        for disciplina in get_disciplinas(professorAtual):
            disciplina_list.controls.append(
                ft.Container(
                    content=ft.ListTile(
                        title=ft.Text(disciplina[1], size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                        #subtitle=ft.Text(f'Professor(a): {get_unique_professor_nome(disciplina[3])}', size=20, color=ft.colors.BLUE_200),
                        data=disciplina[0],
                        on_click=lambda e: abrir_pagina_disciplina(e)
                    ),
                    border_radius=ft.border_radius.all(12),
                    bgcolor=ft.colors.WHITE10
                )
            )
        page.update()
    disciplina_list = ft.Column()


    # Páginas
    def home_view(): #Página de escolher login
        return ft.View(
            '/',
            [
                ft.Column(
                    controls=[
                        ft.Container(
                            ft.Text('Login', size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                content=ft.Text('Aluno', size=20), 
                                on_click=lambda _: show_view(login_aluno_view()), 
                                width=300, 
                                color=ft.colors.BLUE_200,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.WHITE10,
                                    padding=ft.padding.all(20),
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                )
                            ), 
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                content=ft.Text('Professor', size=20), 
                                on_click=lambda _: show_view(login_professor_view()), 
                                width=300, 
                                color=ft.colors.BLUE_200,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.WHITE10,
                                    padding=ft.padding.all(20),
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                )
                            ), 
                            alignment=ft.alignment.center
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                )
            ]
        )
    
    def login_aluno_view(): #Página de login do aluno
        return ft.View(
            '/loginAluno',
            [
                ft.Column(
                    controls=[
                        ft.Row(
                            [
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=go_back),
                                            ft.Text('Login Aluno', size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200)
                                        ]
                                    ),
                                    width=300
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [entradaMatricula],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [entradaSenha],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                content=ft.Text('Entrar', size=18), 
                                on_click=loginAluno, 
                                width=150, 
                                color=ft.colors.BLUE_200,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.WHITE10,
                                    padding=ft.padding.all(18),
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                )
                            ), 
                            alignment=ft.alignment.center
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                )
            ]
        )

    def login_professor_view(): #Página de login do professor
        return ft.View(
            '/loginProfessor',
            [
                ft.Column(
                    controls=[
                        ft.Row(
                            [
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=go_back),
                                            ft.Text('Login Professor', size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200)
                                        ]
                                    ),
                                    width=300
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [entradaMatricula],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [entradaSenha],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                content=ft.Text('Entrar', size=18), 
                                on_click=loginProfessor, 
                                width=150, 
                                color=ft.colors.BLUE_200,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.WHITE10,
                                    padding=ft.padding.all(18),
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                )
                            ), 
                            alignment=ft.alignment.center
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                )
            ]
        )

    def area_aluno_view(): #Área do aluno
        def abrir_tela_disciplina(disciplinaId):
            global disciplinaAtual
            disciplinaAtual = disciplinaId
            show_view(disciplina_aluno_view())

        def abrir_dialogo(e):
            page.overlay.append(caixaDialogo)
            caixaDialogo.open = True
            page.update()

        def fechar_dialogo(e):
            caixaDialogo.open = False
            page.update()

        caixaDialogo = ft.AlertDialog(
            title=ft.Text('Deseja sair da área do aluno?', color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
            actions=[
                ft.TextButton('Sim', on_click=go_back),
                ft.TextButton('Não', on_click=fechar_dialogo)
            ]
        )

        areaView = ft.View(
            '/areaAluno',
            [
                # Página inicial do aluno
                ft.Column(
                    [
                        # Cabeçalho da página
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Text(
                                                'Livrarie Aluno', 
                                                size=40, 
                                                weight=ft.FontWeight.BOLD, 
                                                color=ft.colors.BLACK87
                                            ),
                                            ft.TextButton(
                                                text='Sair',
                                                style=ft.ButtonStyle( 
                                                    color=ft.colors.BLACK87
                                                ),
                                                on_click=abrir_dialogo
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    padding=ft.padding.all(20), 
                                    bgcolor=ft.colors.BLUE_200, 
                                    border_radius=12, 
                                    expand=True
                                )
                            ]
                        ),
                        
                        # Seção principal com as disciplinas e atividades pendentes
                        ft.Row(
                            [
                                # Coluna das disciplinas
                                ft.Column(
                                    [
                                        ft.Container(
                                            content=ft.Text('Disciplinas matriculadas', size=20, color=ft.colors.BLUE_200), 
                                            padding=ft.padding.only(left=20, top=12)
                                        ),

                                        # Coluna de Disciplinas Matriculadas
                                        ft.Column(
                                            [
                                                ft.Row( # Engenharia de Software
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(1), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(1)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_disciplina(1),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_engenharia_de_software(alunoAtual),
                                                    expand=True
                                                ),

                                                ft.Row( # Metodologia de Desenvolvimento de Sistemas
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(2), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(2)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_disciplina(2),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_metodologia_de_desenvolvimento_de_sistemas(alunoAtual),
                                                    expand=True
                                                ),
                                            
                                                ft.Row( # Redes de Computadores
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(3), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(3)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_disciplina(3),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_redes_de_computadores(alunoAtual),
                                                    expand=True
                                                ),
                                            
                                                ft.Row( # Informática
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(4), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(4)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_disciplina(4),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_informatica(alunoAtual),
                                                    expand=True
                                                ),
                                            
                                                ft.Row( # Probabilidade e Estatística
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(5), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(5)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_disciplina(5),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_probabilidade_e_estatistica(alunoAtual),
                                                    expand=True
                                                ),
                                            
                                                ft.Row( # Economia
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(6), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(6)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_disciplina(6),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_economia(alunoAtual),
                                                    expand=True
                                                ),
                                            
                                                ft.Row( # Banco de Dados
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text(value=get_unique_disciplina_nome(7), size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(7)), size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            on_click=lambda e: abrir_tela_disciplina(7),
                                                            expand=True
                                                        ),
                                                    ],
                                                    visible=faz_banco_de_dados(alunoAtual),
                                                    expand=True
                                                ),
                                            ],
                                            scroll='auto',
                                            alignment=ft.alignment.top_center,
                                            expand=True
                                        )
                                    ],
                                    expand=True
                                ),
                                
                                # Coluna de Atividades Pendentes
                                ft.Column(
                                    [
                                        ft.Container(
                                            content=ft.Text('Atividades pendentes', size=20, color=ft.colors.BLUE_200), 
                                            padding=ft.padding.only(left=20, top=12)
                                        ),
                                        ft.ElevatedButton(
                                            content=ft.Column(
                                                [
                                                    ft.Row(
                                                        [
                                                            ft.Column(
                                                                [
                                                                    ft.Text('Projeto - Segunda etapa', size=24, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Metodologia de Desenvolvimento de Sistemas 2', size=18, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            ft.Text('Prazo de entrega:\n13/11/2024, 08:00', color=ft.colors.RED_500)
                                                        ]
                                                    ),
                                                    ft.Row(
                                                        [
                                                            ft.Column(
                                                                [
                                                                    ft.Text('Lista 1', size=24, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Economia', size=18, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            ft.Text('Prazo de entrega:\n15/11/2024, 23:59', color=ft.colors.BLUE_200)
                                                        ]
                                                    )
                                                ],
                                                spacing=20
                                            ),
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.colors.WHITE10,
                                                padding=ft.padding.all(20),
                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                alignment=ft.alignment.center_left
                                            ),
                                            expand=True
                                        )
                                    ],
                                    expand=True  # Expande a coluna para ocupar o espaço verticalmente
                                )
                            ],
                            expand=True  # Expande a Row para ocupar o espaço horizontalmente
                        )
                    ],
                    expand=True  # Expande a Column principal para ocupar o espaço vertical da página
                )
            ]
        )
        refresh_disciplinas()
        return areaView

    def area_professor_view(): #Área do professor
        def abrir_dialogo(e):
            page.overlay.append(caixaDialogo)
            caixaDialogo.open = True
            page.update()

        def fechar_dialogo(e):
            caixaDialogo.open = False
            page.update()
            
        caixaDialogo = ft.AlertDialog(
            title=ft.Text('Deseja sair da área do professor?', color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
            actions=[
                ft.TextButton('Sim', on_click=go_back),
                ft.TextButton('Não', on_click=fechar_dialogo)
            ]
        )

        areaView = ft.View(
            '/areaProfessor',
            [
                # Página inicial do professor
                ft.Column(
                    [
                        # Cabeçalho da página
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Text(
                                                'Livrarie Professor', 
                                                size=40, 
                                                weight=ft.FontWeight.BOLD, 
                                                color=ft.colors.BLACK87
                                            ),
                                            ft.TextButton(
                                                text='Sair',
                                                style=ft.ButtonStyle( 
                                                    color=ft.colors.BLACK87
                                                ),
                                                on_click=abrir_dialogo
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    padding=ft.padding.all(20), 
                                    bgcolor=ft.colors.BLUE_200, 
                                    border_radius=12, 
                                    expand=True
                                )
                            ]
                        ),
                        # Seção principal com as disciplinas e atividades pendentes
                        ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Container(
                                            content=ft.Text('Disciplinas atribuídas', size=20, color=ft.colors.BLUE_200), 
                                            padding=ft.padding.only(left=20, top=12)
                                        ),

                                        # Coluna de Disciplinas Matriculadas
                                        ft.Column(
                                            [disciplina_list],
                                            scroll='auto',
                                            alignment=ft.alignment.top_center,
                                            expand=True
                                        )
                                    ],
                                    expand=True
                                )
                            ],
                            expand=True  # Expande a Row para ocupar o espaço horizontalmente
                        )
                    ],
                    expand=True  # Expande a Column principal para ocupar o espaço vertical da página
                )
            ]
        )
        refresh_disciplinas()
        return areaView

    def disciplina_aluno_view(): #Página de detalhes da matéria do aluno
        return ft.View(
            '/disciplinaAluno',
            [
                ft.Column(
                    [
                        # Cabeçalho da página
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=go_back, icon_color=ft.colors.BLACK87),
                                            ft.Text(
                                                value=get_unique_disciplina_nome(disciplinaAtual), 
                                                size=40, 
                                                weight=ft.FontWeight.BOLD, 
                                                color=ft.colors.BLACK87
                                            )
                                        ]
                                    ),
                                    padding=ft.padding.all(20), 
                                    bgcolor=ft.colors.BLUE_200, 
                                    border_radius=12, 
                                    expand=True
                                )
                            ]
                        ),
                        ft.Container(ft.Text(value=get_unique_professor_nome(get_unique_disciplina_professorid(disciplinaAtual)), size=20, color=ft.colors.BLUE_200), padding=ft.padding.only(left=20, top=12)),
                        ft.Container(
                            content=ft.Text(value=get_unique_disciplina_descricao(disciplinaAtual), size=30, color=ft.colors.BLUE_200),
                            border_radius=ft.border_radius.all(12),
                            bgcolor=ft.colors.WHITE10,
                            padding=ft.padding.all(20)
                        )
                    ],
                    expand=True  # Expande a Column principal para ocupar o espaço vertical da página
                )
            ]
        )

    def disciplina_professor_view(): #Página de detalhes da matéria do professor
        def exibir_alunos():
            match disciplinaAtual:
                case 1:
                    refresh_alunos_engenharia()
                    return alunos_engenharia_list
                case 2:
                    refresh_alunos_metodologia()
                    return alunos_metodologia_list
                case 3:
                    refresh_alunos_redes()
                    return alunos_redes_list
                case 4:
                    refresh_alunos_informatica()
                    return alunos_informatica_list
                case 5:
                    refresh_alunos_probabilidade()
                    return alunos_probabilidade_list
                case 6:
                    refresh_alunos_economia()
                    return alunos_economia_list
                case 7:
                    refresh_alunos_banco()
                    return alunos_banco_list

        disciplinaView = ft.View(
            '/disciplinaProfessor',
            [
                ft.Column(
                    [
                        # Cabeçalho da página
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=go_back, icon_color=ft.colors.BLACK87),
                                            ft.Text(
                                                value=get_unique_disciplina_nome(disciplinaAtual), 
                                                size=40, 
                                                weight=ft.FontWeight.BOLD, 
                                                color=ft.colors.BLACK87
                                            )
                                        ]
                                    ),
                                    padding=ft.padding.all(20), 
                                    bgcolor=ft.colors.BLUE_200, 
                                    border_radius=12, 
                                    expand=True
                                )
                            ]
                        ),
                        # Seção principal
                        ft.Row(
                            [
                                ft.Column(
                                    [
                                        # Descrição e materiais
                                        ft.Column(
                                            [
                                                ft.Container(
                                                    content=ft.Text('Descrição', size=20, color=ft.colors.BLUE_200), 
                                                    padding=ft.padding.only(left=20, top=12)
                                                ),

                                                ft.Container(
                                                    content=ft.Text(value=get_unique_disciplina_descricao(disciplinaAtual), size=25, color=ft.colors.BLUE_200),
                                                    border_radius=ft.border_radius.all(12),
                                                    bgcolor=ft.colors.WHITE10,
                                                    padding=ft.padding.all(20),
                                                    alignment=ft.alignment.top_center
                                                ),

                                                ft.Container(
                                                    content=ft.Text('Materiais', size=20, color=ft.colors.BLUE_200), 
                                                    padding=ft.padding.only(left=20, top=12)
                                                ),

                                                materiais_list
                                            ],
                                            scroll='auto',
                                            alignment=ft.alignment.top_center,
                                            expand=True
                                        ),
                                    ],
                                    expand=True
                                ),

                                # Alunos matriculados
                                ft.Column(
                                    [
                                        ft.Container(
                                            content=ft.Text('Alunos matriculados', size=20, color=ft.colors.BLUE_200), 
                                            padding=ft.padding.only(left=20, top=12)
                                        ),
                                        ft.Container(
                                            content=ft.Column(
                                                [
                                                    exibir_alunos()
                                                ],
                                                alignment=ft.alignment.top_center,
                                                expand=True
                                            ), 
                                            bgcolor=ft.colors.WHITE10,
                                            border_radius=ft.border_radius.all(12),
                                            padding=ft.padding.all(20),
                                            width=400,
                                            expand=True
                                        )
                                    ]
                                )
                            ],
                            expand=True
                        )
                    ],
                    expand=True  # Expande a Column principal para ocupar o espaço vertical da página
                )
            ]
        )
        refresh_materiais()
        return disciplinaView

    def adiciona_material_view():
        return ft.View(
            '/adicionaMaterial',
            [
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=go_back),
                                            ft.Text('Adição de material', size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200)
                                        ]
                                    ),
                                    width=500
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [entradaNomeMaterial],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                content=ft.Text('Selecionar arquivo', size=18), 
                                on_click=lambda _: file_picker.pick_files(allowed_extensions=["pdf"]),  
                                color=ft.colors.BLUE_200,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.WHITE10,
                                    padding=ft.padding.all(18),
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                )
                            ), 
                            alignment=ft.alignment.center
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                )
            ]
        )

    page.title = "Livrarie"
    page.padding = 20
    show_view(home_view())

    def loginAluno(e):
        if not entradaMatricula.value:
            entradaMatricula.error_text = 'Preencha a matrícula'
            page.update()
        elif not entradaSenha.value:
            entradaSenha.error_text = 'Preencha a senha'
            page.update()
        else:
            show_view(area_aluno_view())

    def loginProfessor(e):
        if not entradaMatricula.value:
            entradaMatricula.error_text = 'Preencha a matrícula'
            page.update()
        elif not entradaSenha.value:
            entradaSenha.error_text = 'Preencha a senha'
            page.update()
        else:
            show_view(area_professor_view())

    def seleciona_arquivo(e: FilePickerResultEvent):
        if not entradaNomeMaterial.value:
            entradaNomeMaterial.error_text = 'Preencha o título'
            page.update()
        elif e.files:
            arquivo_selecionado = e.files[0].path
            if arquivo_selecionado:
                salvar_material(entradaNomeMaterial.value, arquivo_selecionado, disciplinaAtual)
                go_back(e)
                refresh_materiais()
                page.snack_bar = ft.SnackBar(content=ft.Text('Material adicionado com sucesso', size=20))
                page.snack_bar.open = True
                page.update()
                print('Material salvo')
            else:
                print('Selecione um arquivo')

    file_picker = FilePicker(on_result=seleciona_arquivo)
    page.overlay.append(file_picker)

    entradaNomeMaterial = ft.TextField(label='Título do material', border_color=ft.colors.WHITE60, focused_border_color=ft.colors.BLUE_200, width=500)
    entradaMatricula = ft.TextField(label='Matrícula', border_color=ft.colors.WHITE60, focused_border_color=ft.colors.BLUE_200)
    entradaSenha = ft.TextField(label='Senha', password=True, border_color=ft.colors.WHITE60, focused_border_color=ft.colors.BLUE_200)

    page.update()

ft.app(target=main)
