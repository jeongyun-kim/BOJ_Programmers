import Foundation

func solution(_ my_string:String, _ is_prefix:String) -> Int {
    let cnt: Int = is_prefix.count
    let myStr: String = String(my_string.prefix(cnt))
    var answer: Int = 0
    
    if myStr == is_prefix {
        answer = 1
    } 
    
    return answer 
}