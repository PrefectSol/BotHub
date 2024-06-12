from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__)

@app.route('/dir/', defaults={'req_path': ''})
@app.route('/dir/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = 'dir'

    abs_path = os.path.join(BASE_DIR, req_path)

    if not os.path.exists(abs_path):
        return "Not Found", 404

    if os.path.isfile(abs_path):
        return send_file(abs_path)

    files_and_dirs = os.listdir(abs_path)
    files_and_dirs = [os.path.join(req_path, fad) for fad in files_and_dirs]
    return render_template_string("""
    <ul>
        {% for item in items %}
        <li><a href="{{ item }}">{{ item }}</a></li>
        {% endfor %}
    </ul>
    """, items=files_and_dirs)

if __name__ == "__main__":
    app.run(debug=True)
