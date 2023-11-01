import Foundation

func solution(_ str_list:[String]) -> [String] {
    var idx: Int = 0
    var answer: [String] = []

    for c in str_list {
        if c == "l" {
            answer = Array(str_list[0..<idx])
            break
        } else if c == "r"{
            answer = Array(str_list[idx+1..<str_list.count])
            break
        }
        idx += 1
    }
    return answer
}