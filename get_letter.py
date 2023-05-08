import random
def get_letter(length):
    letters = 'abcdefghiklmnopqrstuvwxy'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str