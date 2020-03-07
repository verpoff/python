import wikipedia
wikipedia.set_lang("ru")
while True:
    try:
        search = input("Что ищем?\n")
        if search == 'стоп':
            break
        w = wikipedia.page(search)
        print(w.content)
    except:
        print('Я ничего не нашел')
        print()
        valid_variants = wikipedia.search(search)
        print('Доступные варианты:')
        for variant in valid_variants:
            print(variant)