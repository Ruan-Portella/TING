from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    quoteTxt = txt_importer(path_file)
    dict_file = {'nome_do_arquivo': path_file, 'qtd_linhas': len(quoteTxt),
                 'linhas_do_arquivo': quoteTxt}
    for i in instance.queue:
        if i['nome_do_arquivo'] == path_file:
            return None
    instance.enqueue(dict_file)
    sys.stdout.write(f'{instance.queue}')


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
