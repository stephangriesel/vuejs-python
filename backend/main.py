from flask import Flask, jsonify, request
from flask_cors import CORS 

app = Flask(__name__)

app.config.from_object(__name__)

# CORS(app, resources={r"/*":{'origins':"*"}})
CORS(app, resources={r"/*":{'origins':"http://localhost:8080", "allow_headers":"Access-Control-Allow-Origin"}})

@app.route('/', methods=['GET'])
def greetings():
  return("Hello!!")

@app.route('/shark', methods=['GET'])
def shark():
  return("WHAT! Shark!")

LIBRARY = [
  {
    "artist":"ACDC",
    "song":"Highway To Hell",
    "played": True,
  },
  {
    "artist":"Silverchair",
    "song":"Freak",
    "played": True,
  },
  {
    "artist":"Guns 'n Roses",
    "song":"Paradise City",
    "played": False,
  },
  {
    "artist":"Incubus",
    "song":"Pardon Me",
    "played": False,
  }
]

@app.route("/library", methods=["GET", "POST"])
def all_libraries():
  response_object = {"status":"success"}
  if request.method == "POST":
    post_data = request.get_json()
    LIBRARY.append({
      "artist":post_data.get("artists"),
      "song":post_data.get("song"),
      "played":post_data.get("played")})
    response.object["message"] = "Item added!"
  else:
    response_object["library"] = LIBRARY
  return jsonify(response_object)
  

if __name__ == "__main__":
  app.run(debug=True)
