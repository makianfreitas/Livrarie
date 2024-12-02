import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page: ft.Page):

    def route_change(route):
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
                                ft.Container(
                                    ft.Text('Login Aluno', size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
                                    alignment=ft.alignment.center
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
                                ft.Container(
                                    ft.Text('Login Professor', size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
                                    alignment=ft.alignment.center
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
                                                    [
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Metodologia de Desenvolvimento de Sistemas 2', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Curso: Sistemas de Informação', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1920,
                                                            on_click=lambda _: page.go('/materia')
                                                        ),
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Redes de Computadores', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Curso: Sistemas de Informação', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1920,
                                                            on_click=lambda _: page.go('/materia')
                                                        ),
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Informática', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Curso: Sistemas de Informação', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1920,
                                                            on_click=lambda _: page.go('/materia')
                                                        ),
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Probabilidade e Estatística', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Curso: Sistemas de Informação', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1920,
                                                            on_click=lambda _: page.go('/materia')
                                                        ),
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Psicologia Aplicada às Organizações', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Curso: Sistemas de Informação', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1920,
                                                            on_click=lambda _: page.go('/materia')
                                                        ),
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Economia', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Curso: Sistemas de Informação', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1920,
                                                            on_click=lambda _: page.go('/materia')
                                                        ),
                                                        ft.ElevatedButton(
                                                            content=ft.Column(
                                                                [
                                                                    ft.Text('Banco de Dados', size=30, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                                                    ft.Text('Curso: Sistemas de Informação', size=20, color=ft.colors.BLUE_200)
                                                                ],
                                                                expand=True
                                                            ),
                                                            style=ft.ButtonStyle(
                                                                bgcolor=ft.colors.WHITE10,
                                                                padding=ft.padding.all(20),
                                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                                alignment=ft.alignment.center_left
                                                            ),
                                                            width=1920,
                                                            on_click=lambda _: page.go('/materia')
                                                        )
                                                    ],
                                                    scroll='auto',
                                                    alignment=ft.alignment.top_center,
                                                    expand=True  # Expande a coluna para ocupar o espaço verticalmente
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
                                ft.Text('[Disciplina]', size=40, color=ft.colors.BLUE_200, weight=ft.FontWeight.BOLD),
                                ft.Text('[Professor]', size=20, color=ft.colors.BLUE_200),
                                ft.Text('[Ementa]', size=30, color=ft.colors.BLUE_200)
                            ],
                            expand=True  # Expande a Column principal para ocupar o espaço vertical da página
                        )
                    ]
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1] if page.views else None
        if top_view:
            page.go(top_view.route)

    page.title = "Livrarie"
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    '''page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER'''
    page.padding = 20
    page.go('/')

    def loginAluno(e):
        if not entradaMatricula.value:
            entradaMatricula.error_text = 'Preencha a matrícula'
            page.update()
        elif not entradaSenha.value:
            entradaSenha.error_text = 'Preencha a senha'
            page.update()
        else:
            page.go('/areaAluno')

    def loginProfessor(e):
        if not entradaMatricula.value:
            entradaMatricula.error_text = 'Preencha a matrícula'
            page.update()
        elif not entradaSenha.value:
            entradaSenha.error_text = 'Preencha a senha'
            page.update()
        else:
            page.go('/areaProfessor')

    entradaMatricula = ft.TextField(label='Matrícula', border_color=ft.colors.WHITE60, focused_border_color=ft.colors.BLUE_200)
    entradaSenha = ft.TextField(label='Senha', password=True, border_color=ft.colors.WHITE60, focused_border_color=ft.colors.BLUE_200)

    
    
    




    #page.on_resize = lambda e: parteSuperior.update(width=page.width)

    page.update()

ft.app(target=main)

'''# Coluna de Atividades Pendentes
                                        ft.Column(
                                            [
                                                ft.Container(
                                                    content=ft.Text('Mensagens recentes', size=20, color=ft.colors.BLUE_200), 
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
                                        )''''''# Coluna de Atividades Pendentes
                                        ft.Column(
                                            [
                                                ft.Container(
                                                    content=ft.Text('Mensagens recentes', size=20, color=ft.colors.BLUE_200), 
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
                                        )'''