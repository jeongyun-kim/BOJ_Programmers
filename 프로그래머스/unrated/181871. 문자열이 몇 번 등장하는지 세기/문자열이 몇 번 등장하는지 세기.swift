import Foundation

func solution(_ myString:String, _ pat:String) -> Int {
    var str: String = ""
    let length: Int = pat.count
    var answer: Int = 0
    
    for c in myString {
        str += String(c)
        if str.count >= length {
            var idx = str.index(str.endIndex, offsetBy: -length)
            var pat2: String = String(str[idx...])
            if pat2 == pat {
                answer += 1
            }
        }
    }
    
    return answer
}