import argparse
import logging
import logging.handlers
import os
import os.path
import sys
from configparser import ConfigParser

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

config = ConfigParser()

try:
    with open('settings.conf', 'r') as fp:
        config.readfp(fp)
except IOError:
    print("Unable to read settings.conf, file may be missing.")
    sys.exit(1)
except:
    print("Error in settings.conf:", sys.exc_info()[0])
    sys.exit(1)

log = logging.getLogger('Wireless Host')
log.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.getLevelName(
    config.get('logging', 'consoleLevel')))
consoleFormatter = logging.Formatter(
    '%(asctime)s - %(name)s %(levelname)s: %(message)s', '%H:%M:%S')
consoleHandler.setFormatter(consoleFormatter)
try:
    fileHandler = logging.handlers.RotatingFileHandler(config.get('logging', 'file'),
        maxBytes=config.getint('logging', 'maxSize'),
        backupCount=config.getint('logging', 'numBackup'))
except IOError:
    print("Error: unable to write to log files. Check permissions are correct.")
    sys.exit(1)

fileHandler.setLevel(logging.getLevelName(
    config.get('logging', 'fileLevel')))
fileFormatter = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
fileHandler.setFormatter(fileFormatter)
log.addHandler(consoleHandler)
log.addHandler(fileHandler)

app = Flask(__name__)

serverPort = config.getint('server', 'port')
serverDebug = config.getboolean('server', 'debug')
networkInterface = config.get('network', 'interface')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html'), 200


@app.route('/submit', methods=['POST'])
def submit():

    ssid = request.form['ssid']
    psk = request.form['psk']
    log.debug("SSID: {}\tPSK: {}".format(ssid, psk))
    return "got", 200


if __name__ == "__main__":
    log.critical('Starting network module')
    app.run(debug=serverDebug, host="0.0.0.0", port=serverPort)
