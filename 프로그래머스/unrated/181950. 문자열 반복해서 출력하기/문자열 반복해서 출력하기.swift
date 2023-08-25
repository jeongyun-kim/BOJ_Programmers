import Foundation

let inp = readLine()!.components(separatedBy: [" "]).map { $0 }
let (s, n) = (inp[0], Int(inp[1])!) // s은 문자열, n은 반복횟수
let answer = String(repeating: s, count: n)
print(answer)