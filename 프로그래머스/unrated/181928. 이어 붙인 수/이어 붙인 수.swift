import Foundation
// 홀수만 이어붙인 수 + 짝수만 이어붙인 수
func solution(_ num_list:[Int]) -> Int {
    var odd: String = ""
    var even: String = ""
    var total: Int = 0
    
    for num in num_list {
        if num % 2 == 0 {
            even += String(num)
        } else {
            odd += String(num)
        }
    } 
    total = Int(odd)! + Int(even)!
    
    return total
}