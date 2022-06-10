# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 03:10:52 2022

@author: catcry
"""
from dbMan import list_rules
import re

def ng_conf_gen():

    rules_ls_len,rules_ls = list_rules()
    
    try:
        #file = open ("/data/users/appuser/wso2urls.conf",'r')
        file = open ("wso2rules.conf", 'r')
        source_file_content = file.read()
        rule_content = re.search(r"#cc_start((.|\n)*)#cc_end",source_file_content)    
        
    except:
        return "Source file openning error!"
	
    if rule_content:
	
        location_string = ""
        
        for i in range(rules_ls_len):
            location_string = location_string +\
            "\n\n" +\
            "\t" + "location = " + rules_ls[i][2] + "\n" +\
            "\t{\n" +\
            "\t\t" + "rewrite ^" + rules_ls[i][1] + "?$" + " " +rules_ls[i][2] + " " + rules_ls[i][3] + ";\n" +\
            "\t}"

        # final_string = "limit_req_zone $binary_remote_addr zone=ccrules:500m rate=100r/s;\n\n" +\
        # "server {\n\n" + \
        # "#cc_start\n" +\
        # rule_content.group(1) +"\n\n" +\
        # "\tlocation = " +  submitted['exposed_url'] + "\n" +\
        # "\t{\n" +\
        # "\t\t" + "rewrite ^" + submitted['exposed_url'] + "?$" + " " +submitted["original_url"] + " " + submitted["flag"] + ";\n" +\
        # "\t}" + "\n\n" +\
        # "#cc_end\n"+\
        # "}"
        
        final_string = "limit_req_zone $binary_remote_addr zone=ccrules:500m rate=100r/s;\n\n" +\
            "server {\n\n" + \
            "#cc_start\n" +\
            rule_content.group(1) +"\n\n" +\
            "\n#cc_end\n\n" + \
            "#ccRewriteRules_start" +\
            location_string +\
            "\n#ccRewriteRules_end" +\
            "\n}"
            
        
        try:
            des_file = open("wso2tst.txt",'w')
            des_file.write(final_string)
            des_file.close()
            file.close()
            return ("Everything went right. Rules has been updated successfully!")
        except:
            return "Destination file openning error!"
            file.close()
    else:
        return "No regex match in source file. Wrong file or wrong file structure." 
        file.close()
        des_file.close()
                   