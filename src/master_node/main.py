from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<html>
<head>
    <title>Indoor Comfort Dashboard</title>
</head>

<body>
<h1>Indoor Comfort Monitoring</h1>
</body>
</html>
"""

@app.route("/")
def dashboard_ui():
    return render_template_string(HTML)

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()