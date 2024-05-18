import plotly.graph_objects as go

x = ['Kobrasol', 'Barreiros', 'Forquilhas', 'Campinas', 'Areias']
y = [31,26, 32, 23, 23, ]


# Use the hovertext kw argument for hover text
fig = go.Figure(data=[go.Bar(x=x, y=y,
            hovertext=['Nome:João e Juliana<br>Média de Renda:R$ 1.800,00<br>Emprego Procurado:Pedreiro(a)<br>Curso Necessário:Construção Civil<br>Escolaridade:Ensino Medio', 'Nome:Maria e Carla<br>Média de Renda:R$ 1.600,00<br>Emprego Procurado:Carpinteiro(a)<br>Curso Necessário:Marcenaria <br>Escolaridade:Ensino Fundamental,Ensino Medio', 'Nome:José  e Marcelo<br>Média de Renda:R$ 2.000,00<br>Emprego Procurado:Pedreiro(a)<br>Curso Necessário:Construção Civil<br>Escolaridade:Ensino Medio', 'Nome:Pedro e Ana<br>Média de Renda:R$ 2.000,00<br>Emprego Procurado:Pedreiro(a)<br>Curso Necessário:Construção Civil<br>Escolaridade:Ensino Fundamental,Ensino Medio', 'Nome:Lucas e Camila<br>Média de Renda:R$ 1.600,00<br>Emprego Procurado:Carpinteiro(a)<br>Curso Necessário:Marcenaria<br>Escolaridade:Ensino Fundamental,Ensino Medio', ''])])


# Customize aspect
fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.5)
fig.update_layout(
    title_text='Estatísticas de Emprego por Bairro em São José',
    yaxis_title=dict(text='Média de idade', font=dict(size=13, color='#182d45')))
fig.show()
