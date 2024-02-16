from lib.interface import visual
from lib.interface import data_input
from lib.utils.colors import ANSI_colors, paint_text

colors = ANSI_colors()

def init_system() -> int:
    """Tries to open db file, if fails create a new one.

    Returns:
        _type_: flag to main options menu
    """
    global DB_FILE
    try:
        DB_FILE = open(DB_NAME, 'r')
        print(paint_text(f'Arquivo {DB_NAME} aberto com sucesso...', 'yellow'))
        return 1
    except FileNotFoundError:
        try:
            DB_FILE = open(DB_NAME, 'wt+')
            print(paint_text(f'Arquivo {DB_NAME} criado com sucesso...', 'yellow'))
            return 1
        except:
            print(paint_text('Algo deu errado ao criar o arquivo', 'red'))
            return 0
    finally:
        DB_FILE.close()
        visual.main_header('Sistema de Cadastro de Pessoas - SisCaP v0.0.1')
        display_options_menu()

def display_options_menu():
    """Display main options menu while system is running
    """
    while True:
        visual.options_menu(AVAILABLE_OPTIONS)
        try:
            option = data_input.read_int('Sua opção: ', 'Opção inválida, tente novamente.')
            if not 0 <= option <= 3:
                raise ValueError()
            next_action = FIND_OPTION_FUNC[option]()
            if not next_action:
                close_system()
                break
            print(visual.line(48), '.')
        except ValueError:
            print(paint_text('Opção inválida, tente novamente.', 'red'))
            continue
        except KeyboardInterrupt:
            print('\n')
            close_system()
            break
    
def get_registered_people():
    global DB_FILE
    visual.header('Pessoas cadastradas'.upper(), color=colors["yellow"])
    try:
        DB_FILE = open(DB_NAME, 'r')
        people =[]
        for db_line in DB_FILE:
            person = db_line.split(';')
            people.append(person.copy())

        print_people(people)

        return 1
    except Exception as error:
        print('Erro ao ler o banco de dados', error)
        return 0
    finally:
        DB_FILE.close()

def print_people(people: list):
    print(f'{"No.":<5}{"Nome":<10}{"Idade":<4}{"Profissão":>28}')
    print(visual.line(48))
    for index, person in enumerate(people):
        print(f'{(index+1):<5}{person[0]:<10}{person[1]:<4}{person[2]:>28}', end='')
        print(visual.line(48, '.'))
    print(visual.line(48))

def register_new_person():
    global DB_FILE
    visual.header('Cadastrar nova pessoa'.upper(), color=colors['yellow'])
    name = data_input.read_str('Digite o nome: ').capitalize()
    age = data_input.read_int('Digite a idade: ')
    profession = data_input.read_str('Digite a profissão: ').lower()
    try:
        DB_FILE = open(DB_NAME, 'at')
        DB_FILE.write(f'{name};{age};{profession}\n')
        print(paint_text(f'{name} cadastrado com sucesso', 'green'))
        return 1
    except:
        print(paint_text('Algo deu errado ao adicionar a nova pessoa.', 'red'))
        return 0
    finally:
        DB_FILE.close()

def close_system():
    visual.header('Sistema encerrado. O SisCaP agradece.', color=colors['yellow'])
    DB_FILE.close()
    return 0


AVAILABLE_OPTIONS = {
        1: 'Ver pessoas cadastradas',
        2: 'Cadastrar nova pessoa',
        3: 'Sair do sistema'
}

FIND_OPTION_FUNC = {
    1: get_registered_people,
    2: register_new_person,
    3: lambda : 0
}

DB_FILE=0
DB_NAME = "db.txt"
