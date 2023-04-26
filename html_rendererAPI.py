from flask import Flask, request, render_template, abort
from finalapp import final
app = Flask(__name__, template_folder='templates')
API_KEY = '63bf1bb6967221fdecbcf27c712ff6d4'

@app.route('/keyword_search', methods=['GET', 'POST'])
def keyword_search():
    if request.method == "POST":
        api_key = request.headers.get('api-key')
        print('api-key:',request.headers.get('api-key'))
        if api_key != API_KEY:
            # abort(401, 'Unauthorized')

            words = request.form['words']
            print('words:', words)
            result = final(words)
            print('result:', result)
            return render_template('data.html', result=result)
    else:
        return render_template('index.html')
 
if __name__ == '__main__':
    app.run(debug=True)
