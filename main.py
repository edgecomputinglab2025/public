from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_data():
    # クライアントから送信されたJSONデータを取得
    data = request.json
    
    # データをログに出力
    timestamp = data.get('timestamp')
    acceleration = data.get('acceleration')
    rotation = data.get('rotation')

    if timestamp is not None and acceleration is not None and rotation is not None:
        print(f"Timestamp: {timestamp}")
        print(f"Acceleration: {acceleration}")
        print(f"Rotation: {rotation}")
        
        # 必要であれば、データをファイルに保存、データベースに記録など
        # 例：保存処理（ファイルやDBなど）
        
        return jsonify({"status": "success", "message": "Data received successfully"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)