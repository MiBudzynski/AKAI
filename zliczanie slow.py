sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]
#rozdzielanie slow z zdan
for i in range(len(sentences)):
    sentences[i] = sentences[i].split(" ")
words = [] #tablica do zliczania slow
for i in range(len(sentences)):
    for j in range(len(sentences[i])):
        sentences[i][j] = sentences[i][j].lower() #zmiana wielkosci
        #usuwanie , i ? z konca slow
        if sentences[i][j][len(sentences[i][j])-1] == "," or sentences[i][j][len(sentences[i][j])-1] == "?":
            sentences[i][j] = sentences[i][j][:len(sentences[i][j]) - 1]
        # sprawdzenie czy slowo wystapilo, jesli tak +1
        wystopienie = True
        for word in words:
            if word[0] == sentences[i][j]:
                word[1] += 1
                wystopienie = False
        # jesli nie dodaj nowe slowo do listy
        if wystopienie:
            words.append([sentences[i][j], 1])
words.sort(key=lambda x: -x[1]) #sortowanie listy wedle wystapien
#wypisanie
for i in range(3):
    print(f'{i+1}. "{words[i][0]}" - {words[i][1]}')