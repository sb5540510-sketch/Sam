HAUSA_DICT = {
    'money': 'kudi',
    'road': 'hanya',
    'joy': 'farinciki',
    'food': 'abinci',
    'vehicle': 'mota',
    'water': 'ruwa',
    'friend': 'aboki',
    'market': 'kasuwa',
    'school': 'makaranta',
    'mother': 'uwa',
    'boy': 'yaro',
    'book': 'littafi',
    'shoe': 'takalmi',
    'house': 'gida',
    'hospital': 'asibiti',
    'trouser': 'wando',
    'good morning': 'ina kwana',
    'good afternoon': 'ina wuni',
    'mouth': 'baki'
}

def translate_to_hausa(word: str):
    word = word.lower().strip()
    return HAUSA_DICT.get(word, None)
