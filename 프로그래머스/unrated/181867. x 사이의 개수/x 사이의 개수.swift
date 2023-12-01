import Foundation

func solution(_ myString:String) -> [Int] {
    // myString을 문자"x"를 기준으로 나눈 후 나눠진 문자열의 길이를 저장한 배열을 return
    var arr: [String] = myString.components(separatedBy: "x")
    var answer: [Int] = []
    
    for c in arr {
        answer.append(c.count)
    }
    
    return answer
}