from typing import List


class Translator:
    """
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
    """

    def __init__(self):
        self.__surport_lang_list = [
            "ko",
            "en",
            "ja",
            "zh-CN",
            "zh-TW",
            "id",
            "th",
            "de",
            "ru",
            "es",
            "it",
            "fr",
        ]
        self.__surport_lang_dict = {
            "ko": "한국어",
            "en": "영어",
            "ja": "일본어",
            "zh-CN": "중국어 번체",
            "zh-TW": "중국어 간체",
            "id": "인도네시아어",
            "th": "태국어",
            "de": "독일어",
            "ru": "러시아어",
            "es": "스페인어",
            "it": "이탈리아어",
            "fr": "프랑스어",
        }

    def translate(self, text: str, source: str, target: str) -> str:
        """
        Arguments:
        text : source text
        source : source language
        target : target language

        return translated text
        """
        assert source in self.__surport_lang_list
        assert target in self.__surport_lang_list
        assert source != target

        pass

    def translate_texts(self, texts: List[str], source: str, target: str) -> List[str]:
        """
        Arguments:
        texts : list of the source texts
        source : source language
        target : target language

        return list of the translated texts
        """
        translated_texts = list(
            map(lambda text: self.translate(text, source, target), texts)
        )
        return translated_texts

    def back_translate(self, text: str, source: str, target: str) -> str:
        """
        Arguments:
        text : source text
        source : source language
        target : target language
        return source language text translated from the target language.
        """
        translated_text = self.translate(text, source, target)
        back_translated_text = self.translate(translated_text, target, source)
        return back_translated_text

    def back_translate_texts(
        self, texts: List[str], source: str, target: str
    ) -> List[str]:
        """
        Arguments:
        texts : list of the source texts
        source : source language
        target : target language

        return list of the source language texts translated from the target language.
        """
        back_translated_texts = list(
            map(lambda text: self.back_translate(text, source, target), texts)
        )
        return back_translated_texts

    def get_surport_lang(self):
        return self.__surport_lang_dict.copy()
