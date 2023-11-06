import Foundation

func solution(_ myString:String, _ pat:String) -> Int {
    var answer: Int = 0
    let m: String = myString.lowercased()
    let p: String = pat.lowercased()
    
    if m.contains(p) {
        answer = 1
    }
    
    return answer
}