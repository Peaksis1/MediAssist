from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)

# Setup Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # SMTP server
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'mediassist940@gmail.com'
app.config['MAIL_PASSWORD'] = 'tjwv sibf jmvo enxd'
app.config['MAIL_DEFAULT_SENDER'] = 'mediassist940@gmail.com'

mail = Mail(app)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    
    # Extract form data
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        # Create the email message
        msg = Message(
            subject="New Contact Form Submission",
            recipients=["mediassist940@gmail.com"],  # Email of the team
            body=f"Message from: {name}\nEmail: {email}\n\n{message}",
        )
        
        # Send the email
        mail.send(msg)
        return jsonify({"message": "Email sent successfully!"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to send email."}), 500

if __name__ == '__main__':
    app.run(debug=True)
