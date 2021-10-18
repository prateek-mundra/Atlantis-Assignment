import json
import urllib.request

word = str(input("Word? "))
print("Word: " + word)

url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'+word
# url = 'https://dictionaryapi.dev/'

with (urllib.request.urlopen(url)) as u:
    s = u.read()
    # print("type of s",type(s))
    # print("Output: " ,s)
    s = s.decode("utf-8") 
    s = eval(s)
    # print( s[0]['meanings'][0]['partOfSpeech'].title())
    # print(s[0]['meanings'][0]['definitions'][0]['definition'].title())
    p = word.title()+". " + s[0]['meanings'][0]['partOfSpeech'].title()+". "+s[0]['meanings'][0]['definitions'][0]['definition'].title()
    # print("s===",s[0]['meanings']['definitions'])
    print(p)
    # for i in s[0]['meanings'][0]['']['definitions']:
    #     print(i)