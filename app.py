from flask import Flask, render_template, request
app = Flask("my_app")

@app.route("/")
def home():
	return render_template("index.html")


@app.route("/<name>")
def say_hello_to(name):
	return render_template("hello.html", user=name)

@app.route("/feedback", methods=["POST"])
def get_feedback():
	#request.values is a dictionary holiding any POST request data thats not already part of the url
	data = request.values
	return render_template("feedback.html", form_data=data)


app.run(debug=True)