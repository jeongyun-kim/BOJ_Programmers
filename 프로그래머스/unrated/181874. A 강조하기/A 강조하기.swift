import Foundation

func solution(_ myString:String) -> String {
    var answer: String = ""
    
    for c in myString {
        if c == "a" || c == "A" {
            answer += "A"
        } else {
            answer += String(c.lowercased())
        }
    }
    
    return answer
}