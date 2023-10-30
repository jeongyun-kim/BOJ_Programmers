import Foundation

func solution(_ arr:[Int], _ query:[Int]) -> [Int] {
    // 짝수 인덱스 : arr의 query[i] 이후는 버림
    // 홀수 인덱스 : arr의 query[i] 이전은 버림
    var answer: [Int] = arr
    
    for i in 0..<query.count {
        var num: Int = Int(query[i])
        if i % 2 == 0 {
            answer = Array(answer[0...num])
        } else {
            answer = Array(answer[num..<answer.count])
        }
    }
    return answer
}