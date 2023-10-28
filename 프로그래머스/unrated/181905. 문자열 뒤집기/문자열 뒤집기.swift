import Foundation

func solution(_ my_string:String, _ s:Int, _ e:Int) -> String {
    let start = my_string.startIndex
    let end1 = my_string.index(my_string.startIndex, offsetBy: s)
    let end2 = my_string.index(my_string.startIndex, offsetBy : e)
    let start2 = my_string.index(my_string.startIndex, offsetBy: e+1)
    let end3 = my_string.endIndex
    var answer: String = ""
    
    var startStr: String = my_string.substring(with: start..<end1)
    var reversedStr: String = String(my_string.substring(with: end1..<start2).reversed())
    var endStr: String = my_string.substring(with: start2..<end3)

    answer = startStr + reversedStr + endStr
    
    return answer
}