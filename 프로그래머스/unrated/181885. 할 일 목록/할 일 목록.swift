import Foundation

func solution(_ todo_list:[String], _ finished:[Bool]) -> [String] {
    var answer: [String] = []
    
    for i in 0..<todo_list.count {
        if finished[i] == false {
            answer.append(todo_list[i])
        }
    }
    
    return answer
}