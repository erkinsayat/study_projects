import gtts
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path, language = 'en'):


    with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
        pages = [page.extract_text() for page in pdf.pages]

    text = ''.join(pages)
    text = text.replace('\n', '')

    my_audio = gtts.gTTS(text=text, lang=language)
    my_audio.save('mp3_book/audio.mp3')
