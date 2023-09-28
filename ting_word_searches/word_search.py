def exists_word(word, instance):
    items_with_word = []
    for item in instance.queue:
        lines_with_word = [i+1 for i, quote in enumerate(
            item["linhas_do_arquivo"]) if word.lower() in quote.lower()]
        if len(lines_with_word) > 0:
            item_with_word = {
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": [{"linha": line} for line in lines_with_word]
            }
            items_with_word.append(item_with_word)
    return items_with_word


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
