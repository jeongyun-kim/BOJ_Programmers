import Foundation

func solution(_ number:String) -> Int {
    var total: Int = 0
    
    for c in number {
        var num = Int(String(c))!
        total += num
    }
    
    return total % 9
}