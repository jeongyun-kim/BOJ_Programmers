import Foundation

func solution(_ n:Int, _ slicer:[Int], _ num_list:[Int]) -> [Int] {
    // n = 1 : num_list의 0번 인덱스부터 b번 인덱스까지
    // n = 2 : num_list의 a번 인덱스부터 마지막 인덱스까지
    // n = 3 : num_list의 a번 인덱스부터 b번 인덱스까지
    // n = 4 : num_list의 a번 인덱스부터 b번 인덱스까지 c 간격으로
    var a: Int = slicer[0]
    var b: Int = slicer[1] + 1
    var c: Int = 1
    var answer: [Int] = []
    
    if n == 1 {
        a = 0
    } else if n == 2 { 
        b = num_list.count 
    } else if n == 4 {
        c = slicer[2]
    } 
    
    for i in stride(from: a, to: b, by: c){
        answer.append(num_list[i])
    }
    
    return answer
}