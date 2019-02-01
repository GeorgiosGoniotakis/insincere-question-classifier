
document.getElementById("submitQuestion").addEventListener("click", submitInputText);

function submitInputText() {
	var input = document.getElementById("question").value;
	var models = document.getElementsByName("search");
	
	var model;
	for(var i = 0; i < models.length; i++){
	    if(models[i].checked){
		model = models[i].value;
		break;
	    }
	}
	console.log(model);
	document.getElementById("input-text").innerHTML = "<b>Question</b>: " + input
	document.getElementById("input-model").innerHTML = "<b>Model</b>: " + model
	document.getElementById("result").innerHTML = "<b>Result</b>: Calculating ...";
	classify(input, model);
}


function classify(inputText, model) {
	const Url='https://ttds.tech/classify';
	//const Url = 'http://127.0.0.1:5000/classify';	

	fetch(Url, {
	    method: "POST",
	    headers: {
		"Content-Type": "application/json",
		"Accept": "application/json",
	},
	    body: JSON.stringify({"question": inputText, "model":"svm"})
	}).then(data=>{return data.json()})
	  .then(res=>{
		a = res.result
		console.log(a)
		if (a == 0) {
			document.getElementById("result").innerHTML = "<b>Result</b>: <font color='green'>Sincere</font>";
		} else if (a == 1) {
			document.getElementById("result").innerHTML = "<b>Result</b>: <font color='red'>Insincere</font>";
		}
});
}
