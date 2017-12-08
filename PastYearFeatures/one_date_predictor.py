import pandas as p
import numpy as np
from sklearn.externals import joblib
from urllib.request import urlretrieve
import os
import sys
import requests
import gzip
from datetime import datetime, timedelta

class OneDatePredictor:
    def __init__(self, date):
        self.date = date
        self.end_date = date - timedelta(days=1)
        self.start_date = date - timedelta(days=366)

    def download_csv(self):
        start_date = self.start_date.strftime('%d.%m.%Y')
        end_date = self.end_date.strftime('%d.%m.%Y')
        data = self.produce_data_string( 15614, start_date, end_date, 1, 1, 1, 1, 2, 1)
        headers = {
            'Host' : 'rp5.ru',
            'Accept' : 'text/html, */*; q=0.01',
            'Accept-Language' : 'en-US,en;q=0.5',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Referer' : 'https://rp5.ru/',
            'Content-Type' : 'application/x-www-form-urlencoded'
        }

        rp5_url = "https://rp5.ru/responses/reFileSynop.php"
        r = requests.post(rp5_url, data = data, headers = headers)

        url = self.extract_url_from_response(r)
        urlretrieve(url, "data.gz")

    def produce_data_string(self, id, start_date, end_date, f1, f2, f3, p1, p2, ln):
        data = """wmo_id=%s&a_date1=%s&a_date2=%s&
            f_ed3=%s&f_ed4=%s&f_ed5=%s&f_pe=%s&f_pe1=%s&lng_id=%s""" % (id,
             start_date, end_date, f1, f2, f3, p1, p2, ln)
        return data

    def extract_url_from_response(self, response):
        url = response.content.decode("utf-8")
        url = url.split('href=',1)[1].split('>D',1)[0].replace('../', '')
        return url

    def extract_file(self, name):
        arch = gzip.open(name, 'rb').read()
        save = open(name, 'w')
        save.write(arch.decode('utf-8'))
        save.close()

    def remove_rp5_metadata(self, file_path):
        with open(file_path, 'r') as ifile:
            line_list = ifile.readlines()
        with open(file_path, 'w') as ofile:
            ofile.writelines(line_list[6:])
