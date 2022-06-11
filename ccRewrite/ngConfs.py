# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 03:10:52 2022

@author: catcry
"""
from dbMan import list_rules
import re
import os
from datetime import datetime

def ng_conf_gen():

    rules_ls_len,rules_ls = list_rules()
    ## file addresses in edge2:
        # 
        
    #########################################################    
    # copy current url config file to backup directory      #
    #########################################################
    try:
        now = datetime.now()
        date_time = now.strftime("%Y%m%d_%H%M%S")
        cp_string = "cp /etc/opt/rh/rh-nginx18/nginx/conf.d/wso2urls.conf /data/users/appuser/apps/wso2confs_backup/wso2urls.conf_" + date_time
        # os.system(cp_string)
    except:
        return "Current URL Rewrite Conf File Copy Error!"
    
    #########################################################    
    # Open Current URL Config File and Construct New File   #
    #########################################################
    try:
        # file = open ("/data/users/appuser/wso2urls.conf",'r')
        # file = open ("/etc/opt/rh/rh-nginx18/nginx/conf.d/wso2urls.conf" , 'r')
        
        file = open ("wso2rules.conf", 'r')
        source_file_content = file.read()
        rule_content = re.search(r"#cc_start((.|\n)*)#cc_end",source_file_content) 
        file.close()
        
    except:
        return "NGINX Configuration file openning error!"
	
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
            des_file = open("wso2tst1.txt",'w')
            des_file.write(final_string)
            des_file.close()
            return ("Rewrite Rules Set has been updated \n NGINX reloaded successfully")
            # try:
                
            #     os.system("systemctl reload rh-nginx18-nginx")
            #     os.system("systemctl restart rh-nginx18-nginx")
            #     return ("Rewrite Rules Set has been updated \n NGINX reloaded successfully")
            # except:
            #     return "NGINX RESTART FAILED!"
            
        except:
            return "Destination file openning error!"

    else:
        return "No regex match in source file. Wrong file or wrong file structure." 
        
        
                   