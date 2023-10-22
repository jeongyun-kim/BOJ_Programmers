import Foundation

func solution(_ n:Int, _ control:String) -> Int {
    var answer: Int = n
    
    for c in control {
        if c == "w" { answer += 1 }
        else if c == "s" { answer -= 1 }
        else if c == "d" { answer += 10 }
        else { answer -= 10 }
    }
    
    return answer
}