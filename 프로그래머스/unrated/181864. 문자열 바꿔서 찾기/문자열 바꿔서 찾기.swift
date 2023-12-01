import Foundation

func solution(_ myString:String, _ pat:String) -> Int{
    var str: String = ""
    
    for c in pat {
        if c == "A" {
            str += "B"
        } else {
            str += "A"
        }
    }
    
    if myString.contains(str) {
        return 1
    } else {
        return 0
    }
}