from neuralintents import GenericAssistant
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import mplfinance as mpf

import pickle
import sys
import datetime as dt

# Basic Structure of Generic Assistant
"""
def myfunction():
    pass


mappings = {
    'greetings': myfunction()
}

assistant = GenericAssistant('intents.json',intent_methods = mappings)

assistant.train_model()

assistant.request("Hello")
"""

portfolio  = {'TSLA':12 , 'AAPL':3, 'GS':10}

with open('portfolio.pkl)
