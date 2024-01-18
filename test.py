from transformers import MarianMTModel, MarianTokenizer

def translate(text, model_name):
    # Load the tokenizer and model
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize the text
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))

    # Decode the translation
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# Model for English to Spanish
model_name = "Helsinki-NLP/opus-mt-en-es"

# Translate text
with open('english_text.txt', 'r') as english_txt_file:
    english_text = english_txt_file.read()

spanish_translation = translate(english_text, model_name)
print(spanish_translation)
with open('spanish_translation.txt', 'w') as spanish_translation_file:
    spanish_translation_file.write(spanish_translation)


