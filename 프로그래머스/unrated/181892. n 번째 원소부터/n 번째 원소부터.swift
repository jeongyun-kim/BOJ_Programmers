import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    var answer: [Int] = []
    // n번째 원소부터 마지막 원소까지 담은 리스트 return
    for i in stride(from: n-1, to: num_list.count, by: 1) {
        answer.append(num_list[i])
    }
    return answer
}