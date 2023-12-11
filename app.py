from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('website.html', services={
        'netflix': 'netflix.png',
        'hbomax': 'hbomax.png',
        'disneyplus': 'disneyplus.png',
        'youtube': 'youtube.png',
        'crunchyroll': 'crunchyroll.png',
        'viaplay': 'viaplay.png'

    })

@app.route('/<service>')
def redirect_to_service(service):
    services = {
        'netflix': 'https://www.netflix.com/browse',
        'hbomax': 'https://www.hbomax.com/',
        'disneyplus': 'https://www.disneyplus.com/no-no/home',
        'youtube': 'https://www.youtube.com/',
        'crunchyroll': 'https://www.crunchyroll.com/',
        'viaplay': 'https://www.viaplay.com/'
    }
    return redirect(services.get(service, '/'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")