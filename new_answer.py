from SPARQLWrapper import SPARQLWrapper, JSON
from new_question_classifier import how_many_question
import pdb

# _________
def get_answer(query, extract_part):
    if query != None and extract_part != None:
        if extract_part == "unkown":
            return " I don't know"


        else:
            sparql = SPARQLWrapper("http://localhost:3030/Uni_AU_test/query")
            sparql.setReturnFormat(JSON)
            sparql.setQuery(query)

            results = sparql.query().convert()

            case_flag = True

        for result in results["results"]["bindings"]:
            answer = result[extract_part]["value"]
            if answer is not None:
                case_flag = False
                return result[extract_part]["value"]
        if case_flag == True:
            if extract_part == "Former_names":
                return "It doesn't have the former name"
            else:
                return "I don't know."

    else:
        return "I don't know"


def get_answer2(query, extract_part, extract_part2):
    #pdb.set_trace()
    if query != None and extract_part != None:
        if extract_part == "unkown":
            return " I don't know"

        else:
            sparql = SPARQLWrapper("http://localhost:3030/Uni_AU_test/query")
            sparql.setReturnFormat(JSON)
            sparql.setQuery(query)

            results = sparql.query().convert()
            case_flag = True

        if extract_part2 == "Type":
            for result in results["results"]["bindings"]:
               # print("!!!!!!!!!!!!!answer",answer)
               # print("answer2",answer2)
                answer = result[extract_part]["value"]
                answer2 = result[extract_part2]["value"]
                if answer is not None:
                    case_flag = False
                    answer = answer.replace("https://en.wikipedia.org/wiki/", "")
                    answer2 = answer2.replace("http://example.org/university_information/", "")
                    return answer2 + " in the " + answer
            if case_flag == True:
                return "I don't know"

        if extract_part2 == "Motto":
            ans1 = True
            ans2 = True
            for result in results["results"]["bindings"]:
                answer1 = result[extract_part2]["value"]
                if answer1 is not None:
                    ans1 = False

            sparql2 = SPARQLWrapper("http://localhost:3030/Uni_AU_test/query")
            sparql2.setReturnFormat(JSON)
            sparql2.setQuery(extract_part)

            results2 = sparql2.query().convert()

            for result in results2["results"]["bindings"]:
                answer2 = result["Motto_in_English"]["value"]
                if answer2 is not None:
                    ans2 = False

            if ans1 is False and ans2 is False:
                return answer1 + "  /  " + answer2
            if ans1 is True and ans2 is False:
                return answer2
            if ans1 is False and ans2 is True:
                return answer1

            if ans1 is True and ans2 is True:
                return "I don't know"

        for result in results["results"]["bindings"]:
            answer = result[extract_part]["value"]

            if answer is not None:
                case_flag = False

                return answer
        if case_flag == True:

            if extract_part == "students":

                def create_query2(Postgraduates):

                    query1 = """

                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    prefix Uni:   <http://example.org/university_information/>
                    PREFIX UniName: <https://en.wikipedia.org/wiki/>
                 select ?Postgraduates
                 where
                   {
                        UniName:""" + extract_part2 + """
                        Uni:Postgraduates
                        ?Postgraduates.

                        }
                        """
                    return query1

                def create_query3(extract_part2):

                    query2 = """

                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    prefix Uni:   <http://example.org/university_information/>
                    PREFIX UniName: <https://en.wikipedia.org/wiki/>
                 select ?Undergraduates                                       
                 where
                   {
                        UniName:""" + extract_part2 + """
                        Uni:Undergraduates
                        ?Undergraduates.

                        }
                        """
                    return query2

                query1 = create_query2(extract_part2)
                query2 = create_query3(extract_part2)
                # query
                sparql = SPARQLWrapper("http://localhost:3030/Uni_AU_test/query")
                sparql.setReturnFormat(JSON)
                sparql.setQuery(query1)

                results = sparql.query().convert()
                #case_flag = True
                case_flag_Postgraduates = False
                for result in results["results"]["bindings"]:
                    answer1 = result["Postgraduates"]["value"]
                    if answer1 is not None:
                        case_flag_Postgraduates = True
                       # print("Postgraduates is ", answer1)
                    else:
                        case_flag_Postgraduates = False
                      #  print("I don't know")
                sparql = SPARQLWrapper("http://localhost:3030/Uni_AU_test/query")
                sparql.setReturnFormat(JSON)
                sparql.setQuery(query2)

                results = sparql.query().convert()
                case_flag_Undergraduates = False
                for result in results["results"]["bindings"]:
                    answer2 = result["Undergraduates"]["value"]
                    if answer2 is not None:
                        case_flag_Undergraduates = True
                       # case_flag = False

                    else:
                        case_flag_Undergraduates = False


                if case_flag_Undergraduates == False and case_flag_Postgraduates == False:
                    return "I don't know"
                elif case_flag_Undergraduates == True and case_flag_Postgraduates == True:
                    return "Postgraduate:" + answer1 + "   " + "Undergraduate:"+ answer2
                elif case_flag_Undergraduates == False and case_flag_Postgraduates == True:
                    return "Postgraduate:" + answer1
                elif case_flag_Undergraduates == True and case_flag_Postgraduates == False:
                    return "Undergraduate:" + answer2

                # if answer1 is not None and answer2 is not None:
                #
                #     return answer1 + " " + answer2
                #
                # elif answer1 is not None and answer2 is None:
                #
                #     return answer1
                #
                # elif answer1 is None and answer2 is not None:
                #
                #     return answer2

    else:
        return "I don't know"