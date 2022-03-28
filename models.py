class Noticia:
    def __init__(self, id, titulo, resumo, imagem, conteudo, categoria):
        self.__id = id
        self.__titulo = titulo 
        self.__resumo = resumo
        self.__imagem = imagem
        self.__conteudo = conteudo
        self.__categoria = categoria
   
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_resumo(self):
        return self.__resumo

    def get_imagem(self):
        return self.__imagem

    def get_conteudo(self):
        return self.__conteudo

    def get_categoria(self):
        return self.__categoria

lista_noticias = [
    Noticia(0, 'Pela 1ª vez em 20 meses, mapa das UTIs para covid fica todo verde', 'Monitoramento da Fiocruz indica que ocupação está abaixo de 60% em todos os estados', '/static/img/noticia1.jpg', 'Pela primeira vez desde julho de 2020, taxa de ocupação de leitos de UTI Covid-19 para adultos no Brasil está fora da zona de alerta, com taxas inferiores a 60%, informou a Fiocruz nesta sexta-feira (25).', 'Hottest news'),
    Noticia(1, 'Rio começa a aplicar 4ª dose da vacina contra a Covid em pessoas acima de 80 anos', 'Ministério da Saúde recomenda que a aplicação da 4ª dose em idosos acima de 80 anos seja feita quatro meses após a aplicação da 3ª dose.', '/static/img/noticia2.jpg', 'A Prefeitura do Rio começou a aplicar, nesta quinta-feira (24), a 4ª dose da vacina contra a Covid (2ª dose de reforço) em idosos acima de 80 anos. A recomendação é que todas as pessoas que tenham mais de 80 anos procurem uma unidade de saúde para tomar a segunda dose de reforço. As vacinas que serão usadas na cidade do Rio de Janeiro serão a Pfizer, a Jansen e a AstraZeneca, sendo que a Jansen e a AstraZeneca estão disponíveis de imediato em todas as unidades de saúde do Rio. Ainda estamos aguardando novas remessas da Pfizer pelo Ministério da Saúde, explicou o secretário de Saúde, Daniel Soranz.', 'Hottest news'),
    Noticia(2, 'SP promove o "Domingão da Vacinação" para imunização contra Covid-19 e a gripe', 'O Governo de SP, em parceria com os 645 municípios, promove no neste dia 27 o “Domingão da Vacinação” para a imunização de crianças, adultos e idosos contra Covid-19. Além disso, os idosos acima de 80 anos poderão se vacinar contra a gripe.', '/static/img/noticia3.jpg', 'A iniciativa busca ampliar a imunização das crianças de 5 a 11 anos de idade, principalmente com relação a segunda dose contra a COVID-19. No estado 76% do público infantil já tomou a primeira dose, porém apenas 36% receberam as duas doses e completou a imunização, sendo que cerca de 800 mil crianças já poderiam ter recebido a segunda dose. Uma pesquisa da Fundação Seade apontou que 34% dos pais e responsáveis afirmaram que não levaram os filhos para vacinar por falta de tempo.', 'Latest news'),
    Noticia(3, 'O legado da pandemia é tema do 9º fascículo do livro comemorativo dos 60 anos da FAPESP', 'A cronologia das ações de combate ao vírus implementadas pela comunidade cientí­fica paulista é descrita na publicação', '/static/img/noticia4.jpg', 'Os primeiros despachos das agências internacionais de notícias – Reuters e Associated Press – alertando para a gravidade dos casos de pneumonia viral identificados em Wuhan, na China, foram distribuídos no dia 31 de dezembro de 2019, às 18 horas, horário de Brasíia. “Quase ninguém leu”, lembra o epidemiologista Paulo Lotufo, professor da Faculdade de Medicina da Universidade de São Paulo (FM-USP).', 'Latest news'),
    Noticia(4, 'SC tem queda de casos ativos de Covid, mas vê alta na ocupação de UTIs', 'No período analisado, houve redução de 32% no número de pessoas com a doença em relação à semana anterior', '/static/img/noticia5.jpg', 'A publicação mais recente do Núcleo de Estudo de Economia Catarinense (Necat) trata do cenário da pandemia de coronavírus no Estado entre os dias 12 e 18 de março.No período, houve queda de 32% no número de casos ativos, ou seja, de pessoas diagnosticadas que ainda enfrentavam a doença, em relação à semana anterior. Em números absolutos, o Estado seguia com 6.311 pessoas infectadas pelo coronavírus na semana analisada, mas, na anterior, havia 2.995 pacientes a mais, conforme dados da Secretaria Estadual de Saúde, que baseiam o boletim.', 'Latest news' )
]

class Estado:
    def __init__(self, id, nome, sigla, bandeira):
        self.__id = id
        self.__nome = nome
        self.__sigla = sigla
        self.__bandeira = bandeira

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_sigla(self):
        return self.__sigla

    def get_bandeira(self):
        return self.__bandeira

# Bandeiras dos estados https://mundodageografia.com.br/bandeiras-dos-estados-brasileiros/
lista_estados = [
    Estado(0, 'Acre', 'AC', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Acre-300x210.png'),
    Estado(1, 'Alagoas', 'AL', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Alagoas-300x200.png'),
    Estado(2, 'Amapá', 'AP', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Amapa-300x210.png' ),
    Estado(3, 'Amazonas', 'AM', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Amazonas-300x214.png' ),
    Estado(4, 'Bahia', 'BA', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_da_Bahia-300x200.png'),
    Estado(5, 'Ceará', 'CE', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Ceara-300x210.png'),
    Estado(6, 'Distrito Federal', 'DF', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Distrito_Federal_Brasil-300x210.png'),
    Estado(7, 'Espírito Santo', 'ES', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Espirito_Santo-300x210.png'),
    Estado(8, 'Goiás', 'GO', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Goias-300x210.png'),
    Estado(9, 'Maranhão', 'MA', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Maranhao-300x200.png'),
    Estado(10, 'Mato Grosso', 'MT', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Mato_Grosso-300x210.png'),
    Estado(11, 'Grosso do Sul', 'MS', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Mato_Grosso_do_Sul-300x210.png'),
    Estado(12, 'Minas Gerais', 'MG','https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Minas_Gerais-300x210.png'),
    Estado(13, 'Pará', 'PA', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Para-300x200.png'),
    Estado(14, 'Paraíba', 'PB', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_da_Paraiba-300x210.png'),
    Estado(15, 'Paraná', 'PR', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Parana-300x210.png'),
    Estado(16, 'Pernambuco', 'PE', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Pernambuco-300x210.png'),
    Estado(17, 'Piauí', 'PI', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Piaui-300x200.png'),
    Estado(18, 'Rio de Janeiro', 'RJ', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_Rio_de_Janeiro-300x210.png'),
    Estado(19, 'Rio Grande do Norte', 'RN', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Rio_Grande_do_Norte-300x200.png'),
    Estado(20, 'Rio Grande do Sul', 'RS', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Rio_Grande_do_Sul-300x210.png'),
    Estado(21, 'Rondônia', 'RO', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Rondonia-300x210.png'),
    Estado(22, 'Roraima', 'RR', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Roraima-300x200.png'),
    Estado(23, 'Santa Catarina', 'SC', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Santa_Catarina-300x218.png'),
    Estado(24, 'São Paulo', 'SP', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_Sao_Paulo-300x200.png'),
    Estado(25, 'Sergipe', 'SE', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Sergipe-300x210.png'),
    Estado(26, 'Tocantins', 'TO', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Tocantins-300x210.png')]