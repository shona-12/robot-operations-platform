from flask import Flask, jsonify, request, send_from_directory
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# ================= DATABASE =================

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="robotops123",
        database="robotops"
    )


# ================= FRONTEND =================

@app.route("/")
def home():
    return send_from_directory(
        "/workspaces/robot-operations-platform/frontend",
        "index.html"
    )


# ================= ROBOTS =================

@app.route("/robots", methods=["GET"])
def robots():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id,
            robot_code,
            status,
            battery,
            location,
            last_seen
        FROM robots
        ORDER BY id
    """)

    robots_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(robots_data)


# ================= TELEMETRY =================

@app.route("/telemetry", methods=["POST"])
def telemetry():

    data = request.get_json()

    robot_code = data["robot_code"]
    battery = data["battery"]
    location = data["location"]
    status = data["status"]

    connection = get_db_connection()
    cursor = connection.cursor()

    # Update current robot information
    cursor.execute("""
        UPDATE robots
        SET
            battery = %s,
            location = %s,
            status = %s,
            last_seen = CURRENT_TIMESTAMP
        WHERE robot_code = %s
    """, (
        battery,
        location,
        status,
        robot_code
    ))

    # Store telemetry history
    cursor.execute("""
        INSERT INTO telemetry
        (robot_id, battery, location, status)
        SELECT
            id,
            %s,
            %s,
            %s
        FROM robots
        WHERE robot_code = %s
    """, (
        battery,
        location,
        status,
        robot_code
    ))

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Telemetry received",
        "robot_code": robot_code
    })


# ================= ASSIGNMENT =================

@app.route("/robots/<robot_code>/assignment", methods=["GET"])
def get_assignment(robot_code):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            a.id,
            r.robot_code,
            a.task_name,
            a.status,
            a.created_at
        FROM assignments a
        JOIN robots r
            ON a.robot_id = r.id
        WHERE r.robot_code = %s
          AND a.status = 'assigned'
        ORDER BY a.id DESC
        LIMIT 1
    """, (robot_code,))

    assignment = cursor.fetchone()

    cursor.close()
    connection.close()

    if assignment:
        return jsonify(assignment)

    return jsonify({
        "message": "No assignment"
    })


# ================= HEALTH CHECK =================

@app.route("/health", methods=["GET"])
def health():

    try:
        connection = get_db_connection()
        connection.close()

        return jsonify({
            "status": "healthy",
            "database": "connected"
        })

    except Exception as error:

        return jsonify({
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(error)
        }), 500


# ================= START SERVER =================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )