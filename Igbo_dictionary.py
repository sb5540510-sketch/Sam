IGBO_DICT = {
    'money': 'ego',
    'road': 'uzo',
    'joy': 'onu',
    'food': 'nri',
    'vehicle': 'ugboala',
    'water': 'mmiri',
    'friend': 'enyi',
    'market': 'ahia',
    'school': 'ulo akwukwo',
    'mother': 'nne',
    'boy': 'nwa',
    'book': 'akwukwo',
    'shoe': 'akpukpo',
    'house': 'ulo',
    'hospital': 'ulo ogwu',
    'trouser': 'uwe ogologo okpa',
    'good morning': 'ututu oma',
    'good afternoon': 'ehihie oma',
    'mouth': 'onu'
}

def translate_to_igbo(word: str):
    word = word.lower().strip()
    return IGBO_DICT.get(word, None)
