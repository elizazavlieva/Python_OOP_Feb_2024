def vowel_filter(function):

    def wrapper():
        vowels = ["a", "e", "i", "o", "u"]
        letters = function()
        return [letter for letter in letters if letter.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
