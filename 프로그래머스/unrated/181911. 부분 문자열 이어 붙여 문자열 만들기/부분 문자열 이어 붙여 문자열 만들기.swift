import Foundation
// parts[i] = [s, e]
// my_strings[i][s:e+1] 이어붙인 문자열 Return
func solution(_ my_strings:[String], _ parts:[[Int]]) -> String {
    var answer: String = ""
    let length: Int = my_strings.count
    
    for i in 0..<length {
        var str: String = my_strings[i]
        var s: Int = parts[i][0]
        var e: Int = parts[i][1]+1
        var start = str.index(str.startIndex, offsetBy: s)
        var end = str.index(str.startIndex, offsetBy: e)
        answer += str.substring(with: start..<end)
    }
    
    return answer
}