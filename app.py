from flask import Flask,render_template,request,redirect,url_for
import gpt,insert_data
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask",methods=["POST","GET"])
def ask():
    if request.method == "POST":
        question = request.form["promptmsg"]

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        # gptreply=gpt.gpt_reply(question)
        # # print(gptreply)


        #inser data into the postgresqlDB
        insert_data.insert(question=question,answer=current_time) #replace anwer to be gpt_replay after fix token error
        
        # return redirect(url_for("result",result=gptreply))
        return redirect(url_for("result",result=question+'\n'+current_time))
    
    else:
        return render_template("ask.html")

@app.route("/<result>")
def result(result):
        return render_template('result.html',prompt=result)

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)