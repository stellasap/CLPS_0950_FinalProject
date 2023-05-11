import random
def get_letter(length):
    letters = 'ABCDEFGHIKLMNOPQRSTUVWXY' # removed lowercase since Stella's only has upper case
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str