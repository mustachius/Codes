#! python3
# randomQuizGenerator.py - Cria provas com perguntas e respostas em ordem aleatória,
# juntamente com os gabaritos contendo as respostas.

import random

# Os dados para as provas estão dispostos no formato de dicionários. As chaves são os estados e os valores são as capitais.

capitais = {'Acre':'Rio Branco', 'Alagoas':'Maceio', 'Amapá':'Macapá', 'Amazonas': 'Manaus', 'Bahia':'Salvador', 'Ceará':'Fortaleza', 'Espirito Santo':'Vitória',
            'Goiás':'Goiânia', 'Maranhão':'São Luís', 'Mato Grosso':'Cuiabá', 'Mato Grosso do Sul':'Campo Grande', 'Minas Gerais':'Belo Horizonte', 'Pará':'Belém',
            'Paraíba':'João Pessoa', 'Piauí':'Teresina', 'Rio de Janeiro':'Rio de Janeiro', 'Rio Grande do Sul':'Porto Alegre', 'Rondônia':'Porto Velho', 'Roraima':'Boa Vista'
            'Santa Catarina':'Florianópolis', 'São Paulo':'São Paulo', 'Sergipe':'Aracaju', 'Tocantins':'Palmas', 'Distrito Federal':'Brasília'}