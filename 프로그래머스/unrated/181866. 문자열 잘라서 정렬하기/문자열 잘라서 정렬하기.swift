import Foundation

func solution(_ myString:String) -> [String] {
    var arr: [String] = myString.components(separatedBy: "x")
    var answer: [String] = []
    arr = arr.sorted()
    
    for c in arr {
        if c != "" {
            answer.append(c)
        }
    }
    
    return answer
}