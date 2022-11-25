<h1>FLASK-AXIOS API IMPLEMENTATION</h1>
<h3 style="text-decoration:underline;">PROCEDURE</h3>
<div>
<ol>
<li>install python requirements ,flask,flask_cors <kbd>(pip install ...)</kbd></li>
<li>start server <kbd>python3 main.py</kbd> (running on port 5000) in "FlaskServer" directory</li>
<li>start GUI web directory=in root directory(index.html)</li>

</ol>

</div>

<span style="color:red;">AXIOS CODE</span> <br> <hr>

<pre>
<code>
let  data={"name":name,"school":school,"age":age}
url="http://127.0.0.1:5000/leon" 
axios.post(url,data)   
.then((res)=>{
    console.log(res.data)
            response.innerHTML=res.data
        })
        .catch((err)=>{
            alert("error ")
        })

</code>
</pre>
<span style="color:white;">
<span style="color:green;">url</span>-points to flask server endpiont <br>
axios.post(arg1,arg2) <br>
<span style="color:green;">arg1</span>=url,<span style="color:green;">arg2</span>=the json data
</span><br>
<span style="color:red;">FLASK CODE</span> <br> <hr>

<pre>
<code>
@app.route("/leon", methods=['GET', 'POST'])
def postDataDemo():
    if request.method == "POST":
        contents = request.get_json()
        name = contents['name']
        school = contents['school']
        age = contents['age']
        print(name)
        print(school)
        print(age)
        # return response after completing your oparations
        return f"hello {name} your data has been posted successfully"
    return "data"

</code>
</pre>
