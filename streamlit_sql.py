# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:54:33 2024

@author: User
"""

import pandas as pd
import pyodbc
import streamlit as st

# database variables
# sql_server  = 'DESKTOP-86RO9TM'
# database    = 'AA_database'
# username    = 'sa'
# password    = '96328521'
# driver      = '{ODBC Driver 18 for SQL Server}'
conn = pyodbc.connect("DRIVER={SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"])
cursor = conn.cursor()
tech_text = pd.read_sql(sql="EXEC shopline_order_source" , con=conn)
conn.commit()

st.write(tech_text)