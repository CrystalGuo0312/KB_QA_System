import json
import re
import rdflib
from rdflib import URIRef, BNode, Literal
from rdflib import Namespace
from rdflib import Graph

f = open('data.json', 'r')
g1 = Graph()

UniName = Namespace("https://en.wikipedia.org/wiki/")
uni = Namespace("http://example.org/university_information/")


g1.bind('uni', uni)
g1.bind('UniN', "https://en.wikipedia.org/wiki/")

cnt = 0
for line in f:
    print(line)
    txt = eval(line)
    cnt = cnt + 1
    lastbox = []
    try:
        UniName = Namespace("https://en.wikipedia.org/wiki/")
        s = UniName[txt['title']]
        #g1.bind('UniName', UniName)
        g1.bind('UniN', "https://en.wikipedia.org/wiki/")

        #s = rdflib.URIRef('https://en.wikipedia.org/wiki/' + txt['title'])

        # p = rdflib.URIRef('https://en.example.org/Type')
        #
        # o = Literal('University')

        # g1.add((s, p, o))
       # uni = Namespace("http://example.org/university_information/")


      #  g1.bind('Uni', Uni)

        if len(txt['infoBox']) != 0:

            dict = txt['infoBox']
            str = json.dumps(dict)
            box = re.split(r',', str)

            for num in range(len(box) - 1):

                lastbox = re.split(r':', box[num])

                if len(lastbox) == 2:

                    try:
                        rtxt = re.compile(
                            r'"| |　|    |:|：|、|。|\(|\)|（|）|℃|}|{')
                        lastKey = rtxt.sub('', lastbox[0])
                        n = lastKey.replace(' ','_')
                        lastKey = n
                        p = uni[lastKey]
                        # p = rdflib.URIRef(
                        #     'https://en.example.org/' + lastKey)
                        rtxt = re.compile(r'"| |\&gt|\|}|{')
                        lastTest = rtxt.sub('', lastbox[1])
                        print(lastTest)
                        lastTestChild = re.split(
                           r'、|，|；|;|\|', lastTest)

                        for i in range(len(lastTestChild) - 1):

                            o = Literal(lastTestChild[i])

                            g1.add((s, p, o))
                        o = Literal(lastTestChild[len(lastTestChild) - 1])

                        g1.add((s, p, o))

                        lastbox.clear()
                    except:
                        pass

    except Exception as e:
        pass
g1.serialize('RDFdata.rdf')

f.close()