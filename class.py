from unittest import result
import pandas as pd
import statistics
import csv

df=pd.read_csv('data.csv')
hlist=df['h'].to_list()
wlist=df['h'].to_list()
hmean=statistics.mean(hlist)
wmean=statistics.mean(wlist)
hmedian=statistics.median(hlist)
wmedian=statistics.median(wlist)
hmode=statistics.mode(hlist)
wmode=statistics.mode(wlist)
hsd=statistics.stdev(hlist)
wsd=statistics.stdev(wlist)
h1sdstart,h1sdend=hmean-hsd,hmean+hsd
h2sdstart,h2sdend=hmean-(2*hsd),hmean+(2*hsd)
h3sdstart,h3sdend=hmean-(3*hsd),hmean+(3*hsd)
w1sdstart,w1sdend=wmean-wsd,wmean+wsd
w2sdstart,w2sdend=wmean-(2*wsd),wmean+(2*wsd)
w3sdstart,w3sdend=wmean-(3*wsd),wmean+(3*wsd)
hldw1stdev=[result for result in hlist if result>h1sdstart and result<h1sdend]
h2dw1stdev=[result for result in hlist if result>h2sdstart and result<h2sdend]
h3dw1stdev=[result for result in hlist if result>h3sdstart and result<h3sdend]
w1dw1stdev=[result for result in wlist if result>w1sdstart and result<w1sdend]
w2dw1stdev=[result for result in wlist if result>w2sdstart and result<w2sdend]
w3dw1stdev=[result for result in wlist if result>w3sdstart and result<w3sdend]
print("{}% of data for height lies within 1 standard deviations".format(len(hldw1stdev)*100.0/len(hlist)))
print("{}% of data for height lies within 2 standard deviations".format(len(h2dw1stdev)*100.0/len(hlist)))
print("{}% of data for height lies within 3 standard deviations".format(len(h3dw1stdev)*100.0/len(hlist)))
print("{}% of data for weight lies within 1 standard deviations".format(len(w1dw1stdev)*100.0/len(wlist)))
print("{}% of data for weight lies within 2 standard deviations".format(len(w2dw1stdev)*100.0/len(wlist)))
print("{}% of data for weight lies within 3 standard deviations".format(len(w3dw1stdev)*100.0/len(wlist)))