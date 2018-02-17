//var endpoint = "http://127.0.0.1:5000/"
var get_prompt = "get-suggestion"
var endpoint = "localhost:5000/"

$(document).ready(
    
    fetch("http://localhost:5000/get-suggestion")
        .then(response => response.text())
        .then(text => $(".question").text(text))

)

