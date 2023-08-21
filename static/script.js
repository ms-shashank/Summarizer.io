document.addEventListener("DOMContentLoaded", function() {
    const inputText = document.getElementById("inputText");
    const summarizeButton = document.getElementById("summarizeButton");
    const summaryOutput = document.getElementById("summaryOutput");

    summarizeButton.addEventListener("click", function() {
        const text = inputText.value;

        const data = {
            text: text
        };
        // Send the text to the server for summarization using fetch
        fetch("/summarize", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        })
        .then(response => response.json())
        .then(data => {
            // Update the summaryOutput element with the received summary
            summaryOutput.textContent = data.summary;
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
