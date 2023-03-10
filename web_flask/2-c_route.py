#!/usr/bin/python3
"""
script to start Flash web application
listens on 0.0.0.0, port 5000
routes:
/: display "Hello HBNB!"
/hbnb: display "HBNB"
/c/<text>: display "C" followed by value of text variable
"""
if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_hbnb():
        """
        displays "Hello HBNB!"
        """
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """
        displays "HBNB"
        """
        return "HBNB"

    @app.route('/c/<path:text>', strict_slashes=False)
    def c(text):
        """
        displays "C" followed by value of variable list text
        underscores in <text> replaced with spaces
        """
        for i in range(len(text)):
            if text[i] == '_':
                text = text[:i] + ' ' + text[i+1:]
        c_message = "C " + text
        return c_message

    app.run(host='0.0.0.0', port='5000')
