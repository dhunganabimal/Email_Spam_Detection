async function checkSpam() {
    const sender = document.getElementById("sender").value;
    const subject = document.getElementById("subject").value;
    const body = document.getElementById("body").value;

    if (!sender || !subject || !body) {
        alert("Please fill all fields");
        return;
    }

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            sender,
            subject,
            body
        })
    });

    const data = await response.json();

    const resultDiv = document.getElementById("result");
    resultDiv.classList.remove("hidden", "spam", "safe");

    if (data.result === "SPAM") {
        resultDiv.classList.add("spam");
        resultDiv.innerHTML = `SPAM EMAIL<br>Confidence: ${data.confidence}`;
    } else {
        resultDiv.classList.add("safe");
        resultDiv.innerHTML = `SAFE EMAIL<br>Confidence: ${data.confidence}`;
    }
}
