import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    // n번째 이후의 원소들
    var num_list2: [Int] = Array(num_list[n..<num_list.count])
    // n번째 이후 원소들 + n번째 이전 원소들
    for i in stride(from: 0, to: n, by: 1) {
        num_list2.append(num_list[i])
    }
    return num_list2
}