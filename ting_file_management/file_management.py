import sys


def txt_importer(path_file):
    if path_file.endswith('.txt'):
        try:
            with open(path_file, 'r') as file:
                return [line.replace("\n", "") for line in file.readlines()]
        except FileNotFoundError:
            return print(f"Arquivo {path_file} não encontrado",
                         file=sys.stderr)
    else:
        return print("Formato inválido", file=sys.stderr)
