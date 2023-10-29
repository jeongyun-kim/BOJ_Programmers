import Foundation

func solution(_ my_string:String) -> [Int] {
    // 0이 52개인 배열 arr
    var arr = [Int](repeating: 0, count: 52) 
    // A~Z : 65~90 / a~z : 97~122
    for s in my_string {
        var asciiNum: Int = Int(UnicodeScalar(String(s))!.value)
        if asciiNum >= 65 && asciiNum <= 90 {
            var idx1: Int = asciiNum - 65
            arr[idx1] += 1
        } else {
            var idx2: Int = asciiNum - 97
            arr[26+idx2] += 1
        }   
    }
    return arr
}