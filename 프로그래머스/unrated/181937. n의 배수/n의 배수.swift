import Foundation
// num이 n의 배수면 1 / 아니면 0 return
func solution(_ num:Int, _ n:Int) -> Int {
    
    if (num % n == 0) {
        return 1
    } else {
        return 0
    }
    
}