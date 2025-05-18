from flask import Flask, request, jsonify
from flask_cors import CORS
from schema import schema

app = Flask(__name__)
CORS(app)

@app.route("/graphql", methods=["POST"])
def graphql_post():
    data = request.get_json()

    if not data or "query" not in data:
        return jsonify({"error": "Falta la consulta GraphQL"}), 400

    result = schema.execute(
        data["query"],
        variables=data.get("variables"),
        operation_name=data.get("operationName")
    )

    response = {}
    if result.errors:
        response["errors"] = [str(error) for error in result.errors]
    if result.data:
        response["data"] = result.data

    return jsonify(response)

@app.route("/", methods=["GET"])
def index():
    return """
    <html>
        <head><title>GraphQL API</title></head>
        <body>
            <h2>GraphQL API disponible en <code>/graphql</code></h2>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
