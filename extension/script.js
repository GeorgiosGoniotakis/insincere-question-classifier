
document.getElementById("submitQuestion").addEventListener("click", submitInputText);

function submitInputText() {
	var input = document.getElementById("question").value;
	classify(input);
}


function classify(inputText) {
	const Url='https://ttds.tech/classify';

	fetch(Url, {
	    method: "POST",
	    headers: {
		"Content-Type": "application/json",
		"Accept": "application/json",
	},
	    body: JSON.stringify({"question": inputText})
	}).then(data=>{return data.json()})
	  .then(res=>{document.getElementById("result").innerHTML = "Result: " + res.result});
}
