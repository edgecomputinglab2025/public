from flask import Flask, request, jsonify
import json
from flask_cors import CORS  # CORSをインポート

app = Flask(__name__)
CORS(app)  # これで全てのオリジンからのアクセスを許可

@app.route('/save_data', methods=['POST'])
def save_data():
    try:
        data = request.json  # JSON データを受け取る
        timestamp = data['timestamp']
        acceleration = data['acceleration']
        rotation = data['rotation']

        # データをファイルに保存
        with open("sensor_data.json", "a") as file:
            file.write(json.dumps(data) + "\n")

        return jsonify({"status": "success", "message": "Data saved successfully!"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)