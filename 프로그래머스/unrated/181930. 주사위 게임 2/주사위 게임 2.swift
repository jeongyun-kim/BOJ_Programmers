import Foundation
// 세 숫자가 모두 다르다면 a+b+c점
// 두 숫자는 같고 한 숫자는 다르면 (a+b+c)×(a2+b2+c2)점
// 세 숫자가 모두 같다면 (a+b+c)×(a2+b2+c2)×(a3+b3+c3)점
func solution(_ a:Int, _ b:Int, _ c:Int) -> Int {
    var answer: Int = 0
    var abc: Int = a + b + c
    var abc2: Int = abc * (a*a + b*b + c*c)
    var abc3: Int = abc2 * (a*a*a + b*b*b + c*c*c)
    
    if a != b && b != c && a != c {
        answer = abc
    } else if a == b && a == c && b == c {
        answer = abc3
    } else {
        answer = abc2
    }
    
    return answer
}