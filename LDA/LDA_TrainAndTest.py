#!/usr/bin/python
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

# MIMIC-III Connection Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
# ----------------------------

# Setup some Global Variables
VERBOSE = True


#STEP 1 :: Preparing the connection to the dataset...

# Set the database connection information
sqluser = 'postgres'
dbname = 'mimic'
schema_name = 'mimiciii'

# Connect to postgres with a copy of the MIMIC-III database
con = psycopg2.connect(dbname=dbname, user=sqluser)

# the below statement is prepended to queries to ensure they select from the right schema
query_schema = 'set search_path to ' + schema_name + ';'

if VERBOSE: print "Setup Complete!"

# STEP 2 & 3  :: Creating the Tokenizer and Porter Stemmer

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')
if VERBOSE: print en_stop

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()


# Step 4 :: Grabbing the data!

# Pull all clinical notes from the MIMIC-II dataset treating each one as a document
query = query_schema + """
SELECT subject_id, text
FROM noteevents
LIMIT 1000
"""
df = pd.read_sql_query(query, con)
df.head()

# Print and example to validate
#print df[0:1].text.values[0]
print df.at[0, 'text']





