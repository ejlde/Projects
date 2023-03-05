# anomaly detection toolkit
# UNSUPERVISED !! 
# rule-based time series anomaly detection
# not ML

# Combination of detection algorithms (detectors)
# Feature Engineering Methods (transformers)
# Ensemble Methods (aggregators)

# All 3 above are required to build an
# effective anomaly detection model

# Pipe classes to connect them together into a model

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf 
from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import * # * = import everything

data = pd.read_csv("monthly_csv.csv")
data["Date"] = pd.to_datetime(data["Date"])
data = data.set_index("Date")
data = data["Mean"]
#print(data)

##
# Threshold Detection
# low and high - if below or above its an anomaly
# threshold_detector = ThresholdAD(low=-0.5,high=0.75)
# anomalies = threshold_detector.detect(data)
# plot(data,anomaly=anomalies,anomaly_color="red",anomaly_tag="marker")
# plt.show()


##
# Percentiles (Quantiles) Detection
# quantile_detector = QuantileAD(low=0.01,high=0.99)
# anomalies = quantile_detector.fit_detect(data) 
# #.fit_detect trains on data
# plot(data,anomaly=anomalies,anomaly_color="red",anomaly_tag="marker")
# plt.show()


##
# Intraquartile Range (IQR)
# iqr_detector = InterQuartileRangeAD(c=1.5) 
# # deviation from the mean - higher c = less anomalies
# anomalies = iqr_detector.fit_detect(data)
# plot(data,anomaly=anomalies,anomaly_color="red",anomaly_tag="marker")
# plt.show()


##
# ESD Generalized (assumes normal distribution)
# data = validate_series(data)
# # need to validate the data for this method
# esd_detector = GeneralizedESDTestAD(alpha=0.3)
# anomalies = esd_detector.fit_detect(data)
# plot(data,anomaly=anomalies,anomaly_color="red",anomaly_tag="marker")
# plt.show()

##
# TSLA Stock Data from y finance
data1 = yf.download("TSLA")['Close']
data1 = validate_series(data1)

##
# Persist Detector compares value to previous vals
# and detects changes that're anormal
# persist_detector = PersistAD(c=20.0,side="positive")
# persist_detector.window = 10  # how many days to look back
# anomalies = persist_detector.fit_detect(data1)
# plot(data1,anomaly=anomalies,anomaly_color="red",anomaly_tag="marker")
# plt.show()

##
# Volitality Shift Anomaly Detection

volitality_detector = VolatilityShiftAD(c=6.0,side='positive',window =30)
anomalies = volitality_detector.fit_detect(data1)
plot(data1,anomaly=anomalies,anomaly_color="red")
plt.show()
