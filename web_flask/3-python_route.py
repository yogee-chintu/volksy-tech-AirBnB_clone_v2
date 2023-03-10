#!/usr/bin/python3
"""
script to start Flash web application
listens on 0.0.0.0, port 5000
routes:
/: display "Hello HBNB!"
/hbnb: display "HBNB"
/c/<text>: display "C" followed by value of text variable
/python/(<text>): display "Python" followed by value of text
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

    @app.route('/python', strict_slashes=False)
    @app.route('/python/<path:text>', strict_slashes=False)
    def python(text=None):
        """
        displays "Python" followed by value of variable list text
        underscores in <text> replaced with spaces
        default if no text given is "is cool"
        """
        if text is None:
            text = "is cool"
        else:
            for i in range(len(text)):
                if text[i] == '_':
                    text = text[:i] + ' ' + text[i+1:]
        python_message = "Python " + text
        return python_message

    app.run(host='0.0.0.0', port='5000')
