import Foundation

func solution(_ arr:[Int]) -> Int {
    var arr1: [Int] = arr
    var answer: Int = 0
    
    while(true) {
        var arr2: [Int] = []
        for num in arr1 {
            if num >= 50 && num % 2 == 0 {
                arr2.append(num/2)
            } else if num < 50 && num % 2 != 0 {
                arr2.append(num*2+1)
            }
        }
        if arr1 == arr2 {
            print(answer)
            break
        } else {
            answer += 1
            arr1 = arr2
        }
    }
    
    return answer-1
}