# passphrase-generator
Passphrase generator

[See it live](https://passphrase.taggart-tech.com)

Passwords shouldn't be hard. And in fact, we've done a great job making passwords harder than they need to be.

The answer? Passphrases.

A slightly longer, but easier-to-remember passphrase is actually [more secure](https://xkcd.com/936/) than 8 characters of the usual password gibberish.

So, we're gonna help you out.

This project is based on wordlists curated from [WordsAPI](https://www.wordsapi.com/). 

## Make your own wordlists

Start by signing up for an API Key for WordsAPI. Then, take a look at `getwords.example.py`. Copy it to `getwords.py` in the same folder.

## Set up the environment

Either in a virtual environment or just using your system, install the dependencies:

```bash
pip install -r requirements.txt
```

## Set up `getwords.py`

This script pulls down adjective/noun wordlists for use by `pw.py` to generate passphrases. Changing these values will alter the kinds of words your generator will use. Once you have the settings how you like, run the script.

```bash
python getwords.py
```

You'll find new wordlists in the wordlists folder. Curate them as you see fit (like maybe remove the bad words if you're using this with kids).

## Getting Up and Running
You can run the app locally with:

```bash
python app.py
```
It'll be live at `http://localhost:5000`.

There's also a Dockerfile for alternative deployment.