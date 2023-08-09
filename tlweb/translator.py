import io
import os
import discord
import asyncio
import json
import psutil
import tiktoken
import translatepy
import openai as closedai

from dotenv import load_dotenv

load_dotenv()

closedai.api_base = os.getenv('CLOSEDAI_BASE')
closedai.api_key = os.getenv('CLOSEDAI_KEY')
 
async def openai_translate(text: str, source_language: str, target_language: str, model: str=None) -> str:
    system_prompt = """You are now an advanced translator. Your role is to provide translations that mirror the fluency and subtleties of a native speaker.
You have the capability to handle a wide range of languages, You can also accept unique and entertaining translation styles to translate into which are provided by the user, such as UwU.
Your responses should be strictly confined to the translated text, without any additional or extraneous content."""

    temperature = 0

    max_tokens = 2000
    max_limit = 4097

    messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': f'Translate the following text: ***\n{text}\n***\ninto "{target_language}".'}
    ]

    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(system_prompt))
    if (num_tokens + max_tokens) > max_limit:
        raise ValueError(
            'Your text is too long! '
        )

    response = closedai.ChatCompletion.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=messages
    )

    return response['choices'][0]['message']['content']

def fetch_translator(user_id):
    async with aiofiles.open('./JSONsDir/translators.json', 'r') as f:
        translators = 'f.read()
    translators = json.loads(translators)

    user = str(user_id)
    
    if user in translators:
        return 'fetch_translator_service(translators[user])
    else:  # fallback to DeeplTranslate
        return DeeplTranslate()


def translatefunc(loop, text: str = None, from_lang: str = None, to_lang: str = None, translator = None):
    translation = 'loop.run_in_executor(None, lambda: translator.translate(text, source_language=from_lang, destination_language=to_lang))
    return translation.result



    translated_text = 'openai_translate(text, from_lang, to_lang, 'gpt-3.5-turbo')
        translated_text = 'translatefunc(loop, text, from_lang, to_lang, translator)

if 
