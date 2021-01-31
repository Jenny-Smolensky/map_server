from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from Marker import Marker

app = Flask(__name__)
markers_list = []


@app.route("/", methods=["GET"])
@cross_origin()
# default route
def home():
    return render_template("index.html")


# route to get markers
@app.route("/markers", methods=["GET"])
@cross_origin()
def get_markers_list():
    response = ""
    if len(markers_list) != 0:
        response = markers_list
    return jsonify(response)


# route to post new marker
@app.route("/add_marker", methods=['POST'])
@cross_origin()
def add_marker():
    request_dict = request.get_json()

    response = {
        'Success': 'marked',
        'ErrorMessage': ''
    }

    parse_response = Marker.parse_from_json(request_dict)
    if not parse_response[0]:
        response['Success'] = 'Failed'
        response['ErrorMessage'] = parse_response[1]

    else:
        add_new_marker(parse_response[1])

    return jsonify(response)


def add_new_marker(marker):
    new_marker_str = marker.to_str()
    if not markers_list.__contains__(new_marker_str):
        markers_list.append(new_marker_str)
    print(len(markers_list))
    # add to file/db


if __name__ == "__main__":
    CORS(app)
    app.run(debug=True, port=8000)
