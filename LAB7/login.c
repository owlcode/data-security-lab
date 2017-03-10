#include <stdio.h>
#include <string.h>
int main(int argc, char *argv[]){
  char zalogowany;
  char haslo[8];
  zalogowany = 'n';
  strncpy( haslo, argv[1], 8 );
  if( strncmp( haslo, "tajne", 8 ) == 0 ){
    zalogowany = 't';
  }
  if( zalogowany == 't' ){
    printf("Poprawne haslo, witamy :)\n");
  } else {
    printf("Bledne haslo, uciekaj :(\n");
  }
}
