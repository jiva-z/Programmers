def solution(s):
    answer = ''
    dict = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    
    for j in range(len(dict)):
        if dict[j] in s:
            s = s.replace(dict[j],str(j))
            
    return int(s)