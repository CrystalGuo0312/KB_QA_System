from nltk.tag.stanford import StanfordNERTagger

STANFORD_NER_CLF="/Users/guoguo/Downloads/stanford-ner-2018-02-27/classifiers/english.all.3class.distsim.crf.ser.gz"
STANFORD_JAR="/Users/guoguo/Downloads/stanford-ner-2018-02-27/stanford-ner.jar"
def sfNER(jar_path=STANFORD_JAR,clf_path=STANFORD_NER_CLF):
    return StanfordNERTagger(STANFORD_NER_CLF,STANFORD_JAR)
