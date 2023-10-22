import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    var answer: [Int] = num_list
    var cnt: Int = num_list.count-1 // 마지막 요소 인덱스
    
    if num_list[cnt] > num_list[cnt-1] {
        answer.append(num_list[cnt] - num_list[cnt-1])
    } else {
        answer.append(num_list[cnt] * 2)
    }
    
    return answer
}