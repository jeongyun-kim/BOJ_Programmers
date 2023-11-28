import Foundation

func solution(_ my_string:String) -> [String] {
    var arr: [String] = my_string.components(separatedBy: " ")
    var answer: [String] = []
    
    for c in arr {
        if c != "" {
            answer.append(String(c))
        }
    }
    
    return answer
}