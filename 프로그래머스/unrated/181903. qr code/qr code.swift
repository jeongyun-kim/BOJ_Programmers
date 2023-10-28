import Foundation

func solution(_ q:Int, _ r:Int, _ code:String) -> String {
    // code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 이어붙인 문자열 return
    var arr: [Int] = []
    let start = code.startIndex
    var answer: String = ""
    
    for i in 0..<code.count {
        if i % q == r {
            arr.append(i)
        }
    }
    
    for n in arr {
        answer += String(code[code.index(start, offsetBy: n)])
    }
    
    return answer 
}