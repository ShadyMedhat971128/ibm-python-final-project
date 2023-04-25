"""_summary_
an instance of the IBM Watson Language translator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(f'{url}')
languages = language_translator.list_languages().get_result()

def english_to_french(english_text=""):
    """
    function used to convert english text into french text
    using IBM Watson Language Translator API
    Args:
        english_text (str): english text to be translated

    Returns:
        str: translated french text
    """
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = translation['translations'][0]['translation']
        return french_text
    except Exception as translate_exception:
        print(f"{translate_exception}\n")
        return False

def french_to_english(french_text=""):
    """_summary_
    function used to convert french text into english text
    using IBM Watson Language Translator API
    Args:
        french_text (str): french text to be translated

    Returns:
        str: translated english text
    """
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text = translation['translations'][0]['translation']
        return english_text
    except Exception as translate_exception:
        print(f"{translate_exception}\n")
        return False
