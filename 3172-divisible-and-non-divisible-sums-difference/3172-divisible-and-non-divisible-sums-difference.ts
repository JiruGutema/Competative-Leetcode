function differenceOfSums(n: number, m: number): number {
  let sum: number = n*(n+1)/2
    let sum1: number = 0

    for (let counter: number = 0; counter <= n; counter +=m){
        sum1 += counter
    }
    return sum - sum1 - sum1
};