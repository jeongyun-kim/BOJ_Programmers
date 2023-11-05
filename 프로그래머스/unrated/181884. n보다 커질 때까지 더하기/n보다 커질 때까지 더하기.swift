import Foundation

func solution(_ numbers:[Int], _ n:Int) -> Int {
    var answer: Int = 0
    
    for i in 0..<numbers.count {
        answer += numbers[i]
        if answer > n {
            break
        }
    }
    
    return answer
}