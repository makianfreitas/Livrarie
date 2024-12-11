#import os
import flet as ft
import sqlite3

#TESTE

#os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

# Função para obter os dados da tabela Disciplina
def get_disciplinas(professorId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    '''cursor.execute("SELECT IdDisciplina, Nome, Descricao FROM Disciplina WHERE ProfessorId = ?", (professorId,))  # Consulta os dados'''
    cursor.execute("SELECT IdDisciplina, Nome, Descricao FROM Disciplina")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_unique_disciplina_nome(disciplinaId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Nome, Descricao FROM Disciplina WHERE IdDisciplina = ?", (disciplinaId,))  # Consulta os dados
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_unique_disciplina_descricao(disciplinaId):
    conn = sqlite3.connect("livrarie.db")  # Conecta ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT Nome, Descricao FROM Disciplina WHERE IdDisciplina = ?", (disciplinaId,))  # Consulta os dados
    row = cursor.fetchone()
    conn.close()
    return row[1] if row else None

materiaAtual = -1

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

    # Função para atualizar a lista de disciplinas na interface
    def refresh_disciplinas():
        def abrir_pagina_materia(e):
            show_view(materia_view())
            global materiaAtual
            #materiaAtual = disciplinaId
            materiaAtual = e.control.data

        disciplina_list.controls.clear()  # Limpa a lista
        for disciplina in get_disciplinas(1):
            global materiaAtual
            materiaAtual = disciplina[0]
            disciplina_list.controls.append(
                ft.ListTile(
                    subtitle=ft.ElevatedButton(
                        content=ft.Column(
                            [
                                ft.Text(disciplina[1], size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                ft.Text('Professor(a): Larissa', size=20, color=ft.colors.BLUE_200)
                            ],
                            expand=True
                        ),
                        style=ft.ButtonStyle(
                            bgcolor=ft.colors.WHITE10,
                            padding=ft.padding.all(20),
                            shape=ft.RoundedRectangleBorder(radius=12),
                            alignment=ft.alignment.center_left
                        ),
                        width=1080,
                        on_click=lambda _: show_view(materia_view())
                    ),
                    #ft.Text(disciplina[1]),  # Nome da disciplina
                    #subtitle=ft.Text(disciplina[2]),  # Descrição da disciplina
                    #leading=ft.Text(str(disciplina[0])),  # IdDisciplina
                )
            )
        page.update()

    # Lista de disciplinas
    disciplina_list = ft.Column()

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
                                'Aluno', 
                                on_click=lambda _: show_view(login_aluno_view()), 
                                width=300, 
                                color=ft.colors.BLUE_200
                            ), 
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            ft.ElevatedButton(
                                'Professor', 
                                on_click=lambda _: show_view(login_professor_view()), 
                                width=300, 
                                color=ft.colors.BLUE_200
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
                            ft.ElevatedButton('Entrar', on_click=loginAluno, width=150, color=ft.colors.BLUE_200), 
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
                            ft.ElevatedButton('Entrar', on_click=loginProfessor, width=150, color=ft.colors.BLUE_200), 
                            alignment=ft.alignment.center
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                )
            ]
        )

    def area_aluno_view(): #Área do aluno
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

        return ft.View(
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
                                ft.Column(
                                    [
                                        ft.Container(
                                            content=ft.Text('Disciplinas matriculadas', size=20, color=ft.colors.BLUE_200), 
                                            padding=ft.padding.only(left=20, top=12)
                                        ),

                                        # Coluna de Disciplinas Matriculadas
                                        ft.Column(
                                            [
                                                ft.ElevatedButton(
                                                    content=ft.Column(
                                                        [
                                                            ft.Text('Metodologia de Desenvolvimento de Sistemas 2', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                            ft.Text('Professor(a): Larissa', size=20, color=ft.colors.BLUE_200)
                                                        ],
                                                        expand=True
                                                    ),
                                                    style=ft.ButtonStyle(
                                                        bgcolor=ft.colors.WHITE10,
                                                        padding=ft.padding.all(20),
                                                        shape=ft.RoundedRectangleBorder(radius=12),
                                                        alignment=ft.alignment.center_left
                                                    ),
                                                    width=1080,
                                                    on_click=lambda _: show_view(materia_view())
                                                ),
                                                ft.ElevatedButton(
                                                    content=ft.Column(
                                                        [
                                                            ft.Text('Redes de Computadores', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                            ft.Text('Professor(a): Fulano da Silva', size=20, color=ft.colors.BLUE_200)
                                                        ],
                                                        expand=True
                                                    ),
                                                    style=ft.ButtonStyle(
                                                        bgcolor=ft.colors.WHITE10,
                                                        padding=ft.padding.all(20),
                                                        shape=ft.RoundedRectangleBorder(radius=12),
                                                        alignment=ft.alignment.center_left
                                                    ),
                                                    width=1080,
                                                    on_click=lambda _: show_view(materia_view())
                                                )
                                            ],
                                            scroll='auto',
                                            alignment=ft.alignment.top_center,
                                            expand=True  # Expande a coluna para ocupar o espaço verticalmente
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
                                            width=1080,
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

    def materia_view(): #Página de detalhes da matéria
        return ft.View(
            '/materia',
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
                                            ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=go_back, icon_color=ft.colors.BLACK87),
                                            ft.Text(
                                                'Livrarie Aluno', 
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
                        ft.Text(value=get_unique_disciplina_nome(materiaAtual), size=40, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                        ft.Text('[Professor]', size=20, color=ft.colors.BLUE_200),
                        ft.Text(value=get_unique_disciplina_descricao(2), size=30, color=ft.colors.BLUE_200)
                    ],
                    expand=True  # Expande a Column principal para ocupar o espaço vertical da página
                )
            ]
        )

    '''def route_change(route):
        page.views.clear()
        if page.route == '/':
            #Página de escolher login
            page.views.append(
                ft.View(
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
                                        'Aluno', 
                                        on_click=lambda _: page.go('/loginAluno'), 
                                        width=300, 
                                        color=ft.colors.BLUE_200
                                    ), 
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    ft.ElevatedButton(
                                        'Professor', 
                                        on_click=lambda _: page.go('/loginProfessor'), 
                                        width=300, 
                                        color=ft.colors.BLUE_200
                                    ), 
                                    alignment=ft.alignment.center
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            expand=True
                        )
                        
                    ]
                )
            )
        elif page.route == '/loginAluno':
            #Pagina de login do aluno
            page.views.append(
                ft.View(
                    '/loginAluno',
                    [
                        ft.Column(
                            controls=[
                                ft.Row(
                                    [
                                        ft.Container(
                                            ft.Row(
                                                [
                                                    ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=lambda _: page.go('/')),
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
                                    ft.ElevatedButton('Entrar', on_click=loginAluno, width=150, color=ft.colors.BLUE_200), 
                                    alignment=ft.alignment.center
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            expand=True
                        )
                    ]
                )
            )
        elif page.route == '/loginProfessor':
            #Pagina de login do professor
            page.views.append(
                ft.View(
                    '/loginProfessor',
                    [
                        ft.Column(
                            controls=[
                                ft.Row(
                                    [
                                        ft.Container(
                                            ft.Row(
                                                [
                                                    ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=lambda _: page.go('/')),
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
                                    ft.ElevatedButton('Entrar', on_click=loginProfessor, width=150, color=ft.colors.BLUE_200), 
                                    alignment=ft.alignment.center
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            expand=True
                        )
                    ]
                )
            )
        elif page.route == '/areaAluno':
            page.views.append(
                ft.View(
                    '/areaAluno',
                    [
                        # Página inicial do aluno
                        ft.Column(
                            [
                                # Cabeçalho da página
                                ft.Row(
                                    [
                                        ft.Container(
                                            content=ft.Text(
                                                'Livrarie Aluno', 
                                                size=40, 
                                                weight=ft.FontWeight.BOLD, 
                                                color=ft.colors.BLACK87
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
                                                    content=ft.Text('Disciplinas matriculadas', size=20, color=ft.colors.BLUE_200), 
                                                    padding=ft.padding.only(left=20, top=12)
                                                ),

                                                # Coluna de Disciplinas Matriculadas
                                                ft.Column(
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Metodologia de Desenvolvimento de Sistemas 2', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Professor(a): Larissa', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1080,
                                                            on_click=lambda _: page.go('/materia')
                                                        ),
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Redes de Computadores', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Professor(a): Fulano da Silva', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1080,
                                                            on_click=lambda _: page.go('/materia')
                                                        ),
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Informática', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Professor(a): Beltrano Almeida', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1080,
                                                            on_click=lambda _: page.go('/materia')
                                                        ),
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Probabilidade e Estatística', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Professor(a): Cleiton', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1080,
                                                            on_click=lambda _: page.go('/materia')
                                                        ),
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Psicologia Aplicada às Organizações', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Professor(a): Berenice', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1080,
                                                            on_click=lambda _: page.go('/materia')
                                                        ),
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Economia', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Professor(a): Lucas', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1080,
                                                            on_click=lambda _: page.go('/materia')
                                                        ),
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Banco de Dados', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Professor(a): Márcia', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1080,
                                                            on_click=lambda _: page.go('/materia')
                                                        )
                                                    ],
                                                    scroll='auto',
                                                    alignment=ft.alignment.top_center,
                                                    expand=True  # Expande a coluna para ocupar o espaço verticalmente
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
                                                    width=1080,
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
            )
        elif page.route == '/areaProfessor':
            page.views.append(
                ft.View(
                    '/areaProfessor',
                    [
                        # Página inicial do aluno
                        ft.Column(
                            [
                                # Cabeçalho da página
                                ft.Row(
                                    [
                                        ft.Container(
                                            content=ft.Text(
                                                'Livrarie Professor', 
                                                size=40, 
                                                weight=ft.FontWeight.BOLD, 
                                                color=ft.colors.BLACK87
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
            )
            refresh_disciplinas()
        elif page.route == '/materia':
            page.views.append(
                ft.View(
                    '/materia',
                    [
                        # Página inicial do aluno
                        ft.Column(
                            [
                                # Cabeçalho da página
                                ft.Row(
                                    [
                                        ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=lambda _: page.go('/areaAluno')),
                                        ft.Container(
                                            content=ft.Text(
                                                'Livrarie Aluno', 
                                                size=40, 
                                                weight=ft.FontWeight.BOLD, 
                                                color=ft.colors.BLACK87
                                            ), 
                                            padding=ft.padding.all(20), 
                                            bgcolor=ft.colors.BLUE_200, 
                                            border_radius=12, 
                                            expand=True
                                        )
                                    ]
                                ),
                                ft.Text(value=get_unique_disciplina_nome(materiaAtual), size=40, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                ft.Text('[Professor]', size=20, color=ft.colors.BLUE_200),
                                ft.Text(value=get_unique_disciplina_descricao(2), size=30, color=ft.colors.BLUE_200)
                            ],
                            expand=True  # Expande a Column principal para ocupar o espaço vertical da página
                        )
                    ]
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        if page.views:
            page.go(page.views[-1].route)

        top_view = page.views[-1] if page.views else None
        if top_view:
            page.go(top_view.route)'''

    page.title = "Livrarie"
    #page.on_route_change = route_change
    #page.on_view_pop = view_pop
    page.padding = 20
    #page.go('/')
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

    entradaMatricula = ft.TextField(label='Matrícula', border_color=ft.colors.WHITE60, focused_border_color=ft.colors.BLUE_200)
    entradaSenha = ft.TextField(label='Senha', password=True, border_color=ft.colors.WHITE60, focused_border_color=ft.colors.BLUE_200)

    page.update()

ft.app(target=main)