import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    // suffix(n) : 뒤의 문자열 n개 가져옴
    
    return String(my_string.suffix(n))
}