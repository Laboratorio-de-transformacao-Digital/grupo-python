import plotly.graph_objects as go
# Adicionando Bairros e sua media de idade
x = ['Kobrasol', 'Barreiros', 'Forquilhas', 'Campinas', 'Areias']
y = [31, 26, 32, 23, 23]

# Configurando o hovertext:
# texto que aparece quando passa o cursor do mouse sobre a barra de informações do gráfico. 
# Adicionando os nomes,renda,emprego procurado,curso necessário e escolaridade de cada um pedidos
fig = go.Figure(data=[go.Bar(x=x, y=y,
                             hovertext=['Nome: João e Juliana<br>Média de Renda: R$ 1.800,00<br>Emprego Procurado: Pedreiro(a)<br>Curso Necessário: Construção Civil<br>Escolaridade: Ensino Médio',
                                        'Nome: Maria e Carla<br>Média de Renda: R$ 1.600,00<br>Emprego Procurado: Carpinteiro(a)<br>Curso Necessário: Marcenaria <br>Escolaridade: Ensino Fundamental, Ensino Médio',
                                        'Nome: José e Marcelo<br>Média de Renda: R$ 2.000,00<br>Emprego Procurado: Pedreiro(a)<br>Curso Necessário: Construção Civil<br>Escolaridade: Ensino Médio',
                                        'Nome: Pedro e Ana<br>Média de Renda: R$ 2.000,00<br>Emprego Procurado: Pedreiro(a)<br>Curso Necessário: Construção Civil<br>Escolaridade: Ensino Fundamental, Ensino Médio',
                                        'Nome: Lucas e Camila<br>Média de Renda: R$ 1.600,00<br>Emprego Procurado: Carpinteiro(a)<br>Curso Necessário: Marcenaria<br>Escolaridade: Ensino Fundamental, Ensino Médio', ''])])

# Customizando...
fig.update_traces(marker_color='white', marker_line_color='rgb(8,48,107)', marker_line_width=0.0, opacity=0.7)
fig.update_layout(
    title_text='Estatísticas de Emprego por Bairro em São José',
    title_font=dict(size=25, color='white', family="Arial, sans-serif", weight="bold"),  # Definindo tamanho,fonte das letras e cor do título
    title_x=0.4,  # Centralizando o título
    yaxis_title=dict(text='Média de idade', font=dict(size=13, color='white')),
    font=dict(color='white', size=12),  # Definindo cor e tamanho da fonte do texto
    plot_bgcolor='rgb(25, 42, 70)',  # Definindo uma cor de fundo azul escuro 
    paper_bgcolor='rgb(25, 42, 70)',  # Definindo uma cor de fundo azul escuro
    scene=dict(
        xaxis=dict(
            showbackground=False,
            showgrid=False,
            showticklabels=False,
        ),
        yaxis=dict(
            showbackground=False,
            showgrid=False,
            showticklabels=False,
        ),
        zaxis=dict(
            showbackground=False,
            showgrid=False,
            showticklabels=False,
        ),
        camera_eye=dict(x=1.87, y=0.88, z=-0.64),
        aspectmode='manual',
        aspectratio=dict(x=4, y=4, z=2)
    )
)

# Adicionando estatística e media de idade de cada bairro
annotations = [
    dict(
        x='Kobrasol', y=31,
        xref='x', yref='y',
        text='31',
        showarrow=True,
        arrowhead=7,
        ax=0, ay=-40
    ),
    dict(
        x='Barreiros', y=26,
        xref='x', yref='y',
        text='26',
        showarrow=True,
        arrowhead=7,
        ax=0, ay=-40
    ),
    dict(
        x='Forquilhas', y=32,
        xref='x', yref='y',
        text='32',
        showarrow=True,
        arrowhead=7,
        ax=0, ay=-40
    ),
    dict(
        x='Campinas', y=23,
        xref='x', yref='y',
        text='23',
        showarrow=True,
        arrowhead=7,
        ax=0, ay=-40
    ),
    dict(
        x='Areias', y=23,
        xref='x', yref='y',
        text='23',
        showarrow=True,
        arrowhead=7,
        ax=0, ay=-40
    )
]

fig.update_layout(annotations=annotations)

# Adicionando "Bairro" embaixo do gráfico
fig.add_annotation(x=0.0, y=-0.15, xref='paper', yref='paper', text="Bairros", showarrow=False,
                   font=dict(size=12, color="white"))

fig.show()
