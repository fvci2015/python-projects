import demoji

class EmojiConverter:
    def __init__(self):
        # Ensure demoji codes are downloaded
        demoji.download_codes()

    def emoji_to_text_converter(self, input_text):
        # Use demoji to replace emojis with their descriptions
        return demoji.findall(input_text)

if __name__ == "__main__":
    converter = EmojiConverter()
    text = "Then, we added more interesting complex relationships. 🔜 implied that, after time, one thing would lead to another. 🤓🔜🗣️ means that “I’ll be able to talk soon.” We created a scale for asking “How do you feel?”: 😄😀🙂😕☹️😴❓"
    emoji_to_text = converter.emoji_to_text_converter(text)
    print(emoji_to_text)
