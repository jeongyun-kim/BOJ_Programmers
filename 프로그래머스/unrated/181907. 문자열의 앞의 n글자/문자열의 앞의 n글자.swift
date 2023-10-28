import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    let start = my_string.startIndex
    let end = my_string.index(my_string.startIndex, offsetBy : n)
    var answer: String = my_string.substring(with: start..<end)
    
    return answer
}