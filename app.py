#!/usr/bin/env python3

### IMPORTS ###
import os

from flask import Flask

### GLOBALS ###
COLOR_TABLE = {
    "red": "#CC0000",
    "blue": "#0000CC",
    "green": "#00CC00",
    "yellow": "#CCCC00",
    "purple": "#CC66CC",
    "grey": "#CCCCCC",
    "orange": "#FFCC99"
}

HTML_PAGE ="""<!DOCTYPE html>
<html>
<head>
<script type="text/javascript">
function setColor(data) {
    console.log(data);
    document.querySelector("#color_text").innerText = `Color: ${data.color}`;
    document.querySelector("#color_box").style.backgroundColor = data.color;
}
function getColor() {
    fetch('/api/color')
      .then(response => response.json())
      .then(data => setColor(data));
}
document.addEventListener("DOMContentLoaded", getColor);
</script>
</head>
<body style="min-height: 100%;">
  <h1>Test Color Page</h1>
  <h2 id="color_text">Color: #000000</h2>
  <div id="color_box" style="backgroundColor: #000000; height: 300px; width: 300px">
    <br />
  </div>
</body>
</html>
"""

app = Flask(__name__)

### FUNCTIONS ###
@app.before_first_request
def app_startup():
    tmp_color = os.getenv('COLOR', None)
    if tmp_color is None:
        raise RuntimeError("Color not set.  Please set environment variable 'COLOR' to a hex code or a named color.")
    if (len(tmp_color) == 7) and (tmp_color[0] == '#'):
        app.config['COLOR'] = tmp_color
    elif tmp_color.lower() in COLOR_TABLE:
        app.config['COLOR'] = COLOR_TABLE[tmp_color.lower()]
    else:
        raise RuntimeError("Invalid color set.  Please use one of {} or a six digit hex-code.".format(COLOR_TABLE))

@app.route("/api/color", methods=['GET'])
def get_color():
    return {"color": app.config['COLOR']}

@app.route("/", methods=['GET'])
def index():
    return HTML_PAGE

### CLASSES ###

### MAIN ###
if __name__ == "__main__":
    app.run()
