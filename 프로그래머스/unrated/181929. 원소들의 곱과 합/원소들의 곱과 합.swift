import Foundation
// 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0
func solution(_ num_list:[Int]) -> Int {
    var total: Int = 0
    var total2: Int = 1 
    var answer: Int = 0
    
    for num in num_list {
        total = total + num
        total2 = total2 * num
    }
    total = total * total
    
    if total2 < total {
        answer = 1
    } else {
        answer = 0
    }
    
    return answer
}