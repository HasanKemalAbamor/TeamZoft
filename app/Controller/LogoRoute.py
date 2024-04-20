from flask import Flask, send_file
import sqlite3
import io

app = Flask(__name__)

@app.route('/logo')
def logo():
    # Connect to the SQLite database
    conn = sqlite3.connect('Connect')
    cursor = conn.cursor()

    # Get the logo image data
    cursor.execute("SELECT image_data FROM images WHERE id = ?", (1,))  # assuming id 1 is the logo
    image_data = cursor.fetchone()[0]
    conn.close()

    # Return the image as a response
    return send_file(io.BytesIO(image_data), mimetype='image/png')


