import Foundation

func solution(_ l:Int, _ r:Int) -> [Int] {
    var answer: [Int] = []
    var flag: Bool
    
    for i in l...r {
        flag = true
        for c in "12346789" {
            if String(i).contains(c) == true {
                flag = false
                break
            }
        }
        if flag == true {
            answer.append(i)
        }
    }
    if answer.count == 0 {
        answer = [-1]
    }
    
    return answer
}

