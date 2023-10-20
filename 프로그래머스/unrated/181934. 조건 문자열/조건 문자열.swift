import Foundation

func solution(_ ineq:String, _ eq:String, _ n:Int, _ m:Int) -> Int {
    var answer: Int = 0
    
    if ineq == ">" && eq == "=" && n >= m {
        answer = 1
    } else if ineq == ">" && eq == "!" &&  n > m {
        answer = 1
    } else if ineq == "<" && eq == "=" && n <= m {
        answer = 1
    } else if ineq == "<" && eq == "!" && n < m {
        answer = 1
    }
    
    return answer
}