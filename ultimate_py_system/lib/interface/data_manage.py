def create_file(file_name: str):
    """Create a file with the given name

    Args:
        file_name (str): desired file name

    Raises:
        ex: passes on Exception
    """
    # global MANAGED_FILE
    try:
        MANAGED_FILE = open(file_name, 'wt+')
    except Exception as ex:
        raise ex
    finally:
        MANAGED_FILE.close()

def read_file(file_name: str):
    """Read a file that is organized in matrix ; and \\n

    Args:
        file_name (str): name of the file

    Returns:
        _type_: return a matrix of data
    
    Raises:
    ex: passes on Exception
    """
    # global MANAGED_FILE
    try:
        MANAGED_FILE = open(file_name, 'r')
        data = []
        for file_line in MANAGED_FILE:
            person = file_line.split(';')
            data.append(person.copy())
        return data
    except Exception as ex:
        raise ex
    finally:
        MANAGED_FILE.close()

def write_file(file_name: str, data: list):
    """Writes a file with the due data. Data must by separate by ; and by \\n

    Args:
        file_name (str): name of the file
        data (list): desired data to be written

    Raises:
        ex: passes on Exception
    """
    # global MANAGED_FILE
    try:
        MANAGED_FILE = open(file_name, 'w')
        for line in data:
            MANAGED_FILE.write(f'{line[0]};{line[1]};{line[2]}')
    except Exception as ex:
        raise ex
    finally:
        MANAGED_FILE.close()

def write_line(file_name: str, new_line: str):
    """Write a new line on given file

    Args:
        file_name (str): file name
        new_line (str): desired data to be added

    Raises:
        ex: passes on Exception
    """
    try:
        MANAGED_FILE = open(file_name, 'at')
        MANAGED_FILE.write(f'{new_line}\n')
    except Exception as ex:
        raise ex
    finally:
        MANAGED_FILE.close()
