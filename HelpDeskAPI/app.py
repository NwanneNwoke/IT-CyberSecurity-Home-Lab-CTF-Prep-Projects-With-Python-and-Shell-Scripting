from flask import Flask, request, jsonify

app = Flask(__name__)
tickets = []

@app.route('/ticket', methods=['POST'])
def create_ticket():
    data = request.json
    ticket = {"id": len(tickets)+1, "issue": data["issue"]}
    tickets.append(ticket)
    return jsonify(ticket), 201

@app.route('/tickets', methods=['GET'])
def get_tickets():
    return jsonify(tickets)

if __name__ == '__main__':
    app.run(debug=True)
