import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords

def remove_punctuation(text):
    punctuation_pattern = r'[^\w\s]'
    text_without_punctuation = re.sub(punctuation_pattern, '', text)
    return text_without_punctuation

def summarize(text,size,style):
    newText=remove_punctuation(text)
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(newText)
    k=0
    if(size=="Small"):
        k=1.9
    if(size=="Medium"):
        k=1.78
    if(size=="Large"):
        k=1.62
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    average = int(sumValues / len(sentenceValue))

    summary = ""
    ct=0
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (k * average)):
            sentence = ' '.join(re.sub(r'\s+', ' ', sentence).splitlines())
            
            if(style=="BullPt"):
                summary += " \n "
                summary += "\u2022 " + sentence + "\n"
            else:

                ct+=1
                summary+=" "+sentence
                if(ct==5):
                    summary+=" \n "
                    summary+="\n"
                    ct=0
    return summary

