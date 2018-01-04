import signal
import sys

from datetime import datetime

from crawler.terminal import *
from crawler.json import *

def main():
    year = int(sys.argv[1]) if len(sys.argv) == 3 else datetime.today().year
    month = int(sys.argv[2]) if len(sys.argv) == 3 else datetime.today().month

    print('\n\tChecklist de {:02d}/{}\n'.format(month, year))

    file_path = './docs/checklists/br/{}-{:02d}.json'.format(year, month)
    data = load_json_from_file(file_path)
    option = ''

    options = {
        '1' : 'Adicionar novo item a lista manualmente.',
        '2' : 'Editar item da lista.',
        '3' : 'Remover item da lista.',
        'Q' : 'Salvar alterações e sair.'
    }

    while option.upper() != 'Q':
        show_data(data)

        print_options(options)

        option = input('\n\tOpção: ')
    
        if option == '1':
            item = prompt_new_item_manual()
            data.append(item)
            print('\nItem adicionado a lista.\n')
        elif option == '2':
            index = prompt_item_to_update()
            item = prompt_update_item(data[index])
            data[index] = item
            print('\nItem editado na lista.')
        elif option == '3':
            index = prompt_item_to_remove()
            data.pop(index)
            print('\nItem removido da lista.\n')
            
        save_json_to_file(file_path, data)

def signal_handler(signal, frame):
    print('\nCtrl-C pressionado, encerrando.')
    exit(1)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    main()
