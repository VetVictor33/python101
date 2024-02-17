from lib.interface import visual
from lib.interface import data_input
from lib.interface import data_manage
from lib.utils.colors import ANSI_colors, paint_text

colors = ANSI_colors()

def init_system() -> int:
    """Tries to open db file, if fails create a new one.

    Returns:
        _type_: flag to main options menu
    """
    try:
        data_manage.read_file(DB_NAME)
        print(paint_text(f'Arquivo {DB_NAME} aberto com sucesso...', 'yellow'))
        return 1
    except:
        try:
            data_manage.create_file(DB_NAME)
            print(paint_text(f'Arquivo {DB_NAME} criado com sucesso...', 'yellow'))
            return 1
        except:
            print(paint_text('Algo deu errado ao criar o arquivo', 'red'))
            return 0
    finally:
        visual.main_header('Sistema de Cadastro de Pessoas - SisCaP v0.0.1')
        display_options_menu()

def display_options_menu():
    """Display main options menu while system is running
    """
    while True:
        visual.options_menu(AVAILABLE_OPTIONS)
        try:
            option = data_input.read_int('Sua opção: ', error_message='Opção inválida, tente novamente.')
            if not 0 < option <= len(AVAILABLE_OPTIONS.keys()):
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
    visual.header('Pessoas cadastradas'.upper(), color=colors["yellow"])
    try:
        people = data_manage.read_file(DB_NAME)
        visual.print_people(people)
        return 1
    except Exception as error:
        print('Erro ao ler o banco de dados', error)
        return 0

def register_new_person():
    visual.header('Cadastrar nova pessoa'.upper(), color=colors['yellow'])
    name = data_input.read_str('Digite o nome: ').capitalize()
    age = data_input.read_int('Digite a idade: ')
    profession = data_input.read_str('Digite a profissão: ').lower()
    try:
        data_manage.write_line(DB_NAME, f'{name};{age};{profession}')
        print(paint_text(f'{name} cadastrado com sucesso', 'green'))
        return 1
    except Exception as ex:
        print(paint_text(f'Algo deu errado ao adicionar a nova pessoa. {ex}', 'red'))
        return 0

def remove_person():
    visual.header('Remover pessoa'.upper(), color=colors['yellow'])
    try:
        people = data_manage.read_file(DB_NAME)
        option = data_input.read_int('Qual o número da pessoa que você deseja deletar? ', range=(1, len(people)))
        deleted_person = people[option - 1]
        del people[option - 1]
        
        data_manage.write_file(DB_NAME, people)
        print(paint_text(f'{deleted_person[0]} {paint_text("eliminado(a) com sucesso", "red")}', 'yellow'))
        return 1
    except Exception as ex:
        print(paint_text(f'Algo deu errado ao remover a nova pessoa. {ex}', 'red'))
        return 1

def close_system():
    visual.header('Sistema encerrado. O SisCaP agradece.', color=colors['yellow'])
    return 0


AVAILABLE_OPTIONS = {
        1: 'Ver pessoas cadastradas',
        2: 'Cadastrar nova pessoa',
        3: 'Remover pessoa',
        4: 'Sair do sistema'
}

FIND_OPTION_FUNC = {
    1: get_registered_people,
    2: register_new_person,
    3: remove_person,
    4: lambda : 0
}

DB_NAME = "db.txt"