import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    var answer: [Int] = []
    
    for i in stride(from: 0, to: n, by: 1) {
        answer.append(num_list[i])
    }
    
    return answer
}