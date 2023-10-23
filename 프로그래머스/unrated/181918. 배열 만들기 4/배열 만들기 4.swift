import Foundation
// 변수 i 초깃값0 => arr의 길이보다 작으면 
// stk가 빈 배열이라면 arr[i]를 stk에 추가, i+1
// stk에 원소가 있고, stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk뒤에 추가 i+1
// stk에 원소가 있고 stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소를 제거
func solution(_ arr:[Int]) -> [Int] {
    var i: Int = 0
    var stk: [Int] = []
    
    while(i < arr.count) {
        if stk.count == 0 {
            stk.append(arr[i])
            i += 1
        } else if stk[stk.count-1] < arr[i] {
            stk.append(arr[i])
            i += 1
        } else {
            stk.popLast()
        }
    }
    return stk
}