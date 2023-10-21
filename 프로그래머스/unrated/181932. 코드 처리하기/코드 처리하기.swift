import Foundation
// mode가 0일 때, 1이 아니면 idx가 짝수일때만 ret의 맨뒤에 code[idx] 추가
// mode가 1일 때, 1이 아니면 idx가 홀수일때만 ret의 맨뒤에 code[idx] 추가
// code[idx]가 1이면 mode 전환(0<->1)
// ret이 빈 문자열이라면 "EMPTY" 출력
func solution(_ code:String) -> String {
    var ret = ""
    var mode: Int = 0
    var idx: Int = 0
    
    for c in code {
        if (c != "1") {
            if (mode == 0) && (idx % 2 == 0){
                ret += String(c)
            } else if (mode == 1) && (idx % 2 != 0) {
                ret += String(c)
            } 
        } else {
            if mode == 1 {
                mode = 0
            } else {
                mode = 1
            }
        }
        idx += 1
    }
    if ret == "" {
        ret = "EMPTY"
    } 
    
    return ret
}