import Foundation

func solution(_ myString:String, _ pat:String) -> String {
    var myRe: String = String(myString.reversed())
    var cnt: Int = 0 
    var str: String = ""
    let patRe: String = String(pat.reversed())
    
    for c in myRe {
        str += String(c)
        if str.count >= pat.count {
            var idx = str.index(str.endIndex, offsetBy: -pat.count)
            if str[idx...] == patRe {
                break
            }
        cnt += 1
        }
    }
    
    var idx = myString.index(myString.endIndex, offsetBy: -cnt-1)
    let answer = String(myString[...idx])
    
    return answer
}