import re


def replaceAllNumbers(replaceWork,string):
    pattern = r'\d+'
    
    # Use re.sub() to replace all occurrences of the pattern with "Home work"
    return re.sub(pattern, lambda match: " "+str(replaceWork)+" "+match.group() + " ", string)
    
