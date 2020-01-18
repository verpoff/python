import wikipedia
wikipedia.set_lang("ru")
search = input("Что ищем?\n")
w = wikipedia.page(search)
print(w.content)