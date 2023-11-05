import Foundation

func solution(_ names:[String]) -> [String] {
    var cnt: Int = 0
    var answer: [String] = []
    
    for i in stride(from: 0, to: names.count, by: 5) {
        answer.append(names[i])
    }
    
    return answer
}