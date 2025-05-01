from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=8000)

# IF YOU ARE MISSING DEPENDENCIES, RUN THIS:
# pip install -r requirements.txt
