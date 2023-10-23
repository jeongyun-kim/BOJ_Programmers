import Foundation
// query : [s, e, k]
// s <= idx <= e 인 모든 idx에 대해 idx가 k의 배수면 arr[i] + 1 
func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var idx: Int = 0 
    var arr2: [Int] = arr
    
    for i in 0..<queries.count {
        var s: Int = queries[i][0]
        var e: Int = queries[i][1]
        var k: Int = queries[i][2]
        for j in s...e {
            if j % k == 0 {
                arr2[j] = arr2[j] + 1
            }
        }
    }
    return arr2
}