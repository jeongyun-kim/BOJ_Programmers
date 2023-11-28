import Foundation

func solution(_ strArr:[String]) -> [String] {
    var answer: [String] = []
    
    for str in strArr {
        if str.contains("ad") {
            continue
        } else {
            answer.append(str)
        }
    }
    
    return answer
}