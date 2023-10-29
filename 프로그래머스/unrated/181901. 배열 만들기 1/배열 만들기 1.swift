import Foundation

func solution(_ n:Int, _ k:Int) -> [Int] {
    var arr: [Int] = []
    
    for i in stride(from: k, to: n+1, by: k) {
        arr.append(i)
    }
    
    return arr
}