# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 11:11:00 2022

@author: catcry
"""

import cx_Oracle
import time

def wrt2db(submitted):
    dsn_tns = cx_Oracle.makedsn('10.19.10.161', '1502', service_name='orcl.bonyansystem.com')
    conn = cx_Oracle.connect(user=r'ccrewrtdb', password='Bonyan123', dsn=dsn_tns)
    c = conn.cursor()
    sql = " INSERT INTO REWRT_RULES(ORIGINAL_URL,EXPOSED_URL,FLAG) \
        values(:original_url,:exposed_url, :flag) "
    
    #sql = "select * from REWRT_RULES"
    #for row in c.execute(sql):
     #   print(row)

    #sql = "select * from REWRT_RULES where rule_id = :rid"
    
    c.execute(sql,original_url=submitted['original_url'], \
                  exposed_url=submitted['exposed_url'],\
                  flag=submitted['flag'])
    conn.commit()
    c.close()
    conn.close()
    
    
# RULE_ID
# ORIGINAL_URL
# EXPOSED_URL
# FLAG
# SUB_DATE


def list_rules():
    dsn_tns = cx_Oracle.makedsn('10.19.10.161', '1502', service_name='orcl.bonyansystem.com')
    conn = cx_Oracle.connect(user=r'ccrewrtdb', password='Bonyan123', dsn=dsn_tns)
    c = conn.cursor()
    sql = "Select * from REWRT_RULES"
    
    no_rules_sql = "Select count(*) from REWRT_RULES"
    c.execute(no_rules_sql)
    no_rules = c.fetchall()
    
    c.execute(sql)
    results =c.fetchall()
    conn.close()
    return no_rules[0][0],results

