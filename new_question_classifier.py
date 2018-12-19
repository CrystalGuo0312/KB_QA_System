from stanfordNER import sfNER
from nltk.tokenize import word_tokenize
import pdb

def is_wh_question(parsed_question):
    if parsed_question[0].label() == "SBARQ":
        return True
    return False


from stanfordParser import sfParser


def is_who_question(parsed_question):
    if (parsed_question[0][0].leaves()[0].lower() == "who"):
        return True
    return False


def is_how_many_question(parsed_question):
    if (parsed_question[0].leaves()[0].lower() == "how") and (parsed_question[0].leaves()[1].lower() == "many"):
        return True
    return False


def is_what_question(parsed_question):
    if (parsed_question[0][0].leaves()[0].lower() == "what"):
        return True
    return False


def is_where_question(parsed_question):
    if (parsed_question[0][0].leaves()[0].lower() == "where"):
        return True
    return False


def is_when_question(parsed_question):
    if (parsed_question[0][0].leaves()[0].lower() == "when"):
        return True
    return False



def what_question(parsed_question,loc_abb):
    assert (is_what_question(parsed_question))

    if loc_abb != "empty":
        location_entity = loc_abb

       # print("location_entity!!!!!!!!!!:",location_entity)
    else:
        #pdb.set_trace()
        raw_sent = parsed_question[0].leaves()
        ner_parser = sfNER()
        tagged_sent = ner_parser.tag(raw_sent)
        print(tagged_sent)
        location_entity = [w for w, p in tagged_sent if p != "O"]
        # location_entity= location_entity.replace(' ','_')
        location_entity = " ".join(location_entity)
        location_entity = str(location_entity)
        for k,v in dic.items():
            if location_entity in v:
                location_entity = k
    location_entity = location_entity.replace("Motto of ","")
    location_entity = location_entity.replace(' ', '_')

    print("location entity",location_entity)
    #print("1111loction_entity",loction_entity)
    def create_query(location_key):
        # def filter_query(person_key):
        #     return "filter regex(?name,\""+person_key+"\",\"i\")."
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix Uni:   <http://example.org/university_information/> 
        PREFIX UniName: <https://en.wikipedia.org/wiki/>
        select ?Type
        where{
            UniName:""" + location_key + """ 
            Uni:Type
            ?Type
        }
        limit 10
        """
        return query

    def create_query_motto(location_key):

        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix Uni:   <http://example.org/university_information/> 
        PREFIX UniName: <https://en.wikipedia.org/wiki/>
        select ?Motto
        where{
            UniName:""" + location_key + """ 
            Uni:Motto
            ?Motto
        }
        limit 10
        """
        return query

    def create_query_motto_in_English(location_key):

        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix Uni:   <http://example.org/university_information/> 
        PREFIX UniName: <https://en.wikipedia.org/wiki/>
        select ?Motto_in_English
        where{
            UniName:""" + location_key + """ 
            Uni:Motto_in_English
            ?Motto_in_English
        }
        limit 10
        """
        return query

    def create_query_Fomer_names(location_key):
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix Uni:   <http://example.org/university_information/> 
        PREFIX UniName: <https://en.wikipedia.org/wiki/>
        select ?Former_names
        where{
            UniName:""" + location_key + """ 
            Uni:Former_names
            ?Former_names
        }
        limit 10
        """
        return query

    if location_entity == "":

        return "query", "unkown", "unkown"
    else:
        if (parsed_question[0].leaves()[2].lower() == "type" or parsed_question[0].leaves()[3].lower() == "type"):
            query = create_query(location_entity)
            return (query, 'Type', None)

        if (parsed_question[0].leaves()[2].lower() == "motto" or parsed_question[0].leaves()[3].lower() == "motto"):
            query = create_query_motto(location_entity)
            query2 = create_query_motto_in_English(location_entity)
            return (query, query2, 'Motto')
        if (parsed_question[0].leaves()[3].lower() == "former" or parsed_question[0].leaves()[4].lower() == "name"):
            query = create_query_Fomer_names(location_entity)
            return (query, 'Former_names', None)



def name_question(parsed_question,loc_abb,question_list):
    assert (is_who_question(parsed_question))
    raw_sent = parsed_question[0].leaves()
    ner_parser = sfNER()
    tagged_sent = ner_parser.tag(raw_sent)
    print(tagged_sent)
    if loc_abb != "empty":
        location_entity = loc_abb

       # print("location_entity!!!!!!!!!!:",location_entity)

    else:
        location_entity = [w for w, p in tagged_sent if p == "ORGANIZATION"]
        location_entity = " ".join(location_entity)
        location_entity = str(location_entity)
        for k,v in dic.items():
            if location_entity in v:
                location_entity = k

    location_entity = location_entity.replace(' ', '_')
    person_entity = [w for w, p in tagged_sent if p == "PERSON"]
    person_entity = " ".join(person_entity)
    person_entity = str(person_entity)
    person_entity = person_entity.replace(' ', '_')

    def create_query(person_key):

        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix Uni:   <http://example.org/university_information/> 
        PREFIX UniName: <https://en.wikipedia.org/wiki/>
        select ?University ?Type
        where{
            ?University
            ?Type
            ?person. filter regex(?person, '""" + person_key + """')

        }
        limit 10
        """
        return query

    def create_query_chancellor(location_key):
        # def filter_query(person_key):
        #     return "filter regex(?name,\""+person_key+"\",\"i\")."
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix Uni:   <http://example.org/university_information/> 
        PREFIX UniName: <https://en.wikipedia.org/wiki/>
        select ?Chancellor
        where {
            UniName:""" + location_key + """ 
            Uni:Chancellor
            ?Chancellor 

        }
        limit 10
        """
        return query

    if person_entity == "" and location_entity == "":

        return "query", "unkown", "unkown"

    if person_entity == "" and location_entity !="":
        #pdb.set_trace()
#        assert(parsed_question[0].leaves()[2])

        # if parsed_question[0].leaves()[2].lower() is not None:
        #
        #     if (parsed_question[0].leaves()[2].lower() == "chancellor" or parsed_question[0].leaves()[3].lower() == "chancellor"):
        #         query = create_query_chancellor(location_entity)
        if "Chancellor" in question_list:

            query = create_query_chancellor(location_entity)
            return (query, "Chancellor", None)
        else:
            return "query", "unkown", "unkown"

    if person_entity !="" and location_entity == "":

        query = create_query(person_entity)
        return (query, "University", 'Type')


def location_question(parsed_question,loc_abb):

    assert (is_where_question(parsed_question))
    #print(parsed_question)
    if loc_abb != "empty":
        location_entity = loc_abb

        print("location_entity!!!!!!!!!!:",location_entity)
    else:
        raw_sent = parsed_question[0].leaves()

        ner_parser = sfNER()
        tagged_sent = ner_parser.tag(raw_sent)

        location_entity = [w for w, p in tagged_sent if p != "O"]

        location_entity = " ".join(location_entity)
        location_entity = str(location_entity)

        print("location name",location_entity)
        for k,v in dic.items():
            if location_entity in v:
                location_entity = k

    location_entity = location_entity.replace(' ', '_')


    def create_query(location_key):

        query = """

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix Uni:   <http://example.org/university_information/> 
        PREFIX UniName: <https://en.wikipedia.org/wiki/>
        select ?location
            where
            {
            UniName:""" + location_key + """ 
            Uni:Location
            ?location.

            }
           """
        return query

    if location_entity == "":

        return "query", "unkown", "unkown"
    else:

        query = create_query(location_entity)
        return (query, "location", None)


def Established_question(parsed_question,loc_abb):
    assert (is_when_question(parsed_question))

    if loc_abb != "empty":
        location_entity = loc_abb

        print("location_entity!!!!!!!!!!:",location_entity)
    #print(parsed_question)
    else:
        raw_sent = parsed_question[0].leaves()

        ner_parser = sfNER()
        tagged_sent = ner_parser.tag(raw_sent)
        print(tagged_sent)
        location_entity = [w for w, p in tagged_sent if p != "O"]

        location_entity = " ".join(location_entity)
        location_entity = str(location_entity)
        for k,v in dic.items():
            if location_entity in v:
                location_entity = k
    location_entity = location_entity.replace(' ', '_')
    print("location_entity",location_entity)
    def create_query(location_key):

        query = """

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix Uni:   <http://example.org/university_information/> 
        PREFIX UniName: <https://en.wikipedia.org/wiki/>
        select ?Established
        where
       {
            UniName:""" + location_key + """ 
            Uni:Established
            ?Established.

            }
            """
        return query

    if location_entity == "":

        return "query", "unkown", "unkown"
    else:

        query = create_query(location_entity)
        return (query, "Established", None)


def how_many_question(parsed_question,loc_abb):
    assert (is_how_many_question(parsed_question))
    #print(parsed_question)
    if loc_abb != "empty":
        location_entity = loc_abb

        print("location_entity!!!!!!!!!!:",location_entity)
    else:
        #pdb.set_trace()
        raw_sent = parsed_question[0].leaves()
        ner_parser = sfNER()
        tagged_sent = ner_parser.tag(raw_sent)
        print("tagged_sent",tagged_sent)
        location_entity = [w for w, p in tagged_sent if p != "O"]
        location_entity = " ".join(location_entity)
        location_entity = str(location_entity)
        for k,v in dic.items():
            if location_entity in v:
                location_entity = k
    location_entity = location_entity.replace(' ', '_')

    def create_query(location_key):

        #print('Loction', location_key)
        query = """

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix Uni:   <http://example.org/university_information/> 
        PREFIX UniName: <https://en.wikipedia.org/wiki/>
     select ?students
     where
       {
            UniName:""" + location_key + """ 
            Uni:Students
            ?students.
 
            }
            """
        return query

    def create_query2(location_key):
        # def filter_query(location_key):
        #     return "filter regex(?name,\"" + location_key + "\",\"i\")."
    #    print('Loction', location_key)
        query = """

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix Uni:   <http://example.org/university_information/>
        PREFIX UniName: <https://en.wikipedia.org/wiki/>
     select ?Postgraduates
     where
       {
            UniName:""" + location_key + """
            Uni:Postgraduates
            ?Postgraduates.

            }
            """
        return query

    def create_query3(location_key):

        query = """

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix Uni:   <http://example.org/university_information/>
        PREFIX UniName: <https://en.wikipedia.org/wiki/>
     select ?Undergraduates
     where
       {
            UniName:""" + location_key + """
            Uni:Undergraduates
            ?Undergraduates.

            }
            """
        return query

    def create_query4(location_key):

        query = """

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix Uni:   <http://example.org/university_information/>
        PREFIX UniName: <https://en.wikipedia.org/wiki/>
     select ?Administrative_staff
     where
       {
            UniName:""" + location_key + """
            Uni:Administrative_staff
            ?Administrative_staff.

            }
            """
        return query



    if location_entity == "":

        return "query", "unkown", "unkown"
    else:

        if (parsed_question[0].leaves()[2].lower() == "students"):


            query = create_query(location_entity)

            #if (query != None):
            #    pass
            #else:

            return (query, "students", location_entity)


        elif (parsed_question[0].leaves()[2].lower() == "postgraduates"):

            query = create_query2(location_entity)
            return (query, "Postgraduates", None)



        elif (parsed_question[0].leaves()[2].lower() == "undergraduates"):

            query = create_query3(location_entity)
            return (query, "Undergraduates", None)

        elif (parsed_question[0].leaves()[2].lower() == "administrative" and parsed_question[0].leaves()[
            3].lower() == "staff"):

            query = create_query4(location_entity)
            return (query, "Administrative_staff", None)


def quest_cl(parsed_question,question):

    loc_abb = "empty"
    question_list = word_tokenize(question)
    print("question_list",question_list)
    for i, b in dic.items():
        for x in b:
            if x in question_list:
                loc_abb = i
                print("ddddddddd",i)
    if (is_who_question(parsed_question)):
        #pdb.set_trace()
        query, key, key2 = name_question(parsed_question,loc_abb,question_list)
        return (query, key, key2)
    if (is_where_question(parsed_question)):
        query, key, key2 = location_question(parsed_question,loc_abb)
        return (query, key, key2)
    if (is_when_question(parsed_question)):
        query, key, key2 = Established_question(parsed_question,loc_abb)
        return (query, key, key2)
    if (is_how_many_question(parsed_question)):
        query, key, key2 = how_many_question(parsed_question,loc_abb)
        return (query, key, key2)
    if (is_what_question(parsed_question)):
        query, key, key2 = what_question(parsed_question,loc_abb)
        return (query, key, key2)
    return (None, None, None)





dic ={
"University of Western Australia":["Western Australia University","UWA","Uwa"],
"University of New South Wales":["New South Wales University","UNSW","Unsw"],
"RMIT University":["RMIT"],
"University of Technology Sydney":["Technology Sydney University", "UTS","Uts"],
"Swinburne University of Technology":["Swinburne Technology University","Swinburne"],
"University of Wollongong":["Wollongong University","UOW","Uow"],
"University of Southern Queensland":["Southern Queensland University","USQ","Usq"],
"University of the Sunshine Coast":["Sunshine Coast University","USC","Usc"],
"University of Sydney":["Sydney University", "USYD","Usyd"],
"Queensland University of Technology":["Queensland Technology University","QUT","Qut"],
"University of South Australia":["South Australia University", "UniSA"],
"University of Queensland":["Queensland University"],
"Macquarie University":["University of Macquarie University"],
"University of Notre Dame Australia":["Notre Dame Australia University"],
"University of Melbourne":["Melbourne University"],
"University of Canberra":["Canberra University"],
"University of Adelaide":["Adelaide University"],
"University of Divinity":["Divinity University"],

}
#print(dic)