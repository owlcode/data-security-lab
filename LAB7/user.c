 #define TAJNY_PIN 1234
  int main(int ac, char **av)
  {
          int pin,ok=0;
          
       	sscanf(av[1], "%u", &pin);
		
	if (pin < 0) {
		printf("zle\n");
		exit(1);
	}
        
	  if (pin == TAJNY_PIN) {
                  ok = 1;
          }
          if (ok == 1) {
                  printf("PIN poprawny\n");
          } else {
                  printf("PIN bledny\n");
          }
  }
