import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    var ans1: String = String(a) + String(b)
    var ans2: String = String(b) + String(a)
    var answer: String = max(ans1, ans2)
    
    return Int(answer)!
}