import Foundation

func solution(_ binomial:String) -> Int {
    var arr: [String] = binomial.components(separatedBy: " ")
    let op = arr[1]
    var answer: Int = 0
    
    switch op {
        case "+": answer = Int(arr[0])! + Int(arr[2])!
        case "-": answer = Int(arr[0])! - Int(arr[2])!
        case "*": answer = Int(arr[0])! * Int(arr[2])!
        default: answer = 0
    }
    
    return answer
}