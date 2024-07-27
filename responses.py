from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered == '':
        return "bol na"
    elif 'hello' in lowered:
        return 'hello there'
    elif 'how are you' in lowered:
        return 'good tu bata'
    elif 'bye' in lowered:
        return 'atey rehna'
    elif 'roll dice' in lowered:
        return f'you rolled: {randint(1, 6)}'
    else:
        return choice(['kya bol rha samjh ni arha',
                       'i donot understand',
                       'hain??'])
