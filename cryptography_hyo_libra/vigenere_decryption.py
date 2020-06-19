from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('vigenere_decryption.html')

@app.route('/',methods=['POST'])
def my_form_post():
    output_str = ""
    text = request.form['message']
    key = request.form['key']
    for i in range(len(text)):
        x = (ord(text[i]) - ord(key[i]) + 26)%26
        x += ord('A')
        output_str += chr(x)
    return output_str

if __name__ == '__main__':
    app.run(debug=True)
