import os
import json
import csv

DEF_IDIOMA = 'pt'

headers = ['name','set', 'collector_number', 'foil', 'lang', 'number']
nome_input = 'data.json'
nome_output = 'data.csv'

json_file = open(nome_input,'r', encoding='utf-8')
entrada = json.load(json_file)

if not os.path.exists(nome_output):
    with open(nome_output,'w', newline='', encoding='utf-8') as csv_file:
        saida = csv.writer(csv_file)
        saida.writerow(headers)

def collector_search(set,collector_number):
    card = [x for x in entrada if x['set']==set and x['collector_number']==collector_number]
    if len(card)!=0:
        return card[0].get('name')
    return None

def name_search(name, strict):
    card = []
    card = [x for x in entrada if x['name'].lower()==name]
    if len(card) == 0 and not strict:
        card = [x for x in entrada if 'printed_name' in x and name.lower() in x['printed_name'].lower()]
    if len(card) == 0:
        print("Nenhuma carta encontrada!");
        return
    sorted_cards = sorted(card, key=lambda x: int(x['released_at'][:4]))
    i = 1
    select = 0
    if len(sorted_cards) > 1:
        for card in sorted_cards:
            if card['lang'] != 'en':
                found_name = card['printed_name'] + ', '
            print(f"{i} > {found_name}{card['name']}, {card['set']}, {card['collector_number']} , {card['released_at'][:4], {card['lang']}}")
            i+=1

        print("0 > Nenhuma.")

        select = int(input(f"Qual card deseja adicionar? "))
        if select == 0:
            return
        select -= 1
    elif len(sorted_cards) == 1:
        card = sorted_cards[select]
        found_name = '';
        if card['lang'] != 'en':
            found_name = card['printed_name'] + ', '
        print(f"Card encontrado: {found_name}{card['name']}, {card['set']}, {card['collector_number']} , {card['released_at'][:4], {card['lang']}}")

    entrada_usuario = input("Número de cartas, foil: <number*> <foil*>:")
    foil = ''
    number = 1
    lang = DEF_IDIOMA
    if entrada_usuario != '':
        parts = entrada_usuario.split()
        if parts[-1]=='*' or parts[-1]=='foil':
            foil = 'foil'
            parts = parts[:-1]
        if len(parts)>0:
            if parts[0][0].isdigit():
                number = int(parts[0])
    
    ret = add_or_update(sorted_cards[select]['name'],sorted_cards[select]['set'],sorted_cards[select]['collector_number'],lang,number,foil)
    if ret == number:
        print(f"{name} adicionada, quantidade: {ret}")
    else:
        print(f"{name} atualizada, nova contagem: {ret}")
    
        


def add_or_update(name, set_, collector_number, lang, number, foil):
    found = False
    
    with open(nome_output,'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        rows = list(reader)
        if len(rows) > 0:
            for i, row in enumerate(rows):
                if(row[0] == name and
                   row[1] == set_ and
                   row[2] == collector_number and
                   row[3] == lang and
                   row[5] == foil):
                    rows[i][4] = int(number) + int(rows[i][4])
                    val = rows[i][4]
                    found = True
                    break

    if not found:
        rows.append([name,set_,collector_number, lang, number, foil])

    with open(nome_output, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

    return val if found else number
        
    
    
print('comandos: namesearch <name> : busca por uma carta pelo nome exato digitado, mostrando os resultados em ordem cronologica com set, collector number, e ano de lançamento.')
#print('--------- namedate <year> <name> : busca por uma carta lançada em um ano especifico pelo nome')
print('--------- setlang <lang> : muda o idioma atual que as cartas são adicionadas ex PT/EN/IT/ES/JP')
print('padrão de entrada: <set> <collector_number> <lang*> <number*> <foil*> : lang e number opcionais. adicionar um * ao fim da entrada marca o card como foil')

while True:
    entrada_usuario = input(f"<set> <collector_number> <lang*> ex: {DEF_IDIOMA.upper()} <number*> <*|foil*> : ")
    if entrada_usuario.startswith('namesearch '):
        name = entrada_usuario[len('namesearch '):]
        name_search(name, True)
    elif entrada_usuario.startswith('setlang '):
        nl = entrada_usuario[len('setlang '):]
        DEF_IDIOMA = nl
        print(f"novo idioma padrão: {DEF_IDIOMA.upper()}")
    else:
        parts = entrada_usuario.split()
        if len(parts)<2 or not parts[1][0].isdigit():
            if len(entrada_usuario) < 5:
                print("Para busca parcial por nome é necessário pelo menos 5 Caracteres! Se a carta tiver menos caracteres do que isso no nome, tente usar o comando namesearch.")
                continue
            print("Formato incorreto, testando busca por nome...")
            name_search(entrada_usuario, False)
            continue
        if parts[-1]=='*' or parts[-1]=='foil':
            foil = 'foil'       
            parts = parts[:-1]
        else:
            foil = ''
        set_ = parts[0]
        collector_number = str(int(parts[1]))
        if len(parts) > 2:
            if parts[2][0].isdigit():
                number = int(parts[2])
                if len(parts) >3:
                    lang = parts[3]
                else:
                    lang = DEF_IDIOMA
            else:
                lang = parts[2]
                if len(parts) >3:
                    number = int(parts[3])
                else:
                    number = 1
        else:
            number = 1
            lang = DEF_IDIOMA
        name = collector_search(set_,collector_number)
        
        if name==None:
            print("Card não encontrado, tente novamente!")
            continue
        
        if foil!='':
            comma = ','
        else:
            comma = ''

        ret = add_or_update(name, set_, collector_number, lang, number, foil)
        if ret == number:
            print(f"{name} adicionada, quantidade: {ret}")
        else:
            print(f"{name} atualizada, nova contagem: {ret}")
            
        
        
