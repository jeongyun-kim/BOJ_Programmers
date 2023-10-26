import Foundation

func solution(_ my_string:String, _ is_suffix:String) -> Int {
    var answer: Int = 0
    let length: Int = my_string.count
    
    for i in (1...length).reversed() {
        let s: String = String(my_string.suffix(i))
        if s == is_suffix {
            answer = 1
            break
        }
    }
    
    return answer
}