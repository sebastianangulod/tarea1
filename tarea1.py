meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(f"Significado de {word}: {meme_dict[word]}")
else:
    print(f"Lo siento, no tengo información sobre la palabra '{word}'.")
