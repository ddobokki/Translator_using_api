# Translator_using_api
api를 사용한 번역기 입니다.
      
      from Translator import PapagoTranslator, KaKaoTranslator
      
      client_id = ""
      client_secret = "" # 발급 주소: https://developers.naver.com/main/
      
      rest_api_key = "" # 발급 주소: https://developers.kakao.com/
      
      ppg = PapagoTranslator(client_id, client_secret)
      kko = KaKaoTranslator(rest_api_key=rest_api_key)
      
      ppg.get_surport_lang_list()
      # kko.get_surport_lang_list() == ppg.get_surport_lang_list()
      -> {'ko': '한국어', 
          'en': '영어', 
          'ja': '일본어', 
          'zh-CN': '중국어 번체', 
          'zh-TW': '중국어 간체', 
          'id': '인도네시아어', 
          'th': '태국어', 
          'de': '독일어', 
          'ru': '러시아어', 
          'es': '스페인어', 
          'it': '이탈리아어', 
          'fr': '프랑스어'}


- translate: text를 source 언어에서 target 언어로 번역합니다.
- 
      ppg.translate("안녕하세요.", "ko", "en")
      -> Hello

      kko.translate("안녕하세요.", "ko", "en")
      -> Hi!
      
- translate_texts: 리스트에 있는 text를 source 언어에서 target 언어로 번역합니다.

      ppg.translate_texts(["안녕하세요.", "번역기", "테스트입니다."], "ko", "ja")
      -> ['おはようございます', '翻訳機', 'テストです。']

      kko.translate_texts(["안녕하세요.", "번역기", "테스트입니다."], "ko", "ja")
      -> ['こんにちは', '翻訳機', 'テストです']

- back_translate: text를 source -> target -> source로 번역합니다.
    
    
      ppg.back_translate("Welcome to the summoner's rift", "en", "ko")
      -> Welcome to the crack of the summoner.

      kko.back_translate("Welcome to the summoner's rift", "en", "ko")
      -> Welcome to the breach of the summoner
    

- back_translate_texts: 리스트에 있는 text를 source -> target -> source로 번역합니다.


      texts = ["죽는 날까지 하늘을 우러러"
               "한 점 부끄럼이 없기를",
               "잎새에 이는 바람에도",
               "나는 괴로워했다.",
               "별을 노래하는 마음으로",
               "모든 죽어 가는 것을 사랑해야지",
               "그리고 나한테 주어진 길을",
               "걸어가야겠다.",
               "오늘 밤에도 별이 바람에 스치운다."]
    
      ppg.back_translate_texts(texts=texts, source="ko", target="en")
      -> ['죽는 날까지 하늘을 부끄러워하지 않았으면 좋겠어요.',
          '나뭇잎에 바람이 불어도',
          '나는 괴로웠다.',
          '별을 노래하는 마음으로.',
          '죽어가는 모든 것을 사랑해야 합니다.',
          '그리고 내게 주어진 길은...',
          '걸어가야겠어요.',
          '오늘 밤에도 별들은 바람을 타고 지나간다.']

      kko.back_translate_texts(texts=texts, source="ko", target="en")
      -> ['죽는 날까지 하늘을 부끄러워하지 않기를 바란다.', 
          '떠나는 바람에', '나는 고통스러웠다.', 
          '별을 부르는 마음으로', 
          '죽어가는 모든 사람들을 사랑해야 한다', 
          '그리고 저는 그 길을 따라가야 할 것입니다', 
          '걸어야해요.', 
          '오늘 밤, 별들이 바람을 닦는다.']

