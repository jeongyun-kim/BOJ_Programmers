import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var answer: [Int] = arr
    
    for query in queries {
        let s: Int = query[0]
        let e: Int = query[1]
        for i in stride(from: s, to: e+1, by: 1) {
            answer[i] += 1
        }
    }
    
    return answer
}