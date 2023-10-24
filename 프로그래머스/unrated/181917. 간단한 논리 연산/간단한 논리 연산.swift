import Foundation

func solution(_ x1:Bool, _ x2:Bool, _ x3:Bool, _ x4:Bool) -> Bool {
    
    var x12: Bool = x1 || x2
    var x34: Bool = x3 || x4
    var answer: Bool = x12 && x34
    
    return answer
}