import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    var n1: Int = Int(String(a) + String(b))!
    var n2: Int = a * b * 2
    
    return max(n1, n2)
}