#Copy and Paste with Pyperclip
import pyperclip

AFFILIATE_CODE = '&tag=pyb0f-20'

url = pyperclip.paste()

if 'amazon' not in url:
    print('Sorry, invalid link.')
else:
    new_link = url + AFFILIATE_CODE
    pyperclip.copy(new_link)
    print('Affiliate Link generated and copied to clipboard')


#text replacer
def paste_from_clipboard():
    text = pyperclip.paste()
    return text


def copy_to_clipboard(new_text):
    pyperclip.copy(new_text)
    print("The new string is now copied to the clipboard. Hit CTRL V to paste.")


def replace_text(old_text):
    target = input('What would you like to replace? ')
    replacement = input('And what would you like to replace it with? ')
    new_text = old_text.replace(target, replacement)
    return new_text


if __name__ == "__main__":
    old_text = paste_from_clipboard()
    new_text = replace_text(old_text)
    copy_to_clipboard(new_text)
    input()