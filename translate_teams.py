import os
import openai
from dotenv import load_dotenv, find_dotenv
from collections.abc import Iterable

_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def translate_teams(teams: Iterable, from_langs: Iterable, to_langs: Iterable):
    s_teams = ""
    for team, from_lang, to_lang in zip(teams, from_langs, to_langs):
        s_teams += f"{from_lang}, {to_lang}, {team}\n"

    prompt = f"""
    Translate the following football team names: \n
    The input format is: language from which to translate, language to translate to, team name to translate. \n
    Output is just the translated team name. \n
    ```
    {s_teams}
    ```
    """
    response = get_completion(prompt)
    return response


if __name__ == '__main__':
    teams = ["ΠΑΕ Παναθηναϊκός Α.Ο.", "ΠΑΕ ΠΑΟΚ"]
    from_lang = ["Greek", "Greek"]
    to_lang = ["English", "English"]

    transl = translate_teams(teams, from_lang, to_lang)
    print(transl)
