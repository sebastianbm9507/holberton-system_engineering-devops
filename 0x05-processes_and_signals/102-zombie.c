#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
/**
 * infinite_while - no end loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - creates the zombir process
 * Return: 0
 */
int main(void)
{
	pid_t pid_num;
	int zombi_process = 0;

	while (zombi_process < 5)
	{
		pid_num = fork();
		if (pid_num > 0)
		{
			printf("Zombie process created, PID: %d\n", pid_num);
			zombi_process++;
		}
		else
		{
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
