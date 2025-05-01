from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import psycopg2

app = Flask(__name__)
CORS(app)  # 모든 오리진 허용

# 환경변수 기반 설정
#   export DB_HOST=<Cloud SQL Private IP>
DB_HOST = os.getenv('DB_HOST', '10.36.192.3')
DB_NAME = os.getenv('DB_NAME', 'pioneers')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', 'postuser132')

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/api/send', methods=['GET'])
def send():

    return jsonify(response='Received')

@app.route('/api/add-user', methods=['POST'])
def add_user():
    # 고정된 사용자 정보
    username = 'testuser'
    email = 'testuser@example.com'

    conn = get_db_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                (username, email)
            )
    conn.close()
    return jsonify(
        response='User added',
        user={'username': username, 'email': email}
    )

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status='ok'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
