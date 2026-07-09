"""FlaskによるTODOアプリ本体"""

from flask import Flask, render_template, request, redirect, url_for
from todo import add_todo


def create_app():
    """Flaskアプリを生成するファクトリ関数"""
    app = Flask(__name__)

    # TODOリスト（メモリ上で管理）
    app.config["TODOS"] = []

    @app.route("/")
    def index():
        """TODO一覧を表示する"""
        todos = app.config["TODOS"]
        return render_template("index.html", todos=todos)

    @app.route("/add", methods=["POST"])
    def add():
        """フォームから送信されたTODOを追加する"""
        title = request.form.get("title", "")
        add_todo(app.config["TODOS"], title)
        return redirect(url_for("index"))

    return app


# Flaskが直接実行された場合
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5001, debug=True)
