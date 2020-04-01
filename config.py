# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:28:25 2020

@author: FreeA7
"""

PROGRAM_NAME = 'Process_Prospectus'


SENTIMENT_WORDS_DIR = './sentiment_words/'
SENTIMENT_BAN_LIST = ['Constraining']
SENTIMENT_LIST = ['Positive', 'Litigious', 'StrongModal', 'Negative', 'Uncertainty', 'WeakModal']
SENTIMENT_POSITIVE_LIST = ['Positive', 'Litigious', 'StrongModal']
SENTIMENT_NEGATIVE_LIST = ['Negative', 'Uncertainty', 'WeakModal']


PARAGRAPH_CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


URL_LIST = ['https://www.sec.gov/Archives/edgar/data/1060426/000106042607000002/chaoxsb2amend.htm',
            'https://www.sec.gov/Archives/edgar/data/1090514/000101968705001085/aobo_sb2-041405.txt',
            'https://www.sec.gov/Archives/edgar/data/1709505/000104746917004222/a2232277zf-1.htm',
            'https://www.sec.gov/Archives/edgar/data/1281696/000089322005000075/w04091sv1.htm',
            'https://www.sec.gov/Archives/edgar/data/1117057/000114420407041326/v083020_s1.htm']