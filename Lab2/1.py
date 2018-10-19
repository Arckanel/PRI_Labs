import nltk
import re
import string
#Ex4 - usar input() se estiver a usar python 3
#Exercicio 2 usar log base 10

#Reads the file contents (lines) - it does remove the punctuation        
def readDocLines(file):
    c = []
    for line in file:
        line=(line.strip('\n')).lower()
        line = re.sub('['+ string.punctuation +']', '', line)
        for word in nltk.word_tokenize(line):
            c.append(word)
    return c
#Reads the names of the documents to open (doesn't remove the punctuation)
def readDocNames(file):
    names = []
    for line in file:
        line=(line.strip('\n')).lower()
        for word in nltk.word_tokenize(line):
            word=word
            names.append(word)
    return names

#Creates a dictionary with each document's words and its frequency
def countWordOccurrence(words):
    count={}
    for w in words:
        if w not in count:
            count[w]=1
        else:
            count[w]+=1
    return count

#Reads the name of the documents to open, then, for each document, it reads its content, prints it and the document's word frequency
def readFile(doc):
    file=open(doc, 'r')
    docsCounters={}
    contents = readDocNames(file)
    for document in contents: #for each document in the document list..
        currDoc = open(document,'r') #opens the document
        currDocContent = readDocLines(currDoc) #reads document content
        counter = countWordOccurrence(currDocContent) #counts word frequency
        docsCounters[document]=counter
        #print (docsCounters)
        # print (currDocContent) #Prints the words in the document
        # print ('Doc: ' + document + ' ' + str(counter)) #prints the word count for the document
    return docsCounters

#Creates a dictionary containing each word in the texts and their occurrence frequency in each document
def createDictionary(item):
    wordVector={}
    n = 1
    for i in item:
       # print(i) #nome do documneto
      # print (item[i]) 
       for w in (item[i]):
            word=item[i][w]
            #print (w + " " + str(word)) # w eh a palavra
            if w not in wordVector:
                wordVector[w] = [(n,word)]
            else:
                wordVector[w].append((n,word))
       n+=1
    return (wordVector)            

#Counts for each word, in how many documents it appears
def countDocsContaining(vector):
    docOcc={}
    for w in vector:
        #print (w)
        docOcc[w]=len(vector[w])
    return (docOcc)

def countTerms(doc):
    counter=0
    file=open(doc, 'r')
    contents = readDocNames(file)
    for document in contents: #for each document in the document list..
        currDoc = open(document,'r') #opens the document
        currDocContent = readDocLines(currDoc) #reads document content
        for words in currDocContent:
            for w in words:
                counter+=1
    return counter

def countUniqueTerms(dic):
    counter=0
    for words in dic:
        #print(words)
        counter+=1
    return counter
    
def fnumDocs (doc):
    file=open(doc, 'r')
    docs = readDocNames(file)
    return len(docs)
    
def run(file): 
    numDocs = fnumDocs(file)
    docTerms = readFile(file) #Extracts the terms and their frequency from each document and puts it all in an array
    numTerms = (countTerms(file)) #Number of terms on all of the documents (includes the repetitions)
    dic = createDictionary(docTerms) #indexes every term, and for each term checks how many times it appears in each document
    uniques = (countUniqueTerms(dic)) # Unique terms from all the documents
    wordOccurencesInDocs = (countDocsContaining(dic)) #In how many documents does each term appear?
    text = input('Insert the query: \n')
    print(numDocs)
    return

run('docs.txt')