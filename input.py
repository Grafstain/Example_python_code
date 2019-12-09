delete = [' ', '.', ',', '!', '?', '/']
something = input('Введите текст: ')
for delete in delete:
    if delete in something:
        something = (something.replace(delete, ''))
def reverse(text):
    return text[::-1]
def is_palindrome( text ):
    return text == reverse(text)



#symbols = ['!','@','#','$','%',...]

print(something)

if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")