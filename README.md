Bem, isso aqui começou comigo ficando com raiva da dificuldade que é criar coleções online para quando compro muitas cartas de uma vez.

Aqui você pode adicionar várias cartas em sequência de forma rápida, ainda sim com dados importantes como Idioma, Foil, Quantidades...

Como as alt arts sempre tem um SET e ID diferentes, isso já é adicionado meio que de forma automática.

Ao adicionar cartas em bulk, você vai digitar a sigla do SET e logo em seguida a numeração da carta naquele set, são os números abaixo da carta, no canto esquerdo.

"Ah mas e se a carta não tiver essas informações?" Bem ai problema seu... brincadeira, digite o nome da sua carta, não importa a linguagem. Você vai notar que são apenas 3 arquivos:
DataCAD> o código principal, que lê os dados no Data.Json para encontrar a carta que você está tentando adicionar.
DataCleaner> o código secundário que você utiliza quando lançam cartas novas.

O datacleaner utiliza o arquivo 'all cards' do Scryfall, baixado e renomeado para rawdata.json, para criar o data.json.
https://scryfall.com/docs/api/bulk-data Você pode encontrar esse arquivo aqui.

O datacleaner limpa todo o arquivo de textos inuteis no momento, e deixa apenas os dados necessários para cadastrar as cartas.

"E por que não utilizar logo a api do scryfall?", Por quê criei esse script para cadastrar minhas cartas enquanto estava offline.
Mas em breve vou criar uma nova versão para utilizar a API do scryfall.

É Isso my frendos. Xero do Tio Orckine.
