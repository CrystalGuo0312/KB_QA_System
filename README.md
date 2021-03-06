## Knowledge Base Construction and Question Answering for Australian Universities ##

### Introduction ###

Questing Answering (QA) systems aim at automatically generating answers to the questions posed by humans. The common QA methods infer answers from either a structured knowledge base or raw text. While raw text does contain rich information, understanding the semantics of the contents is difficult due to its unstructured form. In contrast, knowledge base (KB) organizes information in a pre-defined schema, thereby facilitates compositional reasoning. Especially for the domain-specific QA systems, KB is able to produce more repeatable and accurate responses to questions efficiently. In the thesis, our goal is to establish a robust KB-QA system which can provide accurate answers to various questions about the universities in Australia. Specifically, we carefully construct our KB by a deep exploration of Wikipedia so as the knowledge is as comprehensive as possible. We parsing questions in the pipeline of part-of-speech (POS) tag prediction, name-entity recognition (NER) and syntactic structure assignation by employing some advanced techniques. We build rules to bridge the parsed questions and our KB so that the computer can understand the semantics of the questions and return reliable answers.

### Prerequisites ###

Library: StanfordNERTagger, StanfordParser, BeautifulSoup, Request, json, re, rdflib

Database: Jena - Fuseki

Environment: pycharm

Server：linux

