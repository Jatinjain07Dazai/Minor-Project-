import textract
import nltk
from nltk.util import ngrams as nltk_ngrams


def common_ngram_txt(tokens1,tokens2,size=15):
    print('Checking ngram length {}'.format(size))
    ng1=set(nltk_ngrams(tokens1, size))
    ng2=set(nltk_ngrams(tokens2, size))
 
    match=set.intersection(ng1,ng2)
    print('..found {}'.format(len(match)))
 
    return match


def n_concordance_offset(text,phraseList):
    c = nltk.ConcordanceIndex(text.tokens, key = lambda s: s.lower())
 
    #Find the offset for each token in the phrase
    offsets=[c.offsets(x) for x in phraseList]
    offsets_norm=[]
    #For each token in the phraselist, find the offsets and rebase them to the start of the phrase
    for i in range(len(phraseList)):
        offsets_norm.append([x-i for x in offsets[i]])
    #We have found the offset of a phrase if the rebased values intersect
    #via http://stackoverflow.com/a/3852792/454773
    intersects=set(offsets_norm[0]).intersection(*offsets_norm[1:])
 
    return intersects
 
def ngram_sweep_txt(txt1,txt2,ngram_min=8,ngram_max=50):
    tokens1 = nltk.word_tokenize(txt1)
    tokens2 = nltk.word_tokenize(txt2)
 
    text1 = nltk.Text(tokens1)
    text2 = nltk.Text(tokens2)
 
    ngrams=[]
    strings=[]
    ranges=[]
    for i in range(ngram_max,ngram_min-1,-1):
        #Find long ngrams first
        newsweep=common_ngram_txt(tokens1,tokens2,size=i)
        for m in newsweep:
            localoffsets=n_concordance_offset(text2,m)
 
            #We need to avoid the problem of masking shorter ngrams by already found longer ones
            #eg if there is a common 3gram in a doc2 4gram, but the 4gram is not in doc1
            #so we need to see if the current ngram is contained within the doc index of longer ones already found
 
            for o in localoffsets:
                fnd=False
                for r in ranges:
                    if o>=r[0] and o<=r[1]:
                        fnd=True
                if not fnd:
                    ranges.append([o,o+i-1])
                    ngrams.append(m)
    return ngrams,ranges,txt1,txt2


 
def ngram_sweep(fn1,fn2,ngram_min=8,ngram_max=50):
    txt1 = fn1
    txt2 = fn2
    # txt1 = textract.process(fn1).decode('utf8')
    # txt2 = textract.process(fn2).decode('utf8')
    ngrams,ranges,txt1,txt2=ngram_sweep_txt(txt1,txt2,ngram_min=ngram_min,ngram_max=ngram_max)
    return ngrams,ranges,txt1,txt2


def n_concordance(txt,phrase,left_margin=0,right_margin=0):
    #via https://simplypython.wordpress.com/2014/03/14/saving-output-of-nltk-text-concordance/
    tokens = nltk.word_tokenize(txt)
    text = nltk.Text(tokens)
 
    phraseList=nltk.word_tokenize(phrase)
 
    intersects= n_concordance_offset(text,phraseList)
 
    concordance_txt = ([text.tokens[list(map(lambda x: x-left_margin if (x-left_margin)>0 else 0,[offset]))[0]:offset+len(phraseList)+right_margin]
                        for offset in intersects])
 
    outputs=[''.join([x+' ' for x in con_sub]) for con_sub in concordance_txt]
    return outputs
 
def concordance_reporter(fn1='1.txt', fn2='2.txt',fo='3.txt',ngram_min=6,ngram_max=10, left_margin=2,right_margin=2,n=5):
    fo=fo.replace('.txt','_ngram_rep{}.txt'.format(n))
    results = []
    f=open(fo, 'w+')
    f.close()
 
    print('Handling {}'.format(fo))
    ##
    ngrams,strings, txt1, txt2=ngram_sweep(fn1,fn2,ngram_min,ngram_max)
    #Remove any redundancy in the ngrams...
    ngrams=set(ngrams)
    with open(fo, 'a') as outfile:
        outfile.write('REPORT FOR ({} and {}\n\n'.format(fn1,fn2))
        print('found {} ngrams in that range...'.format(len(ngrams)))
        
        i = 0
        for m in ngrams:
            output = []
            i += 1
            mt=' '.join(m)
            output.append(f"{i}  " + mt)
            for c in n_concordance(txt1,mt,left_margin,right_margin):
                output.append(f"{i}.{i}  "+ c) 
            results.append(output)
    return results











# if __name__ == '__main__':

#     text1 = """The characterization of Sparrow is based on a combination of The Rolling Stones' guitarist Keith Richards and Looney Tunes cartoons,
# specifically the characters Bugs Bunny and Pepé Le Pew. 
# He first appears in the 2003 film Pirates of the Caribbean: The Curse of the Black Pearl.
# He later appears in the sequels Dead Man's Chest (2006), At World's End (2007), On Stranger Tides (2011), and Dead Men Tell No Tales (2017).

# In the films, Sparrow is one of the nine pirate lords in the Brethren Court, the Pirate Lords of the Seven Seas. 
# He can be treacherous and survives mostly by using wit and negotiation rather than by force, 
# opting to flee most dangerous situations and to fight only when necessary.
# Sparrow is introduced seeking to regain his ship, the Black Pearl, from his mutinous first mate, Hector Barbossa.
# Later, he attempts to escape his blood debt to the legendary Davy Jones while fighting the East India Trading Company.
# In later adventures he searches for the Fountain of Youth and the Trident of Poseidon. """


    
# textmain = """alware  Malware is a general term that encompasses all software designed to do harm.cross checking the assigment because of work load hehehe !
# He can be treacherous and survives mostly by using wit and negotiation rather than by force, 
# opting to flee most dangerous situations and to fight only when necessary.
# Sparrow is introduced seeking to regain his ship, the Black Pearl, from his mutinous first mate, Hector Barbossa.
# Later, he attempts to escape his blood debt to the legendary Davy Jones He later appears in the sequels Dead Man's Chest (2006), At World's End (2007), On Stranger Tides (2011), and Dead Men Tell No Tales (2017).

# In the films, Sparrow is one of the nine pirate lords in the Brethren Court, the Pirate Lords of the Seven Seas. 
# He can be treacherous and survives mostly by using wit and negotiation rather than by force, 
# opting to flee most dangerous situations and to fight only when necessary. """


# concordance_reporter(fn1=textmain, fn2=text1, ngram_min=10,ngram_max=40,left_margin=15,right_margin=15)