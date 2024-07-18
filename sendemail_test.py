import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email content
sender_email = "bryancasabuenac@gmail.com"
receiver_email = "bryancasabuenac@gmail.com"
subject = "Test Email"
body = "New event was found"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body to email
message.attach(MIMEText(body, "plain"))

# SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Port for TLS encryption

try:
    # Establish a secure session with the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, "gwxrsugftjspckyo")  # Replace with your email password

    # Send email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email. Error: {e}")

finally:
    try:
        server.quit()  # Close the SMTP server connection
    except NameError:
        pass  # Handle the case where `server` was never defined due to an exception
