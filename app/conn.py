from IPython.display import display
import sqlite3
from PIL import Image
import io

# Connect to the SQLite database
connection = sqlite3.connect('Connection')
cursor = connection.cursor()

# Retrieve the first image data from the images table
cursor.execute("SELECT image_data FROM images LIMIT 1")
image_data = cursor.fetchone()[0]
connection.close()

# Use Pillow to open the image from binary data
image = Image.open(io.BytesIO(image_data))

# Display the image
display(image)
