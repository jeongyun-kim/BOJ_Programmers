import Foundation

func solution(_ n:Int) -> Int {
    var answer: Int = 0
    var i: Int = 0
    
    if (n % 2 != 0) {
        for i in stride(from: 1, through: n+1, by: 2) {
            answer += i
        }
    } else {
        for i in stride(from: 2, through: n+1, by: 2) {
            answer += (i*i)
        }
    }
    
    return answer
}