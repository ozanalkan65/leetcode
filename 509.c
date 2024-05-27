int fib(int n){
    int f0 = 0;
    int f1 = 1;
    int i;
    int f2;
    if (n==0){
        return 0;
    }
    if (n==1){
        return 1;
    }
    else{
        for (i=1; i<n; i++){
            f2 = f0 + f1;
            f0 = f1;
            f1 = f2;
        }
        return f2;
    }
}