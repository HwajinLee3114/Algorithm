function solution(n) {
    let sum = 0;
    for (let i = 2; i < n + 1; i+=2) {
        sum += i;
    }
    return sum;
}