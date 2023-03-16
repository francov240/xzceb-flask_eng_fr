'''
File containing both en2fr and fr2en translators
'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY  = os.environ['apikey']
URL     = os.environ['url']
VERSION = '2023-01-13'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version = VERSION,
    authenticator = authenticator)
language_translator.set_service_url(URL)

def english_to_french(english_text):
    '''
    Translates text from english to french
    '''
    if english_text != "":
        translation = language_translator.translate(
            text = english_text,
            model_id = 'en-fr'
        ).get_result()
        return translation["translations"][0]['translation']+'\n'
    return 'The string you entered is empty!\n'

def french_to_english(french_text):
    '''
    Translates text from french to english
    '''
    if french_text != "":
        translation = language_translator.translate(
            text = french_text,
            model_id = 'fr-en'
        ).get_result()
        return translation["translations"][0]['translation']+'\n'
    return 'Le texte que vous avez saisi est vide!\n'
