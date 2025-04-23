from flask import Flask, request, jsonify
from flask_cors import CORS            # CORS 활성화용
import os
import psycopg2

app = Flask(__name__)
CORS(app)  # 모든 오리진 허용; 필요시 특정 도메인만 허용하도록 설정 가능 :contentReference[oaicite:6]{index=6}

# 환경변수 기반 설정
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

@app.route('/api/send', methods=['POST'])
def send():
    payload = request.get_json()
    msg = payload.get('message')

    # Cloud SQL (PostgreSQL) 연결
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO messages (text) VALUES (%s)",
                (msg,)
            )
    conn.close()

    return jsonify(response='Received')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
