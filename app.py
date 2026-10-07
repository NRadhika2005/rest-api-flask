from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "students.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            course TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Student Management REST API",
        "status": "API is running"
    }), 200


@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must contain JSON data"}), 400

    required_fields = ["name", "email", "course", "age"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    name = data["name"]
    email = data["email"]
    course = data["course"]
    age = data["age"]

    if not isinstance(age, int):
        return jsonify({"error": "Age must be an integer"}), 400
    if age <= 0:
        return jsonify({"error": "Age must be greater than 0"}), 400

    conn = get_db_connection()
    try:
        cursor = conn.execute("""
            INSERT INTO students (name, email, course, age)
            VALUES (?, ?, ?, ?)
        """, (name, email, course, age))
        conn.commit()
        student_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error": "Email already exists"}), 400
    finally:
        try:
            conn.close()
        except Exception:
            pass

    return jsonify({
        "message": "Student created successfully",
        "student_id": student_id
    }), 201


@app.route("/students", methods=["GET"])
def get_students():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()

    return jsonify([
        {
            "id": student["id"],
            "name": student["name"],
            "email": student["email"],
            "course": student["course"],
            "age": student["age"]
        }
        for student in students
    ]), 200


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    conn = get_db_connection()
    student = conn.execute(
        "SELECT * FROM students WHERE id = ?", (student_id,)
    ).fetchone()
    conn.close()

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(dict(student)), 200


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must contain JSON data"}), 400

    required_fields = ["name", "email", "course", "age"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    name = data["name"]
    email = data["email"]
    course = data["course"]
    age = data["age"]

    if not isinstance(age, int):
        return jsonify({"error": "Age must be an integer"}), 400
    if age <= 0:
        return jsonify({"error": "Age must be greater than 0"}), 400

    conn = get_db_connection()
    student = conn.execute(
        "SELECT * FROM students WHERE id = ?", (student_id,)
    ).fetchone()

    if student is None:
        conn.close()
        return jsonify({"error": "Student not found"}), 404

    try:
        conn.execute("""
            UPDATE students
            SET name = ?, email = ?, course = ?, age = ?
            WHERE id = ?
        """, (name, email, course, age, student_id))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error": "Email already exists"}), 400

    conn.close()
    return jsonify({"message": "Student updated successfully"}), 200


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    conn = get_db_connection()
    student = conn.execute(
        "SELECT * FROM students WHERE id = ?", (student_id,)
    ).fetchone()

    if student is None:
        conn.close()
        return jsonify({"error": "Student not found"}), 404

    conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Student deleted successfully"}), 200


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Route not found"}), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="127.0.0.1", port=5000)
