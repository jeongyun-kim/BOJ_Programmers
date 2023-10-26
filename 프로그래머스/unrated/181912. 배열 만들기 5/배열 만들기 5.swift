import Foundation
// intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로 변환
// 이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 Return 
func solution(_ intStrs:[String], _ k:Int, _ s:Int, _ l:Int) -> [Int] {
    var answer: [Int] = []
    for iS in intStrs {
        let start = iS.index(iS.startIndex, offsetBy: s)
        let end = iS.index(iS.startIndex, offsetBy: l+s)
        var str: String = iS.substring(with: start..<end)
        if let num = Int(str) { 
            if num > k {
                answer.append(num)
            } } else {
                print("")
        }
    }
    return answer
}