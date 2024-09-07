import string
def is_palindrome(text):
    for i in text:
        if i in string.punctuation:
            text = text.replace(i, '').lower()
            text = text.replace(' ', '')

    palindrome_text = ''.join(reversed(text))
    # print(line)

    if palindrome_text == text:
        return True
    else:
        return False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

