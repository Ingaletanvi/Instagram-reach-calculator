from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate_reach_impressions():
    data = request.json
    followers = data['followers']
    reach_rate = data['reach_rate']
    impression_rate = data['impression_rate']
    
    reach = followers * reach_rate
    impressions = followers * impression_rate
    
    return jsonify({
        'reach': reach,
        'impressions': impressions
    })

if __name__ == '__main__':
    app.run(debug=True)