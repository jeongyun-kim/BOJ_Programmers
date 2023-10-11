import Foundation

func solution(_ my_string:String, _ overwrite_string:String, _ s:Int) -> String {
    var answer = ""
    if(s != 0){
        let frontIdx = my_string.index(my_string.startIndex, offsetBy: Int(s-1))
        answer.append(String(my_string[...frontIdx]))
    }
    
    answer.append(overwrite_string)
    
    let idx = s + overwrite_string.count - my_string.count
    if(idx != 0){
        let backIdx = my_string.index(my_string.endIndex, offsetBy: idx)
        answer.append(String(my_string[backIdx...]))
    }
    return answer
}