import Foundation

func solution(_ str1:String, _ str2:String) -> String {
    var answer = ""
    let start1 = str1.startIndex
    let start2 = str2.startIndex
    
    for i in 0..<str1.count {
        var s1 = String(str1[str1.index(start1, offsetBy: i)])
        var s2 = String(str2[str2.index(start2, offsetBy: i)])
        answer.append(s1)
        answer.append(s2)
    }
    
    return answer
}