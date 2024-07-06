# import streamlit as st
# import pandas as pd

# # Função para autenticação
# def authenticate(tipo):
#     senha = st.text_input(f'Digite a senha para acessar como {tipo}:', type='password')
#     if tipo == 'administrador' and senha == 'box_88T2024':  # Nova senha para administrador
#         return True
#     elif tipo == 'competidor' and senha == 'competidor':  # Nova senha para competidor
#         return True
#     else:
#         st.warning('Senha incorreta. Acesso negado.')
#         return False

# # Inicialização dos dados com os times das categorias
# data_iniciante = pd.DataFrame({
#     'Rank': [1, 2, 3, 4, 5],
#     'Nome': ['Natinha, Pepa, Navarro', 'Gabis, Lívia, Vitoria', 'Kleberson, Juma, Jessica', 'Maria, Fernanda, Vini', 'Giseley, Elis, Cair'],
#     'Prova1': [0, 0, 0, 0, 0],
#     'Prova2': [0, 0, 0, 0, 0],
#     'Prova3': [0, 0, 0, 0, 0],
#     'Prova4': [0, 0, 0, 0, 0],  # Inicializa as provas vazias
#     'Pontuação Total': [0, 0, 0, 0, 0]
# })

# data_scale = pd.DataFrame({
#     'Rank': [1, 2, 3, 4, 5, 6, 7],
#     'Nome': ['Chandelle, Moto', 'Edilton, Luane', 'Thalita, Araújo, Telles', 'Simone, Renato', 'Jenifer S, Diego', 'Ana, Rafa', 'Rose, Paulo', ''],
#     'Prova1': [0, 0, 0, 0, 0, 0, 0],
#     'Prova2': [0, 0, 0, 0, 0, 0, 0],
#     'Prova3': [0, 0, 0, 0, 0, 0, 0],
#     'Prova4': [0, 0, 0, 0, 0, 0, 0],
#     'Pontuação Total': [0, 0, 0, 0, 0, 0, 0]
# })

# data_rx = pd.DataFrame({
#     'Rank': [1, 2, 3],
#     'Nome': ['Willian, Karen', 'Gustavo, Karina', 'Guto, Eliene75'],
#     'Prova1': [0, 0, 0],
#     'Prova2': [0, 0, 0],
#     'Prova3': [0, 0, 0],
#     'Prova4': [0, 0, 0],
#     'Pontuação Total': [0, 0, 0]
# })

# # Função para calcular a pontuação total
# def calcular_pontuacao_total(df):
#     df['Pontuação Total'] = df[['Prova1', 'Prova2', 'Prova3', 'Prova4']].sum(axis=1)
#     return df

# # Título da aplicação
# st.title('Leaderboard - Box 88 GAMES 2024')

# # Autenticação como administrador ou competidor
# tipo_acesso = st.radio('Você é:', ['administrador', 'competidor'])

# if authenticate(tipo_acesso):
#     if tipo_acesso == 'administrador':
#         # Selecionar ação (administração ou visualização apenas leitura)
#         acao = st.selectbox('Selecione ação:', ['Visualizar Leaderboard por Categoria', 'Atualizar Pontuação'])

#         if acao == 'Visualizar Leaderboard por Categoria':
#             st.subheader('Visualizar Leaderboard por Categoria')
#             categoria_selecionada = st.selectbox('Selecione a categoria:', ['Iniciante', 'Scale', 'RX'])
            
#             if categoria_selecionada == 'Iniciante':
#                 data_iniciante = calcular_pontuacao_total(data_iniciante)
#                 st.dataframe(data_iniciante.set_index('Rank').style.set_properties(**{'text-align': 'left'}), height=400)
#             elif categoria_selecionada == 'Scale':
#                 data_scale = calcular_pontuacao_total(data_scale)
#                 st.dataframe(data_scale.set_index('Rank').style.set_properties(**{'text-align': 'left'}), height=400)
#             elif categoria_selecionada == 'RX':
#                 data_rx = calcular_pontuacao_total(data_rx)
#                 st.dataframe(data_rx.set_index('Rank').style.set_properties(**{'text-align': 'left'}), height=400)

#             st.write(f"Visualizando times para a categoria '{categoria_selecionada}'.")
#             st.write("Apenas visualização. Competidores não podem editar os dados.")

#         elif acao == 'Atualizar Pontuação':
#             st.subheader('Atualizar Pontuação')
#             categoria_selecionada = st.selectbox('Selecione a categoria:', ['Iniciante', 'Scale', 'RX'])

#             if categoria_selecionada == 'Iniciante':
#                 st.write("Selecione o competidor para atualizar:")
#                 competidor = st.selectbox('Selecione o competidor:', data_iniciante['Nome'])
#                 prova = st.selectbox('Selecione a prova:', ['Prova1', 'Prova2', 'Prova3', 'Prova4'])
#                 nova_pontuacao = st.number_input(f'Nova pontuação para {prova}:', min_value=0)

#                 if st.button('Atualizar'):
#                     data_iniciante.loc[data_iniciante['Nome'] == competidor, prova] = nova_pontuacao
#                     data_iniciante = calcular_pontuacao_total(data_iniciante)
#                     st.success(f'Pontuação atualizada para {prova} para o competidor {competidor}!')

#             elif categoria_selecionada == 'Scale':
#                 st.write("Selecione o competidor para atualizar:")
#                 competidor = st.selectbox('Selecione o competidor:', data_scale['Nome'])
#                 prova = st.selectbox('Selecione a prova:', ['Prova1', 'Prova2', 'Prova3', 'Prova4'])
#                 nova_pontuacao = st.number_input(f'Nova pontuação para {prova}:', min_value=0)

#                 if st.button('Atualizar'):
#                     data_scale.loc[data_scale['Nome'] == competidor, prova] = nova_pontuacao
#                     data_scale = calcular_pontuacao_total(data_scale)
#                     st.success(f'Pontuação atualizada para {prova} para o competidor {competidor}!')

#             elif categoria_selecionada == 'RX':
#                 st.write("Selecione o competidor para atualizar:")
#                 competidor = st.selectbox('Selecione o competidor:', data_rx['Nome'])
#                 prova = st.selectbox('Selecione a prova:', ['Prova1', 'Prova2', 'Prova3', 'Prova4'])
#                 nova_pontuacao = st.number_input(f'Nova pontuação para {prova}:', min_value=0)

#                 if st.button('Atualizar'):
#                     data_rx.loc[data_rx['Nome'] == competidor, prova] = nova_pontuacao
#                     data_rx = calcular_pontuacao_total(data_rx)
#                     st.success(f'Pontuação atualizada para {prova} para o competidor {competidor}!')

#     elif tipo_acesso == 'competidor':
#         # Função para visualizar leaderboard como competidor
#         def view_leaderboard_competidor():
#             st.subheader('Leaderboard - Visualização Competidor')

#             st.write("Times da categoria Iniciante:")
#             st.dataframe(data_iniciante.set_index('Rank').style.set_properties(**{'text-align': 'left'}), height=200)

#             st.write("Times da categoria Scale:")
#             st.dataframe(data_scale.set_index('Rank').style.set_properties(**{'text-align': 'left'}), height=200)

#             st.write("Times da categoria RX:")
#             st.dataframe(data_rx.set_index('Rank').style.set_properties(**{'text-align': 'left'}), height=200)

#             st.write("Apenas visualização. Competidores não podem editar os dados.")

#         # Exibir leaderboard para competidor
#         view_leaderboard_competidor()

# else:
#     st.warning('Por favor, insira a senha correta para acessar.')





import streamlit as st
import pandas as pd

# Função para autenticação
def authenticate(tipo):
    senha = st.text_input(f'Digite a senha para acessar como {tipo}:', type='password')
    if tipo == 'administrador' and senha == 'box_88T2024':  # Nova senha para administrador
        return True
    elif tipo == 'competidor' and senha == 'competidor':  # Nova senha para competidor
        return True
    else:
        st.warning('Senha incorreta. Acesso negado.')
        return False

# Inicialização dos dados com os times das categorias
data_iniciante = pd.DataFrame({
    'Rank': [1, 2, 3, 4, 5],
    'Nome': ['LOS PEPITOS', 'A TROPA DOS NO REP', 'RX JUNIOR', 'INIMIGOS DO CARDIO', 'ROUGE '],
    'Prova1': [0, 0, 0, 0, 0],
    'Prova2': [0, 0, 0, 0, 0],
    'Prova3': [0, 0, 0, 0, 0],
    'Prova4': [0, 0, 0, 0, 0],  # Inicializa as provas vazias
    'Pontuação Total': [0, 0, 0, 0, 0]
})

data_scale = pd.DataFrame({
    'Rank': [1, 2, 3, 4, 5, 6],
    'Nome': [ 'GUERREIROS DO SAMU', 'NAO TEM GALANTIA', 'MOTOR MARCHA LENTA','CROSSFAKE', 'MC FERROU E MC DEU MAL', 'RX NA PROXIMA'],
    'Prova1': [ 0, 0, 0, 0, 0, 0],
    'Prova2': [ 0, 0, 0, 0, 0, 0],
    'Prova3': [ 0, 0, 0, 0, 0, 0],
    'Prova4': [ 0, 0, 0, 0, 0, 0],
    'Pontuação Total': [ 0, 0, 0, 0, 0, 0]
})

data_rx = pd.DataFrame({
    'Rank': [1, 2, 3],
    'Nome': ['SEM NO RAP', 'CROSSFRITO', 'RX FAKE'],
    'Prova1': [0, 0, 0],
    'Prova2': [0, 0, 0],
    'Prova3': [0, 0, 0],
    'Prova4': [0, 0, 0],
    'Pontuação Total': [0, 0, 0]
})

# Função para calcular a pontuação total
def calcular_pontuacao_total(df):
    df['Pontuação Total'] = df[['Prova1', 'Prova2', 'Prova3', 'Prova4']].sum(axis=1)
    return df

# Função para estilizar a tabela com destaque para maior e menor pontuação
def style_table(df):
    styled_df = df.style.format({"Pontuação Total": "{:.0f}"})\
                         .highlight_max(subset="Pontuação Total", color='lightgreen')\
                         .highlight_min(subset="Pontuação Total", color='lightcoral')\
                         .set_table_styles([
                             {'selector': 'thead th', 'props': [('background-color', '#f4f4f4'), ('font-weight', 'bold')]},
                             {'selector': 'tbody tr:nth-child(even)', 'props': [('background-color', '#f9f9f9')]},
                             {'selector': 'tbody tr:hover', 'props': [('background-color', '#f1f1f1')]}
                         ])
    return styled_df

# Título da aplicação
st.title('Leaderboard - Box 88 GAMES 2024')

# Autenticação como administrador ou competidor
tipo_acesso = st.radio('Você é:', ['administrador', 'competidor'])

if authenticate(tipo_acesso):
    if tipo_acesso == 'administrador':
        # Selecionar ação (administração ou visualização apenas leitura)
        acao = st.selectbox('Selecione ação:', ['Visualizar Leaderboard por Categoria', 'Atualizar Pontuação'])

        if acao == 'Visualizar Leaderboard por Categoria':
            st.subheader('Visualizar Leaderboard por Categoria')
            categoria_selecionada = st.selectbox('Selecione a categoria:', ['Iniciante', 'Scale', 'RX'])
            
            if categoria_selecionada == 'Iniciante':
                data_iniciante = calcular_pontuacao_total(data_iniciante)
                st.dataframe(style_table(data_iniciante.set_index('Rank').reset_index()), height=400)
            elif categoria_selecionada == 'Scale':
                data_scale = calcular_pontuacao_total(data_scale)
                st.dataframe(style_table(data_scale.set_index('Rank').reset_index()), height=400)
            elif categoria_selecionada == 'RX':
                data_rx = calcular_pontuacao_total(data_rx)
                st.dataframe(style_table(data_rx.set_index('Rank').reset_index()), height=400)

            st.write(f"Visualizando times para a categoria '{categoria_selecionada}'.")
            st.write("Apenas visualização. Competidores não podem editar os dados.")

        elif acao == 'Atualizar Pontuação':
            st.subheader('Atualizar Pontuação')
            categoria_selecionada = st.selectbox('Selecione a categoria:', ['Iniciante', 'Scale', 'RX'])

            if categoria_selecionada == 'Iniciante':
                st.write("Selecione o competidor para atualizar:")
                competidor = st.selectbox('Selecione o competidor:', data_iniciante['Nome'])
                prova = st.selectbox('Selecione a prova:', ['Prova1', 'Prova2', 'Prova3', 'Prova4'])
                nova_pontuacao = st.number_input(f'Nova pontuação para {prova}:', min_value=0)

                if st.button('Atualizar'):
                    data_iniciante.loc[data_iniciante['Nome'] == competidor, prova] = nova_pontuacao
                    data_iniciante = calcular_pontuacao_total(data_iniciante)
                    st.success(f'Pontuação atualizada para {prova} para o competidor {competidor}!')

            elif categoria_selecionada == 'Scale':
                st.write("Selecione o competidor para atualizar:")
                competidor = st.selectbox('Selecione o competidor:', data_scale['Nome'])
                prova = st.selectbox('Selecione a prova:', ['Prova1', 'Prova2', 'Prova3', 'Prova4'])
                nova_pontuacao = st.number_input(f'Nova pontuação para {prova}:', min_value=0)

                if st.button('Atualizar'):
                    data_scale.loc[data_scale['Nome'] == competidor, prova] = nova_pontuacao
                    data_scale = calcular_pontuacao_total(data_scale)
                    st.success(f'Pontuação atualizada para {prova} para o competidor {competidor}!')

            elif categoria_selecionada == 'RX':
                st.write("Selecione o competidor para atualizar:")
                competidor = st.selectbox('Selecione o competidor:', data_rx['Nome'])
                prova = st.selectbox('Selecione a prova:', ['Prova1', 'Prova2', 'Prova3', 'Prova4'])
                nova_pontuacao = st.number_input(f'Nova pontuação para {prova}:', min_value=0)

                if st.button('Atualizar'):
                    data_rx.loc[data_rx['Nome'] == competidor, prova] = nova_pontuacao
                    data_rx = calcular_pontuacao_total(data_rx)
                    st.success(f'Pontuação atualizada para {prova} para o competidor {competidor}!')

    elif tipo_acesso == 'competidor':
        # Função para visualizar leaderboard como competidor
        def view_leaderboard_competidor():
            st.subheader('Leaderboard - Visualização Competidor')

            st.write("Times da categoria Iniciante:")
            st.dataframe(style_table(data_iniciante.set_index('Rank').reset_index()), height=200)

            st.write("Times da categoria Scale:")
            st.dataframe(style_table(data_scale.set_index('Rank').reset_index()), height=200)

            st.write("Times da categoria RX:")
            st.dataframe(style_table(data_rx.set_index('Rank').reset_index()), height=200)

            st.write("Apenas visualização. Competidores não podem editar os dados.")

        # Exibir leaderboard para competidor
        view_leaderboard_competidor()

else:
    st.warning('Por favor, insira a senha correta para acessar o app.')



