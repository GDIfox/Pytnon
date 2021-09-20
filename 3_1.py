trans = {
    'zero':'ноль',
    'one':'один',
    'two':'два',
    'three':'три',
    'four':'четыре',
    'five':'пять',
    'six':'шесть',
    'seven':'семь',
    'eight':'восемь',
    'nine':'девять',
    'ten':'десять'
}
w = input('Напишите число (от 0 до 10) прописью на "Eng": ')


def num_translatelist(word):
    return trans.get(word)


print(num_translatelist(w))