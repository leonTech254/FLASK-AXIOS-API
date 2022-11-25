from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resorces={r'/*': {"orgins": '*'}})


@app.route("/")
def home():
    return "welcome to leon Application"


@app.route("/leon", methods=['GET', 'POST'])
def postDataDemo():
    if request.method == "POST":
        contents = request.get_json()
        name = contents['name']
        school = contents['school']
        age = contents['age']
        # ####################################################
        #                                                    #
        # validate the data before data inserting to database#
        #                                                    #
        ######################################################
        print(name)
        print(school)
        print(age)
        # return response after completing your oparations
        return f"hello {name} your data has been posted successfully"
    return "data"


if __name__ == "__main__":
    app.run(debug=True)
