import Foundation

func solution(_ num_list:[Int]) -> Int {
    var nums: [Int] = num_list
    var answer: Int = 0
    
    for num in nums {
        var num: Int = num
        while(num>1) {
            if num % 2 == 0 {
                num = num / 2
            } else {
                num = (num-1)/2
            }
            answer += 1
        }
    }
    
    return answer
}