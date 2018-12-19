# from flask import Flask, request, render_template
# from main import main
#
# app = Flask(__name__)
#
# #@app.route('/')
# #def hello_world():
# #    return 'Hello World!'
#
# @app.route("/")
# def hello():
#     return render_template('index.html')
#
#
# @app.route("/question", methods=['POST'])
# def echo():
#     print("For simplify problem, I only deal with 2 kind of question")
#     print("1/Who-question\t2/Where-question")
#     print("Example question: ")
#     print("\tWho is Barack Obama?")
#     print("\tWhere is Eiffel Tower?")
#     print("\tWho is Bill Gate?")
#     print("There will be more than 1 answer (may be duplicate) but they use for user selection")
#     print("Where-question may not get a good result. Reason is NERtagger to tag LOCATION is not perfect now!")
#
#     answer1 = main(request.form['text']+"")
#     #answer1 = main("Where is James Cook University?")
# #    answer1 = answer1.replace("_",' ')
#     return render_template('index.html', text=answer1, question = request.form['text'])
#
#
# if __name__ == '__main__':
#     app.debug = True
#     app.run()

from flask import Flask, request, render_template
from new_main import main

app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello World!'

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/question", methods=['POST'])
def echo():
    # print("For simplify problem, I only deal with 2 kind of question")
    # print("1/Who-question\t2/Where-question")
    # print("Example question: ")
    # print("\tWho is Barack Obama?")
    # print("\tWhere is Eiffel Tower?")
    # print("\tWho is Bill Gate?")
    # print("There will be more than 1 answer (may be duplicate) but they use for user selection")
    # print("Where-question may not get a good result. Reason is NERtagger to tag LOCATION is not perfect now!")

    answer1 = main(request.form['text']+"")
    #answer1 = main("Where is James Cook University?")
    answer1 = answer1.replace("_",' ')
    return render_template('index.html', text=answer1, question = request.form['text'])


if __name__ == '__main__':
    app.debug = True
    app.run()
