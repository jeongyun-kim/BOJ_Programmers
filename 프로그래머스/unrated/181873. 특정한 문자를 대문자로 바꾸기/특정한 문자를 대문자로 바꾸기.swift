import Foundation

func solution(_ my_string:String, _ alp:String) -> String {
    var answer: String = ""
    
    for c in my_string {
        if String(c) == alp {
            answer += String(c.uppercased())
        } else {
            answer += String(c)
        }
    }
    
    return answer
}