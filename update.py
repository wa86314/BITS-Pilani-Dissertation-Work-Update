from flask import Flask, request

from connection import db_conn

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "INFO: This Microservice is use for updating record to the Database"

@app.route('/update', methods=['PUT'])
def update():
    
    # Updating student name by ID
    data = request.get_json()
    stud_id = data.get('id')
    latest_stud_name = data.get('name')

    db_cursor = db_conn.cursor()
    query = "UPDATE student SET name = %s WHERE id = %s"
    values = (latest_stud_name, stud_id)
    db_cursor.execute(query, values)
    db_conn.commit()

    #If the target ID won't present in the student table
    if db_cursor.rowcount == 0:
       return f"ID {stud_id} not found"

    return f"Record Update for {stud_id} successfully!"

if __name__ == '__main__':
    app.run(debug=True, port=9002, host='0.0.0.0')

db_conn.close()
