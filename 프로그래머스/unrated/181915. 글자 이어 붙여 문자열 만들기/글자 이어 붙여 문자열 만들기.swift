import Foundation
// 문자열 : my_string, 정수 배열 : index_list
func solution(_ my_string:String, _ index_list:[Int]) -> String {
    var answer: String = ""
    var start = my_string.startIndex
    
    for idx in index_list {
        var c = my_string[my_string.index(start, offsetBy: idx)]
        answer += String(c)
    }
    
    return answer
}