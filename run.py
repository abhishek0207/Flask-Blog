from flaskblog import create_app

app = create_app()  # could pass a configuration but by default it uses default
if __name__ == "__main__":
    app.run(debug=True)


