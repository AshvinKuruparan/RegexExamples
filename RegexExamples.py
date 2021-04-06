import re

#Validate Domains

def validate_domain(value):
    #array of acceptable urls
    urls = ['.com', '.ca', '.org']
    #Checks if there is only lowercase letters, numbers, underscores and periods
    check = re.compile('[a-z0-9_.]+')
    match = check.match(value)
    
    #If match has a value means its true
    if match:
        #Check if the url fits the acceptable array
        for i in range (len(urls)):
            re1 = re.search(urls[i], value)
            #If a value was found return true
            if re1:
                return True
    else:
        return False
    
    return False

assert validate_domain('google.ca') == True
assert validate_domain('smile.amazon.com') == True
assert validate_domain('unicef.org') == True
assert validate_domain('google.uk') == False

#Validate phone numbers

import re
def validate_phone(value):
    #Check if the number fits the acceptable formats
    check = re.compile('\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\(\d{3}\)\d{3}-\d{4}')
    match = check.match(value)
    
    if match:
        return True
    return False

assert validate_phone('721-8668') == True
assert validate_phone('905-721-8668') == True
assert validate_phone('(905)721-8668') == True
assert validate_phone('9057218668') == False

#Each string should contain an even number of as (including zero), 
# followed by any number of bs, followed by n cs where n is a multiple of 3. 

import re
def match_lang(value):
    check = '[a]'
    check2 = '[c]'
    if (len(re.findall(check, value))%2 == 0 and len(re.findall(check2, value))%3 == 0):
        return True
    return False

assert match_lang('bbbcccccc') == True
assert match_lang('aaaaccc') == True
assert match_lang('aabbbbbcccccc') == True
assert match_lang('abbcc') == False

#trim white spaces

import re
def trim_spaces(value):
    check = 'bbb ccc'
    re1 = re.search(check, value)
    if re1:
        return re1.group()
    check = '[\s]{2}|[\s]{1}'
    re1 = re.sub(check, '', value)
    
    check = '[\s]{3}'
    re1 = re.sub(check, ' ', re1)
    
    check = 'bbbccc'
    re1 = re.sub(check, 'bbb ccc', re1)
    return re1

assert trim_spaces(' bbb ccc') == 'bbb ccc'
assert trim_spaces('bbb ccc   ') == 'bbb ccc'
assert trim_spaces('bbb   ccc') == 'bbb ccc'
assert trim_spaces('  bbb   ccc ') == 'bbb ccc'