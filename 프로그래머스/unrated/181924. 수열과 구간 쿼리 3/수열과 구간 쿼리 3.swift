import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    // query : [i, j] => arr[i] <-> arr[j]
    var arr2: [Int] = arr
    
    for query in queries {
        var i: Int = query[0] // i
        var j: Int = query[1] // j
        var temp: Int = arr2[i] 
        arr2[i] = arr2[j]
        arr2[j] = temp
    }
 
    return arr2
}