from django.shortcuts import render

import re
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def convert(test_keyword):
    split_keyword_list = list(test_keyword)
    #print(split_keyword_list)

    result = list()
    for keyword in split_keyword_list:
        # 한글 여부 check 후 분리
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
            char_code = ord(keyword) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            result.append(CHOSUNG_LIST[char1])
            
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            result.append(JUNGSUNG_LIST[char2])
            
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            if char3==0:
                continue
            else:
                result.append(JONGSUNG_LIST[char3])
                
        else:
            result.append(keyword)
            
    newlist =[]
    
    for i in result:
        if i == 'ㅇ':
            newlist.append('ㅁ')
        else:
            newlist.append(i)
            
    resultword=""
    for word in newlist:
        resultword +=word

    return resultword

            
            



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

     

def result(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary={}

    for word in word_list:
        newword = convert(word)
        if newword in word_dictionary:
            word_dictionary[newword] +=1
        else:
            word_dictionary[newword] = 1
    


    return render(request, 'result.html', {'fulltext':full_text, 'total': len(word_list), 'dictionary':word_dictionary.items()},)


def meow(request):
    return render(request, 'meow.html')

# Create your views here.
