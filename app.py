from flask import Flask, render_template, request, jsonify
from summary import summarize
#app = Flask(__name__)
app = Flask(__name__, template_folder='templates')
#app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "web_app"))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("inputText")
        summary = summarize(text, 0.3)  # Adjust per as needed

        # Integrate your summarization code here
        # For example:
        # summary = my_summarization_function(text, 0.3)

        # Return the rendered template with summary and input_text
        return render_template("index.html", summary=summary, input_text=text)

    return render_template("index.html", summary="", input_text="")

@app.route("/summarize", methods=["POST"])
def summarize_text():
    data = request.json  # Get the JSON data from the request
    text = data.get("text")
    summary = summarize(text, 0.5)  # Adjust per as needed

    # Return the summary as a JSON response
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
