import Foundation

func solution(_ arr:[Int], _ intervals:[[Int]]) -> [Int] {
    var answer: [Int] = []
    
    for i in intervals {
        var a: Int = i[0]
        var b: Int = i[1] + 1
        for j in stride(from: a, to: b, by: 1){
            answer.append(arr[j])
        }
    }
    return answer
}