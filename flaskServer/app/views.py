__author__ = 'Kevans05'
from flask import render_template, flash, redirect
from forms import creatAlarm, creatPresets, setSetting
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title = 'home')

@app.route('/setAlarm', methods = ['GET', 'POST'])
def setAlarm():
    form = creatAlarm()
    return render_template('setAlarm.html',title = 'Set Alarm',form = form)

@app.route('/presets')
def presets():
    form = creatPresets()
    return render_template("setPreset.html", title = 'Set Presets', form = form)

@app.route('/viewAlarms')
def viewAlarms():
    return render_template("viewAlarm.html", title = 'View Alarms')

@app.route('/settings')
def settings():
    form = setSetting()
    return render_template("settings.html", title = 'Settings',form = form)