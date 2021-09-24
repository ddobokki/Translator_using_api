# Translator_using_api
api를 사용한 번역기 입니다.
- translate: text를 source 언어에서 target 언어로 번역합니다.
    
      ppg = PapagoTranslator(client_id, client_secret)
    
      ppg.translate('안녕하세요', 'ko', 'en')

      -> Hello
- translate_texts: 리스트에 있는 text를 source 언어에서 target 언어로 번역합니다.

      ppg.translate_texts(['안녕하세요.', '번역기', '테스트입니다.'], 'ko', 'ja')

      -> ['おはようございます', '翻訳機', 'テストです。']
- back_translate: text를 source -> target -> source로 번역합니다.
    
    
      ppg.back_translate('Billie Jean is not my lover', 'en', 'zh-CN')
     
      -> Billie Jean is not my lover.
    

- back_translate_texts: 리스트에 있는 text를 source -> target -> source로 번역합니다.
    
    
      ppg.back_translate_texts(['노인을 위한 나라는 없다.', '어벤져스:가망 없음 ', '스파이더맨: 노 웨이 홈'], 'ko', 'de')
    
      -> ['노인을 위한 나라는 없습니다.', '어벤져스: 말도 안돼.', '스파이더맨: 노웨이 홈']

