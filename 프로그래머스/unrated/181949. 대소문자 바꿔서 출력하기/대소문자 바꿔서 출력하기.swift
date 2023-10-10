import Foundation

let s1 = readLine()!
var answer = ""
for c in s1 {
    if c.isUppercase == true {
        answer.append(c.lowercased())
    }
    else {
        answer.append(c.uppercased())
    }
}
print(answer)
