import Foundation

func solution(_ num_list:[Int]) -> Int {
    var odd: Int = 0
    var even: Int = 0
    
    for i in 0..<num_list.count {
        if i % 2 == 0 {
            odd += num_list[i]
        } else {
            even += num_list[i]
        }
    }
    
    return max(odd, even)
}