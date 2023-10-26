import Foundation

func solution(_ my_string:String) -> [String] {
    
    var answer: [String] = []
    var length: Int = my_string.count
    
    for i in (1...length).reversed() {
        answer.append(String(my_string.suffix(i)))
    }
    answer.sort()
    
    return answer
}