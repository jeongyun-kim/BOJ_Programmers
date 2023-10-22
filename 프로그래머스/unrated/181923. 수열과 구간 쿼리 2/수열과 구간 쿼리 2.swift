import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    // query => [s, e, k]
    // s <= idx <= e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i] 찾기
    var answer: [Int] = []
    
    for query in queries {
        
        var arr2: [Int] = []
        var s: Int = query[0]
        var e: Int = query[1]
        var k: Int = query[2]
        
        for i in s...e {
            if arr[i] > k {
                arr2.append(arr[i])
            }
        }
        
        if let num = arr2.min() {
            answer.append(num)
        } else {
            answer.append(-1)
        }
        
    }
    return answer
}