import Foundation

func solution(_ numLog:[Int]) -> String {
    var length: Int = numLog.count
    var answer: String = ""
    var dic: [Int: String] = [1: "w", -1: "s", 10: "d", -10: "a"]
    
    for i in 1..<length {
        var num: Int = numLog[i] - numLog[i-1]
        answer += dic[num]!
    }
    
    return answer
}