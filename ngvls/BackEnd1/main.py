# python -m venv .venv
# print("Dhena")
# pip install Flask-Cors

from flask import Flask, render_template,jsonify
from flask_cors import CORS

app = Flask("__name__")
# CORS(app)
CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/a")
def Home():
    # return render_template("index.html")
    return "<h1>Head a</h1>"

@app.route("/members", methods=["GET"])
def member():
    # return {"memberss" : ["Name","Dhanes", "Age","ous","yes"]}
    dat = {"message":"HI hello I got it!!"}
    return jsonify(dat)

@app.route("/questionanswer/<bada>")
def askQuestion(bada):
    from questionans import openAiModelAnswer
    pararaph = '''
    Musk attended Queen’s University in Kingston, Ontario, and in 1992 he transferred to the University of Pennsylvania, Philadelphia, where he received bachelor’s degrees in physics and economics in 1997. He enrolled in graduate school in physics at Stanford University in California, but he left after only two days because he felt that the Internet had much more potential to change society than work in physics. In 1995 he founded Zip2, a company that provided maps and business directories to online newspapers. In 1999 Zip2 was bought by the computer manufacturer Compaq for $307 million, and Musk then founded an online financial services company, X.com, which later became PayPal, which specialized in transferring money online. The online auction eBay bought PayPal in 2002 for $1.5 billion.
    Witness the launch of the SpaceX Dragon capsule, May 25, 2012
    Witness the launch of the SpaceX Dragon capsule, May 25, 2012See all videos for this article
    Musk was long convinced that for life to survive, humanity has to become a multiplanet species. However, he was dissatisfied with the great expense of rocket launchers. In 2002 he founded Space Exploration Technologies (SpaceX) to make more affordable rockets. Its first two rockets were the Falcon 1 (first launched in 2006) and the larger Falcon 9 (first launched in 2010), which were designed to cost much less than competing rockets. A third rocket, the Falcon Heavy (first launched in 2018), was designed to carry 117,000 pounds (53,000 kg) to orbit, nearly twice as much as its largest competitor, the Boeing Company’s Delta IV Heavy, for one-third the cost.
    '''
    # question = "when elon musk lauched spaceX?"
    # question = "space when started?"
    # question = "weight of rocket?"
    question = " study of elon musk"
    # answer = openAiModelAnswer(pararaph, question)
    answer = openAiModelAnswer(pararaph, bada)
    print(answer)
    return jsonify(answer)
    # return answer

@app.route("/convertYtFinalOutput/<videoLink>")
def convertoOtherLanguage(videoLink):
    from translateytVideo import nextGenTranslator

    if(nextGenTranslator(videoLink)):
        return jsonify("OutputStored Successfully!!")


if __name__ == "__main__":
    app.run(debug=True)
# flask --app main  run