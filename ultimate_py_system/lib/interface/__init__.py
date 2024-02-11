
def line(length=30, character='-') -> str:
    """Return a line with the due length or 30

    Args:
        length (int, optional): Line length. Defaults to 30.
    """
    generated_line = character * length
    return generated_line

def generate_title(title:str, color:str, line_len=48) -> str:
    """Generate system main title

    Args:
        title (str): Desired title
        color (str): ANSI pattern text color
        line_len (int, optional): content length. Defaults to 48.

    Returns:
        str: return styled text to be displayed
    """
    generated_title = f'{color} {title:^{line_len}}\033[m'
    return generated_title

def header(title: str, line_len=48, color='\033[m'):
    """Prints system header

    Args:
        title (str): Desired title
        line_len (int, optional): Content length. Defaults to 48.
        color (str, optional): ANSI pattern text color. Defaults to '\\033[m' (none).
    """
    print(line(line_len))
    print(generate_title(title, color, 44))
    print(line(line_len))

def main_header(title:str, line_len=48, color='\033[1;32m'):
    """Generates system main header

    Args:
        title (str): Desired title
        line_len (int, optional): Content length. Defaults to 48.
        color (str, optional): ANSI pattern text color. Defaults to '\\033[1;32m' (green).
    """
    header(title, line_len, color)

def read_int(message:str, error_message='Valor inválido. Tente novamente'):
    """Reads user input until it's a valid integer

    Args:
        message (str): Message to display to user
        error_message (str, optional): Show when user inout a not integer. Defaults to 'Valor inválido. Tente novamente' red colored.

    Returns:
        _type_: returns an integer inputted by user
    """
    while True:
        try:
            n = int(input(message))
            return n
        except ValueError:
            print(f'\033[31m{error_message}\033[m')
            continue

def read_str(message:str, error_message='Valor inválido. Tente novamente'):
    """Reads user input until it's a valid string, empty string is considered invalid

    Args:
        message (str): Message to display to user
        error_message (str, optional): Show when user fails to input a valid string. Defaults to 'Valor inválido. Tente novamente' red colored.

    Returns:
        _type_: striped string
    """
    while True:
        try:
            n = str(input(message)).strip()
            if not n:
                raise ValueError()
            return n
        except ValueError:
            print(f'\033[31m{error_message}\033[m')
            continue

def init_system() -> int:
    """Tries to open db file, if fails create a new one.

    Returns:
        _type_: flag to main options menu
    """
    global DB_FILE
    try:
        DB_FILE = open(DB_NAME, 'r')
        print(f'Arquivo {DB_NAME} aberto com sucesso...')
        return 1
    except FileNotFoundError:
        try:
            DB_FILE = open(DB_NAME, 'wt+')
            print(f'Arquivo {DB_NAME} criado com sucesso...')
            return 1
        except:
            print('Algo deu errado ao criar o arquivo')
            return 0
    finally:
        DB_FILE.close()

def display_options_menu():
    """Display main options menu while system is running
    """
    while True:
        options_menu()
        try:
            option = read_int('Sua opção: ', 'Opção inválida, tente novamente.')
            if not 0 <= option <= 3:
                raise ValueError()
            next_action = FIND_OPTION_FUNC[option]()
            if not next_action:
                close_system()
                break
            print(line(48), '.')
        except ValueError:
            print('\033[31mOpção inválida, tente novamente.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n')
            close_system()
            break

def options_menu() -> int:
    for option, text in AVAILABLE_OPTIONS.items():
        print(f'\033[32m{option} - \033[34m{text}\033[m')
    print(line(48))
    
def get_registered_people():
    global DB_FILE
    header('Pessoas cadastradas'.upper(), color='\033[33m')
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
    print(line(48))
    for index, person in enumerate(people):
        print(f'{(index+1):<5}{person[0]:<10}{person[1]:<4}{person[2]:>28}', end='')
        print(line(48, '.'))
    print(line(48))

def register_new_person():
    global DB_FILE
    header('Cadastrar nova pessoa'.upper(), color='\033[33m')
    name = read_str('Digite o nome: ').capitalize()
    age = read_int('Digite a idade: ')
    profession = read_str('Digite a profissão: ').lower()
    try:
        DB_FILE = open(DB_NAME, 'at')
        DB_FILE.write(f'{name};{age};{profession}\n')
        print(f'{name} cadastrado com sucesso')
        return 1
    except:
        print('Algo deu errado ao adicionar a nova pessoa.')
        return 0
    finally:
        DB_FILE.close()

def close_system():
    header('Sistema encerrado. O SisCaP agradece.', color='\033[33m')
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
