def gmail_email(receiver,subject,body):
    import smtplib
    conn = smtplib.SMTP('smtp.gmail.com',587)
    conn.ehlo()
    conn.starttls()
    
    conn.login('flyncloud@gmail.com','xiqjsyirpwnxmjct')
    # receiver = input('What is the email address that you want to receive the email on\n:')
    # subject = input('What is the subject you want your email\n:')
    # body = input('What is the body you want for the email to',receiver,'\n:')
    message = f"""Subject: {subject}\n
    {body}
    """
    conn.sendmail('flyncloud@gmail.com',receiver,message)
    conn.quit()

