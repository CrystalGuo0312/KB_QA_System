from stanfordParser import sfParser
from new_question_classifier import quest_cl
from new_answer import get_answer
from new_answer import get_answer2
from nltk.tokenize import word_tokenize
import pdb

def main(question):
    question = upper_first_letter(question)
    #print("!!!!!!!!!!!!!",question)
    parser=sfParser()
    parsed_iter=parser.raw_parse(question)

   # print("parsed_iter：",parsed_iter)

    for iter in parsed_iter:
        parsed_question=iter
        print("1",parsed_question)



    #print("Q:%s"%question)
    #pdb.set_trace()
    query,key_value, key_value2=quest_cl(parsed_question,question)

    if query!=None and key_value!=None:
        if key_value2 == None:
            print("A:")
            get_answer(query,key_value)
            return get_answer(query,key_value)
          #  print("----------------------------")
          #  print()
        else:
            #get_answer(query, key_value, key_value2)
            get_answer2(query, key_value,key_value2)
            return get_answer2(query, key_value,key_value2)

    else:
        # print("Haven't defined this kind of question. "
        #       "You can define it now!!!")
        # print("----------------------------")
        # print()
        return "Haven't defined this kind of question."

#new method!!!!!!!!!!!!
def upper_first_letter(sentence):
    x = word_tokenize(sentence)
    print(x)
    t =[]
    nu = 0
    for i in x:
        if nu < 2:
            nu = nu + 1
            t.append(i)
            pass
        elif i =="of":
            t.append(i)
        else:
            y = i[0].upper() + i[1:]
            t.append(y)
    f = " "
    new_upper = f.join(t)
    return new_upper

if __name__ == '__main__':

    while(1):
            question=input()
            main(question)
            print("this is the return", main(question))
