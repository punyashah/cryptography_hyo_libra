from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('caesar_encryption.html')

@app.route('/',methods=['POST'])
def my_form_post():
    output_str = ""
    text = request.form['message']
    shift = int(request.form['shift'])
    for char in text:
        if(char.isupper()):
            shifted_final = ord(char) + (shift%26)
            if(shifted_final > 90):
                shifted_final -= 26
            output_str += chr(shifted_final)
        elif(char.islower()):
            shifted_final = ord(char) + (shift%26)
            if(shifted_final > 122):
                shifted_final -= 26
            output_str += chr(shifted_final)
        else:
            output_str += char

    return output_str

if __name__ == '__main__':
    app.run(debug=True)
