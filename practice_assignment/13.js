/* Return the Largest Digit in a Number
# You are given an integer n. 
# Your task is to return the largest digit present in the number.*/

function returnLargestDigit(n) {
    let largest = 0;
    while(n>0){
        let digit = n%10;
        if (digit>largest){
            largest=digit;
    
        }
        n = Math.floor(n/10)
    }
    return largest;
}