import Foundation

func solution(_ myString:String) -> String {
    var answer: String = ""
    
    for c in myString {
        answer += String(c.uppercased())
    }
    
    return answer
}