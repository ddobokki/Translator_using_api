import os
import sys
from typing import List
import urllib.request
import json


class PapagoTranslator():
    '''
    지원 언어

    한국어(ko)
    영어(en)
    일본어(ja)
    중국어 간체(zh-CN)
    중국어 번체(zh-TW)
    베트남어(vi)
    인도네시아어(id)
    태국어(th)
    독일어(de)
    러시아어(ru)
    스페인어(es)
    이탈리아어(it)
    프랑스어(fr)
    '''

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.url = "https://openapi.naver.com/v1/papago/n2mt"

    def translate(self, text: str, source: str, target: str) -> str:
        '''
        Arguments:
        text : source text
        source : source language, surport: ko, en, ja
        target : target language, surport: ko, en, ja

        return translated text
        '''
        surport_lang_list = ['ko', 'en', 'ja', 'zh-CN',
                             'zh-TW', 'id', 'th', 'de', 'ru', 'es', 'it', 'fr']
        assert source in surport_lang_list
        assert target in surport_lang_list
        assert source != target

        encText = urllib.parse.quote(text)
        data = f'source={source}&target={target}&text=' + encText
        request = urllib.request.Request(self.url)
        request.add_header("X-Naver-Client-Id", self.client_id)
        request.add_header("X-Naver-Client-Secret", self.client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()

        if(rescode == 200):
            response_body = response.read()
            decode = json.loads(response_body.decode('utf-8'))
            # print(decode)
            translated_text = decode['message']['result']['translatedText']
        else:
            print("Error Code:" + rescode)

        return translated_text

    def translate_texts(self, texts: List[str], source: str, target: str) -> List[str]:
        '''
        Arguments:
        texts : list of the source texts
        source : source language
        target : target language

        return list of the translated texts
        '''
        translated_texts = list(
            map(lambda text: self.translate(text, source, target), texts))
        return translated_texts

    def back_translate(self, text: str, source: str, target: str) -> str:
        '''
        Arguments:
        text : source text
        source : source language
        target : target language

        return source language text translated from the target language.
        '''
        translated_text = self.translate(text, source, target)
        back_translated_text = self.translate(translated_text, target, source)
        return back_translated_text

    def back_translate_texts(self, texts: List[str], source: str, target: str) -> List[str]:
        '''
        Arguments:
        texts : list of the source texts
        source : source language
        target : target language

        return list of the source language texts translated from the target language.
        '''

        back_translated_texts = list(
            map(lambda text: self.back_translate(text, source, target), texts))
        return back_translated_texts


if __name__ == '__main__':

    # 발급 주소: https://developers.naver.com/main/
    client_id = "id"  # 개발자센터에서 발급받은 Client ID 값
    client_secret = "secret"  # 개발자센터에서 발급받은 Client Secret 값

    ppg = PapagoTranslator(client_id, client_secret)
    print(ppg.translate('안녕하세요', 'ko', 'en'))
    print(ppg.translate_texts(['안녕하세요.', '번역기', '테스트입니다.'], 'ko', 'ja'))
    print(ppg.back_translate(
        'Billie Jean is not my lover', 'en', 'zh-CN'))
    print(ppg.back_translate_texts(
        ['노인을 위한 나라는 없다.', '어벤져스:가망 없음 ', '스파이더맨: 노 웨이 홈'], 'ko', 'de'))
