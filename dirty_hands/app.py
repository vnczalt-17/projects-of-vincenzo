from flask import Flask, render_template, request

app = Flask(__name__)

def converter(millis):
    
    if millis < 1000:
        print (f"just {millis} milisecond/s") 
    
    else:

        seconds=(millis/1000)%60

        seconds = (int(seconds))

        minutes=(millis/(1000*60))%60

        minutes = (int(minutes))

        hours= (millis/(1000*60*60))%24
        
        hours = (int(hours))

    return (f"{hours} hour/s, {minutes} minute/s, {seconds} second/s")

@app.route('/', methods=['GET'])
def main_get():
    return render_template('index.html', developer_name='GROUP CLOUDERS', not_valid=False)


@app.route('/', methods=['POST'])
def main_post():

    alpha=request.form['number']
    if not alpha.isdecimal():
        return render_template('index.html', developer_name='GROUP CLOUDERS', not_valid=True)
    
    number=int(alpha)
    if number <= 0:
        return render_template('index.html', developer_name='GROUP CLOUDERS', not_valid=True)
    
    return render_template('result.html', developer_name='GROUP CLOUDERS', milliseconds=number, result=converter(number))

if __name__ == '__main__':
    app.run(debug=True)