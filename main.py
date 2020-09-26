import pyttsx3
import PyPDF2

book = open('Rich dad poor dad.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages


engine = pyttsx3.init()

voices = engine.getProperty()
# engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', voices[1].id)

for num in range(16,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
