import Foundation

func solution(_ num_list:[Int]) -> Int {
    let length: Int = num_list.count
    var answer: Int = 0
    
    if length >= 11 {
        for num in num_list {
            answer += num
        } 
    } else {
        answer = 1
        for num in num_list{
            answer *= num
        }
    }
    
    return answer
}