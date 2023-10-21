import Foundation

func solution(_ a:Int, _ d:Int, _ included:[Bool]) -> Int {
    var idx: Int = 0
    var total: Int = 0
    
    for i in included {
        if i == true {
            total = total + a + d*idx
        }
        idx += 1
    }
    
    return total
}