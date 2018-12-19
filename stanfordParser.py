STANFORD_JAR="/Users/guoguo/Downloads/stanford-corenlp-full-2018-02-27/stanford-corenlp-3.9.1.jar"
STANFORD_MODEL="/Users/guoguo/Downloads/stanford-corenlp-full-2018-02-27/stanford-corenlp-3.9.1-models.jar"

from nltk.parse.stanford import StanfordParser

def sfParser(jar_path=STANFORD_JAR,model_path=STANFORD_MODEL):
    return StanfordParser(STANFORD_JAR,STANFORD_MODEL)