# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 03:10:52 2022

@author: catcry
"""
import re

def ng_conf_gen(submitted):

    try:
        file = open ("/data/users/appuser/wso2urls.conf",'r')
        source_file_content = file.read()
        rule_content = re.search(r"\n#cc_start((.|\n)*)\n#cc_end",source_file_content)    
        
    except:
        return "Source file openning error!"
	
    if rule_content:
	
        final_string = "limit_req_zone $binary_remote_addr zone=ccrules:500m rate=100r/s;\n\n" +\
        "server {\n\n" + \
        "#cc_start\n" +\
        rule_content.group(1) +"\n\n" +\
        "\t\tlocaion = " +  submitted['exposed_url'] + "\n" +\
        "\t\t{\n" +\
        "\t\t\t" + "rewrite ^" + submitted['exposed_url'] + "?$" + " " +submitted["original_url"] + " " + submitted["flag"] + ";\n" +\
        "\t\t}" + "\n\n" +\
        "#cc_end"
        "}"
        try:
            des_file = open("amirtest.txt",'w')
            des_file.write(final_string)
            des_file.close()
            file.close()
            return ("Everything went right. Rules has been updated successfully!")
        except:
            return "Destination file openning error!"
            file.close()
    else:
        return "No regex match in source file. Wrong file or wrong file sructure." 
        file.close()
        des_file.close()
                   