import collections 
def solution(participant, completion):
    answer = ''
    participants = collections.Counter(participant)
    completion = collections.Counter(completion)
    
    for key, value in participants.items() :
        if key not in completion or value > completion[key] :
            answer = key
            break
            
    return answer
    
    
