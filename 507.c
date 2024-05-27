bool checkPerfectNumber(int num) {
    int i;
    int counter = 0;
    for (i=1; i<(num/2+1); i++) {
        if (num % i == 0) {
            counter +=i ;
        }
    }    
    printf("%d\n", counter);
    return counter == num;
}