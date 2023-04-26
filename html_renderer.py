from flask import Flask, request, render_template
from finalapp import final



app =Flask(__name__, template_folder= 'templates')

@app.route('/keyword_search', methods=['GET', 'POST'])

def keyword_search():
    if request.method=="POST":
        words = request.form['words']
        print('words:',words)
        result=final(words)
        print('result:',result)
        return render_template('data.html',result=result)
    else:
        return render_template('data.html')


if __name__ =='__main__':
    app.run(debug=True)


