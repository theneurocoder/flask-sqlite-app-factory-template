from flask import render_template, request, redirect, url_for, flash
from app.db import get_connection


def register_routes(app):
    @app.route("/")
    def index():
        # Fetch all notes for display
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT title, content FROM notes ORDER BY id DESC")
        notes = cur.fetchall()
        conn.close()

        return render_template("index.html", notes=notes)

    @app.route("/notes", methods=["POST"])
    def create_note():
        # Read and normalize form input
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        # Form validation
        if not title or not content:
            flash("Title and content are required.")
            return redirect(url_for("index"))

        # Insert new note
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO notes (title, content) VALUES (?, ?)",
            (title, content)
        )
        conn.commit()
        conn.close()

        flash("Note created successfully.")
        return redirect(url_for("index"))
