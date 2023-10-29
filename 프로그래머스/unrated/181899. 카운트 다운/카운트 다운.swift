import Foundation

func solution(_ start:Int, _ end_num:Int) -> [Int] {
    var arr: [Int] = []
    
    for i in (end_num..<start+1).reversed() {
        arr.append(i)
    }
    
    return arr
}