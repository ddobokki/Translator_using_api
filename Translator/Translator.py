import os
import sys
from typing import List
import urllib.request
import requests
import json
from base_translator import Translator


class PapagoTranslator(Translator):

    def __init__(self, client_id: str, client_secret: str):
        '''
        client_id: 발급받은 Client ID 값
        client_secret: 발급받은 Client Secret 값
        발급 주소: https://developers.naver.com/main/

        '''
        super().__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.url = "https://openapi.naver.com/v1/papago/n2mt"

    def translate(self, text: str, source: str, target: str) -> str:
        assert source in self.surport_lang_list
        assert target in self.surport_lang_list
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


class KaKaoTranslator(Translator):
    def __init__(self, rest_api_key):
        '''
        rest_api_key: 발급 받은 REST API KEY
        발급 주소: https://developers.kakao.com/
        '''
        super().__init__()
        self.url = "https://dapi.kakao.com/v2/translation/translate"
        self.rest_api_key = rest_api_key

    def translate(self, text: str, source: str, target: str) -> str:
        assert source in self.surport_lang_list
        assert target in self.surport_lang_list
        assert source != target

        source, target = self._convert_lang_code(source, target)

        params = {'query': text, 'src_lang': source, 'target_lang': target}
        header = {'authorization': f'KakaoAK {self.rest_api_key}'}
        response = requests.get(url=self.url, headers=header, params=params)

        if response.status_code == 200:
            decode = response.json()
            translated_text = decode['translated_text'][0][0]
        else:
            print("Error Code:" + response.status_code)
        return translated_text

    def _convert_lang_code(self, source, target):
        if source == 'ko':
            source = 'kr'
        elif source == 'ja':
            source = 'jp'
        elif source == 'zh-TW' or source == 'zh-CN':
            source = 'cn'

        if target == 'ko':
            target = 'kr'
        elif target == 'ja':
            target = 'jp'
        elif target == 'zh-TW' or target == 'zh-CN':
            target = 'cn'

        return source, target


if __name__ == '__main__':
    '''
    발급 주소: https://developers.naver.com/main/
    개발자센터에서 발급받은 Client ID 값
    개발자센터에서 발급받은 Client Secret 값
    '''

    client_id = ''
    client_secret = ''

    ppg = PapagoTranslator(client_id, client_secret)
    print(ppg.translate('안녕하세요', 'ko', 'en'))
    print(ppg.translate_texts(['안녕하세요.', '번역기', '테스트입니다.'], 'ko', 'ja'))
    print(ppg.back_translate(
        'Billie Jean is not my lover', 'en', 'zh-CN'))
    print(ppg.back_translate_texts(
        ['노인을 위한 나라는 없다.', '어벤져스:가망 없음 ', '스파이더맨: 노 웨이 홈'], 'ko', 'de'))

    '''
    rest_api_key: 발급 받은 REST API KEY
    발급 주소: https://developers.kakao.com/
    '''

    rest_api_key = ''
    kko = KaKaoTranslator(rest_api_key)
    print(kko.translate('안녕하세요', 'ko', 'en'))
    print(kko.translate_texts(['안녕하세요.', '번역기', '테스트입니다.'], 'ko', 'ja'))
    print(kko.back_translate(
        'Billie Jean is not my lover', 'en', 'zh-CN'))
    print(kko.back_translate_texts(
        ['노인을 위한 나라는 없다.', '어벤져스:가망 없음 ', '스파이더맨: 노 웨이 홈'], 'ko', 'de'))
