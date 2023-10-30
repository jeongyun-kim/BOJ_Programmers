import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var answer: [Int] = []
    var idxs: [Int] = []
    
    for i in 0..<arr.count {
        if arr[i] == 2 {
            idxs.append(i)
        }
    }
    
    if idxs.count == 0 {
        answer.append(-1)
    } else {
        var start = idxs[0]
        var end = idxs[idxs.count-1] + 1
        for j in stride(from: start, to: end, by: 1) {
            answer.append(arr[j])
        }
    }
    
    return answer
}