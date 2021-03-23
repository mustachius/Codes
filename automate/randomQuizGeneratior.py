#! python3
# randomQuizGenerator.py - Cria provas com perguntas e respostas em ordem aleatória,
# juntamente com os gabaritos contendo as respostas.

import random

# Os dados para as provas estão dispostos no formato de dicionários. As chaves são os estados e os valores são as capitais.

capitais = {'Acre':'Rio Branco', 'Alagoas':'Maceio', 'Amapá':'Macapá', 'Amazonas': 'Manaus', 'Bahia':'Salvador', 'Ceará':'Fortaleza', 'Espirito Santo':'Vitória',
            'Goiás':'Goiânia', 'Maranhão':'São Luís', 'Mato Grosso':'Cuiabá', 'Mato Grosso do Sul':'Campo Grande', 'Minas Gerais':'Belo Horizonte', 'Pará':'Belém',
            'Paraíba':'João Pessoa', 'Piauí':'Teresina', 'Rio de Janeiro':'Rio de Janeiro', 'Rio Grande do Sul':'Porto Alegre', 'Rondônia':'Porto Velho', 'Roraima':'Boa Vista'
            'Santa Catarina':'Florianópolis', 'São Paulo':'São Paulo', 'Sergipe':'Aracaju', 'Tocantins':'Palmas', 'Distrito Federal':'Brasília'}

# Gerando 35 arquivos com as provas e os gabaritos das respostas.

for quizNum in range(35):
    # Criando os arquivos com os questionários e com os gabaritos de resposta
    quizFile = open('capitaisquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitaisquiz_respostas%s.txt' % (quizNum + 1), 'w')

    # Escrevendo o cabeçalho da prova
    quizFile.write('Nome:\n\nData:\n\nPeríodo:\n\n')
    quizFile.write(('' * 20) + 'Questionários sobre as capitais brasileiras (Form %s)' %(quizNum + 1))
    quizFile.write('\n\n')

    # Embaralhando a ordem dos estados
    stados = list(capitais.keys())
    random.shuffle(stados)