def solution(skill, skill_trees):
    answer = 0
    skill2 = [skill[:i+1] for i in range(0, len(skill))]

    for i in range(0, len(skill_trees)) :
        skill_tree = ""
        for s in skill_trees[i] :
            if s in skill :
                skill_tree += s
        if skill_tree in skill2 or skill_tree == "" :
            answer += 1
            
    return answer