from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('second.html')

@app.route('/my-handling-form-page', methods=['GET'])
def handle_form_submission():
    nameValue = request.args.get("user_name_again")
    print(nameValue)
    filename = f"{nameValue}.txt"
    with open(filename, 'r') as file:
        file_contents = file.read()
        print(file_contents)
    return render_template('display_text.html', text_content=file_contents)
        
if __name__ == '__main__':
    app.run(debug=True)
