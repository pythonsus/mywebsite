

from forms import audiobutton, binary_to_text, contactform, text_to_binaryForm, transform
from googletrans import Translator, constants
from pprint import pprint
from flask import Flask, request, render_template
from email_function import gmail_email

application = Flask(__name__)
application.config['SECRET_KEY'] = 'iuhguivfduivdifvjdfhv'

@application.route('/binarytotext', methods=['GET','POST'])
def decode_binary_string():
    form = binary_to_text()
    if form.is_submitted():
        result = request.form
        res = ''.join(chr(int(result['binary'][i*8:i*8+8],2)) for i in range(len(result['binary'])//8))
        return render_template('rt.html',res=res)
    return render_template('t.html',form=form)
@application.route('/texttobinary', methods=['GET','POST'])
def ttb():
    form = text_to_binaryForm()
    if form.is_submitted():
        result = request.form
        b = ''.join(format(ord(i), '08b') for i in result['text'])
      
        return render_template('rb.html',binary=b)
    return render_template('b.html',form=form)
@application.route('/', methods=['GET','POST'])
def translater_func():
    form = transform()
 
    if form.is_submitted():
        result = request.form
        print(result)
        try:
            t = result['translangto'].lower() or 'en'
       
            s=result['source'] or 'en'
            translator = Translator()
            translation = translator.translate(result['tasktotrans'], dest=t.strip(),src=s)
          

        
        except:
            t = result['translangto'].lower() or 'en'
           
            translator = Translator()
            translation = translator.translate(result['tasktotrans'], dest=t.strip())     
    
            
        return render_template('result.html',re=translation.text,pro=translation.pronunciation)
    return render_template('index.html',form=form)
@application.route('/feedback', methods=['GET','POST'])
def feedback_func():
    form = contactform()

    if form.is_submitted():
        result = request.form
        
        # with open('database.txt', mode='a') as database:
        #     email = result['email']
        #     name = result['name']
        #     body = result['body']
        #     file = database.write(f'\n{email},{name},{body} ')
       
        gmail_email('thayyilsuhaan@gmail.com',f"feedback from translater from: {result['name']},{result['email']},",result['body'])
    
        return render_template('rf.html')
    return render_template('feedback.html',form=form)
@application.route('/logs')
def logs_func():
    return render_template('logs.html')
@application.route('/ca')
def Ca_func():
    return render_template('ca.html')
@application.route('/about')
def Aboutpage():
    return render_template('about.html')
@application.route('/pp')
def pp_page():
    return render_template('pp.html')
@application.route('/robots.txt')
def r():
    return render_template('robots.html')
if __name__ == '__main__':
    application.run(debug=True)
