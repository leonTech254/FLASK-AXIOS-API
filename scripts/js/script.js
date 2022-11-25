function SubmitData()
{
    // alert("hello leon")
    let name=document.getElementById("name").value;
    let school=document.getElementById("school").value;
    let age=document.getElementById("age").value;
    

    // simple validatation
    if (name!="" || school!="" || age!="")
    {   //submitting data inform of json
        data={"name":name,"school":school,"age":age}
        // submiting the data to flask usin axios
        url="http://127.0.0.1/leon" //points to flask end point
        axios.post(url,data) //takes two argumente the url for posting data and the data you are posting
        // .then -if the http response is 200 ok
        .then((res)=>{
            // res is the response from the the flask server
            console.log(res.data)
        })
        // .catch -if the http response not 200 ok

        .catch((err)=>{

            alert("error ")
        })



        
    }else
    {
        alert("all field required")
    }
}