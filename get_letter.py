import random
def get_letter(length):
    letters = 'ABCDEFGHIKLMNOPQRSTUVWXYabcdefghikmnopqrstuvwxy'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str