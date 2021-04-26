import streamlit as st

st.sidebar.header('Para se inciar o ciclo de cultivo é necessario definir uma meta, mantendo todos envolvidos informando sobre qual o obetivo final da produção. Por isso criamos a Fish Planning, para ajudar você Piscicultor na hora de fazer o planejamento do seu cutivo.')
st.write('')
st.sidebar.header('No início da produção de peixe, é necessário realizar um correto planejamento para a contrução dos viveiros e a infraestrutura de suporte na piscicultura. Assim que for definido qual especie cultivar, e qual o sistema de cultivo, com a finalidade de que se consiga alcançar o objetivo final da produção de peixe para fornecer ao mercado consumidor.')
st.sidebar.subheader('Desenvolvido por acadêmicos do Curso de Engenharia de Pesca, da Universidade Federal do Maranhão - UFMA  campus de Pinheiro.')
st.write('')
st.sidebar.markdown('**Inácio Vinicius**')
st.sidebar.text('ivt.rodrigues@discente.ufma.br')
st.sidebar.markdown('**Kedma Costa**')
st.sidebar.text('kedma.costa@discente.ufma.br')
st.sidebar.markdown('**Paloma Pinheiro**')
st.sidebar.text('palomapinheiro@discente.ufma.br')
st.sidebar.markdown('**Suane Gomes**')
st.sidebar.text('suane.sg@discente.ufma.br')
st.title('Fish Planning 📃')
st.markdown('Olá!  Somos a Fish Planning e vamos te ajudar a fazer o planejamento da sua piscicultura. Realizando os cálculos do Povoamento para seu viveiro e despesca do seu cultivo.')

st.markdown('**Mais informações na descrição.**')
st.write('')

st.markdown('A seguir precisaremos que você nos informe os dados para realizarmos os calculos, por favor.')



st.header('Os cálculos são referentes ao cultivo em viveiro')
st.write('')
nome_da_especie = st.text_input('Qual o nome da espécie cultivada? 🐟', help='O cálculo é apenas referente a espécies de peixes.')

cultivo = st.radio('Selecione',['Cálculo povoamento','cálculo pós cultivo'])
if cultivo == 'Cálculo povoamento':

    st.subheader('Definição da quantidade de peixes na engorda')
    peso_final = st.number_input('Defina o peso final (kg)', value=1.0)
    biomassa_final = st.number_input('Informe a biomassa final (kg)', value=1.0)
    numero_de_peixes = biomassa_final/peso_final
    st.write('A quantidade de peixes na engorda é de', round(numero_de_peixes),'peixes/ha')

    st.subheader('Determinação da quantidade inicial de peixes na alevinagem')
    st.write('')
    mortalidade_ale = st.slider('Taxa de mortalidade (%)',min_value=1.0, max_value=100.0, step=0.5)
    porcentagem = round(numero_de_peixes*mortalidade_ale / 100)   
    final = round(numero_de_peixes + porcentagem)  
    alev_mort = round(final) * round(mortalidade_ale /100) 
    final_alevi = round(final) + round(alev_mort)
    check = st.checkbox('Teve mortalidade na engorda?')
    if check == True:
        mortalidade_engorda = st.slider('Taxa de mortalidade na engorda (%)', min_value=0.01, max_value=0.50, step=0.01)
        porc_2 = round(final_alevi * mortalidade_engorda) 
        fim = round(final_alevi) + round(porc_2)
        st.write('A quantidade de peixes ao final da alevinagem é de',fim,'peixes')
    if check == False:
        st.write('Para a engorda de',round(numero_de_peixes) ,'o produtor deverá comprar',round(final_alevi) ,'alevinos')

    st.subheader('Densidade de estocagem da alevinagem')
    densidade_alevinagem = st.number_input('Informe a densidade',value=1.0)
    calculo_de = biomassa_final / densidade_alevinagem
    st.write('A densidade de estocagem na alevinagem é de',round(calculo_de),'kg/ha')

    st.subheader('Definição do tamanho do tanque de alevinagem')
    kilos = peso_final / 10000
    biomass_estocada_alevino = numero_de_peixes * kilos
    tanque_de_alevinagem = biomass_estocada_alevino / calculo_de
    st.write('Será peciso de uma área de',tanque_de_alevinagem,'ha','por área de alevinos')

#fazer relatório povoamento

if cultivo == 'cálculo pós cultivo':

    st.header('Cálculo referente a despesca')

    st.subheader('Biomassa inicial')
    biomassa_ini = st.number_input('Informe o número de individuos inicial',value=1)
    pes_inic = st.number_input('Informe o peso inicial (kg)',value=1.0)
    cal_biomassa = biomassa_ini * pes_inic
    st.write('A biomassa inicial é',round(cal_biomassa),'Kg')

    st.subheader('Biomassa final')
    num_ind_fi = st.number_input('Informe o número de individuos final',value=1)
    pe_fi = st.number_input('Informe o peso final dos indiviuos (Kg)',value=2.0)
    bio_fim = num_ind_fi * pe_fi
    st.write('A biomassa final é',round(bio_fim),'Kg')

    st.subheader('Ganho de peso absoluto')
    calculo_peso_abs =  pe_fi - pes_inic
    st.write('O ganho de peso absoluto foi',round(calculo_peso_abs),'Kg')

    st.subheader('Ganho de peso relativo')
    ganho_p_rel = 100 * (pe_fi - pes_inic)
    ganho_p_final = ganho_p_rel / pes_inic
    st.write('O ganho de peso relativo é',round(ganho_p_final),'%')

    st.subheader('Sobrevivência')
    sobrevivencia = num_ind_fi * 1
    sobrevivencia_fim = sobrevivencia / cal_biomassa
    st.write('A sobrevivência é de',100-round(sobrevivencia_fim),'%')


    st.subheader('Produção')
    st.write('A produção é de',round(bio_fim),'Kg' )

    st.subheader('Produtividade')
    calc_produtividade = bio_fim - cal_biomassa
    st.write('A produtividade é de',round(calc_produtividade),'Kg/viveiro/ciclo')

    st.subheader('Ganho de biomassa')
    ganho_bio = bio_fim - cal_biomassa
    st.write('O ganho de biomassa é',round(ganho_bio),'Kg')

    st.subheader('Conversão alimentar aparente')
    c_aparente = st.number_input('Informe a quantidade de ração ofertada no viveiro (Kg)',value=1.0)
    conversao = c_aparente / ganho_bio
    st.write('A conversão alimentar aparente é de',conversao,'Kg')


    #colocar o cálculo lm
    from math import log
    st.subheader('Taxa de crescimento específico')
    tempo = st.number_input('Informe o tempo de cultivo (Dias)',value=1)
    taxa_cresc_espec = 100 * (log(pe_fi) - log(pes_inic))
    tx_crescimento = taxa_cresc_espec / tempo
    st.write('A taxa de crescimento específica é',tx_crescimento,'%')