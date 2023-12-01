#include <stdio.h>
#include <string.h>

#define MAX_LEN 100

void encryptRailFence(char *plaintext, int rails, char *ciphertext) {
    int len = strlen(plaintext);
    char matrix[rails][len];
    memset(matrix, 0, sizeof(matrix));

    int row = 0, col = 0;
    int dir_down = 0;

    for (int i = 0; i < len; i++) {
        if (row == 0 || row == rails - 1)
            dir_down = !dir_down;

        matrix[row][col++] = plaintext[i];

        dir_down ? row++ : row--;
    }

    int index = 0;
    for (int i = 0; i < rails; i++) {
        for (int j = 0; j < len; j++) {
            if (matrix[i][j] != 0)
                ciphertext[index++] = matrix[i][j];
        }
    }
    ciphertext[index] = '\0';
}

int main() {
    char plaintext[MAX_LEN], ciphertext[MAX_LEN];
    int rails;

    printf("Enter the plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);
    plaintext[strcspn(plaintext, "\n")] = '\0';

    printf("Enter the number of rails: ");
    scanf("%d", &rails);

    encryptRailFence(plaintext, rails, ciphertext);

    printf("Ciphertext: %s\n", ciphertext);

    return 0;
}
