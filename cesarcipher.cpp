#include<stdio.h>
#include<string.h>
#include<ctype.h>
int main()
{
    char plain[10],cipher[10];
    int i,key,length;
    printf("enter the plain text\n");
    scanf("%s",plain);
    printf("enter the key vaue\n");
    scanf("%d",&key);
    printf("\n\n\t PLAIN TEXT:%s",plain);
    printf("\n\n\t ENCRYPTION: ");
    for(i=0,length=strlen(plain);i<length;i++)
    {
        cipher[i]=plain[i]+key;
        if(isupper(plain[i])&&(cipher[i]>'Z'))
        cipher[i]=cipher[i]+26;
        if(islower(plain[i])&&(cipher[i]>'z'))
        cipher[i]=cipher[i]+26;
        printf("%c",cipher[i]);
    }
    printf("\n\n\n DECRYPTION:");
    for(i=0;i<length;i++)
    {
        plain[i]=cipher[i]-key;
        if(isupper(cipher[i])&&(plain[i]<'A'))
        plain[i]=plain[i]-26;
        if(islower(cipher[i])&&(cipher[i]<'a'))
        plain[i]=plain[i]-26;
        printf("%c",plain[i]);
        
    }
    return 0;
}
