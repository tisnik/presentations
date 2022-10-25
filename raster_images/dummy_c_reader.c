#include <stdio.h>

/*
 * A PNG file starts with an 8-byte signature
 * Values     Purpose
 * 89         Has the high bit set to detect transmission systems that do not support 8-bit data 
 *            and to reduce the chance that a text file is mistakenly interpreted as a PNG, or vice versa.
 * 50 4E 47   In ASCII, the letters PNG, allowing a person to identify the format easily if it is viewed in a text editor.
 * 0D 0A      A DOS-style line ending (CRLF) to detect DOS-Unix line ending conversion of the data.
 * 1A         A byte that stops display of the file under DOS when the command type has been used—the end-of-file character.
 * 0A         A Unix-style line ending (LF) to detect Unix-DOS line ending conversion.
 */
int read_header(FILE * f)
{
    unsigned char header[8];
    unsigned char expected[] = { 0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a };
    size_t read_bytes;
    int i;
    int err = 0;

    read_bytes = fread(header, sizeof(header), 1, f);
    if (read_bytes != 1) {
        printf("File truncated?");
        return 1;
    }

    printf("PNG header\n");
    printf("Offset Read Expected Status\n");

    for (i = 0; i < 8; i++) {
        if (header[i] != expected[i]) {
            printf("%d     %02x    %02x       differs\n", i, header[i], expected[i]);
            err = 1;
        } else {
            printf("%d     %02x    %02x       ok\n", i, header[i], expected[i]);
        }
    }
    printf("\n");

    return err;
}

/* A chunk consists of four parts: length (4 bytes, big-endian), chunk
 * type/name (4 bytes), chunk data (length bytes) and CRC (cyclic
 * redundancy code/checksum; 4 bytes). The CRC is a network-byte-order
 * CRC-32 computed over the chunk type and chunk data, but not the length. 
 */
int read_chunks(FILE * f)
{
    unsigned char buffer[4];
    unsigned char type[4];
    size_t read_bytes;
    int length;

    printf("Chunk Length\n");

    do {

        read_bytes = fread(&buffer, sizeof(buffer), 1, f);
        if (read_bytes != 1) {
            printf("Read error!\n");
            return 1;
        }
        length = (int) buffer[3] | (int) buffer[2] << 8 | (int) buffer[1] << 16 | (int) buffer[0] << 24;

        read_bytes = fread(&type, sizeof(length), 1, f);
        if (read_bytes != 1) {
            printf("Read error!\n");
            return 1;
        }

        printf("%c%c%c%c  %d\n", type[0], type[1], type[2], type[3],
               length);
        fseek(f, length + 4, SEEK_CUR);
    } while (!(type[0] == 'I' && type[1] == 'E' && type[2] == 'N' && type[3] == 'D'));

    return 0;
}

int main(void)
{
    char *filename = "c.png";
    FILE *f = NULL;
    int err;

    f = fopen(filename, "rb");
    if (f == NULL) {
        printf("Unable to read file\n");
        return 1;
    }

    printf("File opened for reading\n\n");

    err = read_header(f);
    if (err) {
        printf("Wrong header\n");
        fclose(f);
        return 1;
    }

    err = read_chunks(f);
    if (err) {
        printf("Error reading chunks\n");
        fclose(f);
        return 1;
    }

    fclose(f);


    return 0;
}
