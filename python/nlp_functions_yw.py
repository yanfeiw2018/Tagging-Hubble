{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import nltk\n",
    "import unicodedata\n",
    "from nltk.tokenize import word_tokenize\n",
    "import spacy\n",
    "nlp = spacy.load('en')\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "298"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stop_words = nltk.corpus.stopwords.words('english')\n",
    "f = open('reuters_wos.txt')\n",
    "reu_stop = f.read().split()\n",
    "stop_words.extend(x for x in reu_stop if x not in stop_words)\n",
    "len(stop_words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "399"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "places = []\n",
    "with open('pre2_stop.txt', 'r') as filehandle:  \n",
    "    for line in filehandle:\n",
    "        currentPlace = line[:-1]\n",
    "        places.append(currentPlace)\n",
    "\n",
    "stop_words.extend(x for x in places if x not in stop_words)\n",
    "len(stop_words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def remove_accented_chars(text):\n",
    "    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')\n",
    "    return text\n",
    "\n",
    "def lemmatize_text(text):\n",
    "    text = nlp(text)\n",
    "    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])\n",
    "    return text\n",
    "\n",
    "def remove_stopwords(text):\n",
    "    tokens = word_tokenize(text)\n",
    "    tokens = [token.strip() for token in tokens]\n",
    "    filtered_tokens = [token for token in tokens if token not in stop_words]    \n",
    "    filtered_text = ' '.join(filtered_tokens) # re-create document from filtered tokens\n",
    "    return filtered_text\n",
    "\n",
    "def normalize_corpus(corpus, lemm = True, stopword_removal = True):\n",
    "    normalized_corpus = []\n",
    "    for doc in corpus:\n",
    "        doc = remove_accented_chars(doc)\n",
    "        doc = doc.lower()\n",
    "        doc = re.sub(r'[\\r|\\n|\\r\\n]+', ' ',doc) # remove extra newlines\n",
    "        doc = re.sub(' +', ' ', doc)\n",
    "        doc = doc.strip()\n",
    "        doc = re.sub(r'[^a-zA-Z0-9\\s]', '', doc, re.I|re.A) # remove special characters\n",
    "        if lemm:\n",
    "            doc = lemmatize_text(doc)\n",
    "        if stopword_removal:\n",
    "            doc = remove_stopwords(doc)\n",
    "        normalized_corpus.append(doc)\n",
    "    return normalized_corpus\n",
    "\n",
    "def tokenize_para (para):\n",
    "    sent = sent_tokenizer.tokenize(para) # string to sentences, return a list of sentences;\n",
    "    sent_word = []; # break the sentence into words, return a list of words\n",
    "    for i in range(len(sent)):\n",
    "        sent_word.append(word_tokenize(sent[i])); # a list of lists of words\n",
    "    sent_filt1 = [[word for word in sent if word not in remove_terms] for sent in sent_word]\n",
    "    sent_filt1 = [' '.join(tok_sent) for tok_sent in sent_filt1] # a list of full sentences (each sentence is a string)\n",
    "    norm_sent_filt1 = normalize_corpus(sent_filt1) # return the same as above, but after normalization\n",
    "    norm_00 = [tok_sent for tok_sent in norm_sent_filt1 if len(tok_sent.split()) > 3]\n",
    "    texts = [[text for text in doc.split()] for doc in norm_sent_filt1]\n",
    "    para_styles = {'sent': norm_sent_filt1,\n",
    "                  'word': texts}\n",
    "    return para_styles\n",
    "    ## 'word' is for bigram training\n",
    "    ## 'sent' is for tfidf model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['', '', '', '', 'l', '', 'r']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "normalize_corpus('123_lir')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
