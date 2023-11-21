import Foundation

func solution(_ strArr:[String]) -> [String] {
    var idx: Int = 0
    var answer: [String] = []
    
    for c in strArr {
        if idx % 2 == 0 {
            answer.append(c.lowercased())
        } else {
            answer.append(c.uppercased())
        }
        idx += 1
    }
    
    return answer
}