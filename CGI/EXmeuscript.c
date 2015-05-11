#include <stdio.h> 
#include <stdlib.h> 
int main(void){ 
  /* print content type and blank line */ 
printf(“Content-Type:text/html\n\n”); 
printf(”<html>\n”); 
printf("<H3>CGI Test</H3>\n"); 
printf(“<p>This is my first CGI program!\n”); 
printf(“</html>\n”); 
return 0; 
} 