import Foundation

func solution(_ rny_string:String) -> String {
    let answer: String = rny_string.replacingOccurrences(of: "m", with: "rn")
    return answer
}