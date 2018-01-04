import operator

from tabulate import tabulate
from datetime import datetime

from crawler.constants import AVAILABLE_PUBLISHERS

def print_options(options):
    print('\n\tOpções:')
    for key, value in options.items():
        print('\t{}) {}'.format(key, value))

def print_options_list(options):
    print('\n\tOpções:')
    for index, value in enumerate(options, start=1):
        print('\t{}) {}'.format(index, value))

def prompt_new_item_manual():
    item = {}

    print('\nEditoras:\n')
    print_options_list([v['name'] for k, v in AVAILABLE_PUBLISHERS['br'].items()])

    code = int(input('\n\tEditora: '))
    item['publisher'] = {}
    item['publisher']['code'] = code
    item['publisher']['name'] = AVAILABLE_PUBLISHERS['br'][code]['name']

    available_labels = AVAILABLE_PUBLISHERS['br'][code]['publishing_labels']

    if len(available_labels) == 1:
        item['publisher']['label'] = available_labels[0]
        print('\nSelo editorial: {}'.format(available_labels[0]))
    else:
        print('\nSelo editorial:\n')
        print_options_list(available_labels)
        code = int(input('\n\tSelo editorial: '))
        item['publisher']['label'] = available_labels[code - 1]

    print('\nInformações:')
    item['name'] = input('\tNome: ')
    item['date'] = input('\tData (dd/mm/yyyy): ')
    item['subtitle'] = input('\tSubtítulo: ')
    item['synopsis'] = input('\tSinopse: ')

    print('\nDados da Edição:')
    i_volume = input('\tVolume: ')
    item['volume'] = -1 if i_volume == '' else int(i_volume)
    item['authors'] = input('\tAutor(es): ')
    item['page_number'] = int(input('\tNúmero de páginas: '))
    item['age_rating'] = input('\tClassificação etária: ')

    print('\nEdição Impressa:')
    item['paper_edition'] = {}
    item['paper_edition']['format'] = input('\tFormato: ')
    item['paper_edition']['price'] = float(input('\tPreço: ').replace(',', '.'))
    item['paper_edition']['isbn'] = input('\tISBN: ').replace('-', '')

    digital = input('\nEdição Digital (S / N): ')
    if digital.upper() == 'S':
        item['digital_edition'] = {}
        item['digital_edition']['format'] = input('\tFormato: ')
        item['digital_edition']['price'] = float(input('\tPreço: ').replace(',', '.'))
        item['digital_edition']['available_at'] = input('\tDisponível nas lojas: ')
        item['digital_edition']['isbn_epub'] = input('\tISBN [.epub]: ').replace('-', '')
        item['digital_edition']['isbn_mobi'] = input('\tISBN [.mobi]: ').replace('-', '')
    
    print('\nImagens:')
    item['cover_url'] = input('\tCapa: ')
    i_header_url = input('\tCabeçalho: ')
    item['header_url'] = item['cover_url'] if i_header_url == '' else i_header_url
    item['url'] = input('\tUrl: ')

    return item

def prompt_update(prompt, original_value, ellipsize=False, show_value=True):
    i_input = input('\t{}{}: '.format(prompt, ' ({})'.format('...' if ellipsize else original_value) if show_value else ''))
    return '' if i_input == '*' else original_value if i_input == '' else i_input

def prompt_update_item(item):
    print('\n\tEditando {}.\n\tTecle Enter caso queira manter o mesmo valor,\n\tou digite * para limpar o valor.'.format(item['name']))

    print('''
    Editora:
        Nome: {}
        Selo editorial: {}
    '''.format(item['publisher']['name'], item['publisher']['label']))

    print('\nInformações:')
    item['name'] = prompt_update('Nome', item['name'])
    item['date'] = prompt_update('Data (dd/mm/yyyy)', item['date'])
    item['subtitle'] = prompt_update('Subtítulo', item['subtitle'])
    item['synopsis'] = prompt_update('Sinopse', item['synopsis'], ellipsize=True)

    print('\nDados da Edição:')
    item['volume'] = int(prompt_update('Volume', item['volume']))
    item['authors'] = prompt_update('Autor(es)', item['authors'])
    item['page_number'] = int(prompt_update('Número de páginas', item['page_number']))
    item['age_rating'] = prompt_update('Classificação etária', item['age_rating'])

    print('\nEdição Impressa:')
    item['paper_edition']['format'] = prompt_update('Formato', item['paper_edition']['format'])
    v_price = prompt_update('Preço', item['paper_edition']['price'])
    item['paper_edition']['price'] = v_price if type(v_price) is float else float(v_price.replace(',', '.'))
    item['paper_edition']['isbn'] = prompt_update('ISBN', item['paper_edition']['isbn']).replace('-', '')

    digital_exists = 'digital_edition' in item
    digital = 'S' if digital_exists else input('\nEdição Digital (S / N): ')
    if digital.upper() == 'S':
        if digital_exists:
            print('\nEdição Digital:')
        item['digital_edition'] = item['digital_edition'] if digital_exists else {}
        item['digital_edition']['format'] = prompt_update(
            'Formato', item['digital_edition']['format'] if digital_exists else '', show_value=digital_exists
        )
        v_price = prompt_update(
            'Preço', item['digital_edition']['price'] if digital_exists else '', show_value=digital_exists
        )
        item['digital_edition']['price'] = v_price if type(v_price) is float else float(v_price.replace(',', '.'))
        item['digital_edition']['available_at'] = prompt_update(
            'Disponível nas lojas', item['digital_edition']['available_at'] if digital_exists else '', show_value=digital_exists
        )
        item['digital_edition']['isbn_epub'] = prompt_update(
            'ISBN [.epub]', item['digital_edition']['isbn_epub'] if digital_exists else '', show_value=digital_exists
        ).replace('-', '')
        item['digital_edition']['isbn_mobi'] = prompt_update(
            'ISBN [.mobi]', item['digital_edition']['isbn_mobi'] if digital_exists else '', show_value=digital_exists
        ).replace('-', '')
    
    print('\nImagens:')
    item['cover_url'] = prompt_update('Capa', item['cover_url'], ellipsize=True)
    v_header = prompt_update('Cabeçalho', item['header_url'], ellipsize=True)
    item['header_url'] = item['cover_url'] if v_header == '' else v_header
    item['url'] = prompt_update('URL', item['url'], ellipsize=True)

    return item

def prompt_item_to_remove():
    return int(input('\tÍndice para remover: '))

def prompt_item_to_update():
    return int(input('\tÍndice para editar: '))

def show_data(data):
    if not data:
        print('\tLista vazia.')
        return

    data.sort(key=lambda x: (x['date'] == '', '' if x['date'] == '' else datetime.strptime(x['date'], '%d/%m/%Y')))

    data_list = [[i['publisher']['name'], i['publisher']['label'], i['name'], i['volume'], i['date']] for i in data]
    headers = ['Editora', 'Selo', 'Nome', 'Volume', 'Data']
    print(tabulate(
        tabular_data=data_list, headers=headers, tablefmt='rst', showindex='always'
    ))
