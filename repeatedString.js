const repeatedString = (s, n) => {
    const countAll = y => y.split('a').length - 1
    let totCount = countAll(s) * Math.floor(n / s.length)
    let rem = countAll(s.slice(0, n % s.length))
    return totCount + rem
}


console.log(repeatedString('aba', 10))