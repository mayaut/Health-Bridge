from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/my-handling-form-page', methods=['GET'])
def handle_form_submission():
    nameValue = request.args.get("user_name")
    heightValue = request.args.get('user_height')
    weightValue = request.args.get('user_weight')
    medValue = request.args.get('user_medication')
    allergiesValue = request.args.get('user_allergies')
    hospitalValue = request.args.get('user_hospital')
    msgsValue = request.args.get('user_message')
    genderValue = request.args.get('user_gender')
   
    with open(f"{nameValue}.txt", "w") as f:
        f.write(f"Name: {nameValue}\n")
        f.write(f"Gender: {genderValue}\n")
        f.write(f"Height: {heightValue}\n")
        f.write(f"Weight: {weightValue}\n")
        f.write(f"Medications: {medValue}\n")
        f.write(f"Allergies: {allergiesValue}\n")
        f.write(f"Hospital Preferences: {hospitalValue}\n")
        f.write(f"Additional Messages: {msgsValue}\n")

    return jsonify({'success': True, 'message': 'Data saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)
