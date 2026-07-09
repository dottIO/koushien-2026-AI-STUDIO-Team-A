"""Flask TODO application."""

from flask import Flask, render_template, request, redirect, url_for
from todo import add_todo


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config["todos"] = []

    @app.route("/")
    def index():
        """Display the TODO list."""
        return render_template("index.html", todos=app.config["todos"])

    @app.route("/add", methods=["POST"])
    def add():
        """Add a new TODO item."""
        title = request.form.get("title", "").strip()
        if title:
            app.config["todos"] = add_todo(app.config["todos"], title)
        return redirect(url_for("index"))

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
