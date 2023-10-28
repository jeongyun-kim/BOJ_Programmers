import Foundation

func solution(_ my_string:String, _ m:Int, _ c:Int) -> String {
    let length: Int = my_string.count
    var cnt: Int = 1
    var arr: [String] = []
    var answer: String = ""
    
    for i in stride(from: 0, to: length, by: m) {
        var start = my_string.index(my_string.startIndex, offsetBy: i)
        var end = my_string.index(my_string.startIndex, offsetBy: cnt*m)
        cnt += 1
        arr.append(String(my_string.substring(with: start..<end)))
    }
    
    for s in arr {
        answer += String(s[s.index(s.startIndex, offsetBy: c-1)])
    }
    
    return answer 
}