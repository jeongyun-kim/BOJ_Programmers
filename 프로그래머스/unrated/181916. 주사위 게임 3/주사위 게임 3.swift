import Foundation
    // 네 주사위에서 나온 숫자가 모두 p라면 1111 x p점 => 숫자 1개
    // 세 주사위에서 나온 숫자가 p 나머지는 다른 숫자라면 (10xp+q)^2점 => 숫자 2개
    // 두 값 같고 두 값 틀리면 (p+q)x(|p-q|) => 숫자 2개
    // 두 숫자는 같고 그 외는 q, r로 다르다면 qxr점 => 숫자 3개
    // 네 주사위의 숫자 모두 다르다면 가장 작은 숫자 => 숫자 4개
func solution(_ a:Int, _ b:Int, _ c:Int, _ d:Int) -> Int {
    var arr: [Int] = [a, b, c, d]
    let countedArr = NSCountedSet(array: arr)
    var dic: [Int:Int] = [:] 
    for abcd in arr {
        dic[abcd] = countedArr.count(for: abcd)
    }
    let sortedDic = dic.sorted { $0.1 > $1.1 }
    var cnt: Int = sortedDic.count 
    var answer: Int = 0
    
    if cnt == 1 {
        answer = 1111 * a
    } else if cnt == 2 {
        var p: Int = sortedDic[0].key
        var q: Int = sortedDic[1].key
        if sortedDic[0].value == sortedDic[1].value {
            answer = ((p+q)*(abs(p-q)))
        } else {
            answer = (10*p+q) * (10*p+q)
        }
    } else if cnt == 3 {
        var q: Int = sortedDic[1].key
        var r: Int = sortedDic[2].key
        answer = q * r
    } else {
        answer = arr.min()!
    }
    return answer 
}