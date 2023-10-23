import Foundation
// x가 짝수면 2로 나누고 홀수면 3*x+1 => 하다보면 언젠가 x가 1이됨
func solution(_ n:Int) -> [Int] {
    var x: Int = n
    var answer: [Int] = [n]
    
    while(x>1) {
        if x % 2 == 0 {
            x = x / 2
        } else {
            x = x * 3 + 1
        }
        answer.append(x)
    }
    
    return answer
}