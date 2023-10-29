import Foundation

func solution(_ my_string:String, _ indices:[Int]) -> String {
    var idx: Int = 0
    var answer: String = ""
    
    for s in my_string {
        if indices.contains(idx) == false {
            answer += String(s)
        }
        idx += 1
    }
    
    return answer
}