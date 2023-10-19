import Foundation

func solution(_ my_string:String, _ k:Int) -> String {
    var ans = ""
    
    for i in 0..<k {
        ans = ans + my_string
    }
    
    return ans
}