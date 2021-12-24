

char * addBinary(char * a, char * b){
    int alength = strlen(a);
    int blength = strlen(b);
    int carry = 0;
    int length = alength > blength ? alength : blength;
    char* result = malloc(length+2);
    result[length+1] = '\0';
    while (alength || blength)
    {
        if (alength)
        {
            carry += a[--alength] - '0';
        }
        if (blength)
        {
            carry += b[--blength] - '0';
        }
        result[length--] = (carry & 1) + '0';

        carry >>= 1; // right shift 1
    }
    result[0] = carry + '0';
    
    return result + (carry ^ 1); // xor
}