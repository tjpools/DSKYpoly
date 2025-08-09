//******************************************************************************************
//main.c
//******************************************************************************************
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//******************************************************************************************
	void log_event(const char* msg);//Prototype
	//**********************************************************************************
	void log_event(const char* msg){
	FILE *log = fopen("DSKYpoly.log", "a"); //open in append mode
	if (log == NULL) {
		perror("Log file error");
        return ;
	}

	// Get current time
	time_t now = time(NULL);
	struct tm *t = localtime(&now);
        
	// Format and write time-stamped log entry
	fprintf(log, "[%04d-%02d-%02d %02d:%02d:%02d] DSKYpoly boot sequence initiated. \n",
		t->tm_year + 1900, t->tm_mon + 1, t->tm_mday,
		t->tm_hour, t->tm_min, t->tm_sec);

	fclose(log);

	printf("DSKYpoly launched. Log updated.\n");
	}
	//**********************************************************************************
int main(){
	int verb, noun;
	printf("=== DSKYpoly Interface ===\n");
	printf("Enter VERB (action): ");
	scanf("%d", &verb);
	printf("Enter NOUN (target): ");
	scanf("%d", &noun);

	char log_msg[128];
	snprintf(log_msg, sizeof(log_msg), "VERB %02d / NOUN %02d entered.", verb, noun);
	log_event(log_msg);

	if (verb == 10 && noun == 1){
		printf("Loading quadradic polynomial...\n");
		log_event("Loading quadratic polynomial.");
			// ToDo: Prompt for coefficients
	} else if (verb == 20 && noun == 01) {
		printf("Solving quadratic polynomial.");
		log_event("Solving quadratic polynomial.");
		// ToDo: Call solver
	}  else if (verb == 30 && noun == 01) {
		printf("Displaying the roots.");
		// ToDo: Print Results
	} else if(verb == 99) {
		printf("Exiting DSKYpoly.\n");
		log_event("Program Exited.");
		return 0;
	} else  {
		printf("Invalid VERB/NOUN combination.\n");
		log_event("Invalid Command.");
	}
		return 0;
	}	
	//**********************************************************************************




