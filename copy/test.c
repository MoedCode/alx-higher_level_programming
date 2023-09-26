#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct is_palind_sruct
{
	char* str;
	bool isPland;
	size_t strln;

} plStruct;

plStruct is_palind_str(char *str);

int main(int argc, char **argv)
{
	plStruct a;
	if (argc < 2 || !argv[1] )
		return (-1);
	printf("argc[%d]\n",argc);

	a = is_palind_str(argv[1]);
	printf("[%s][%s][%zu]\n",a.str,a.isPland ? "TRUE":"FALSE",a.strln);
	return (0);
}

plStruct is_palind_str(char *str)
{
	size_t i, j;
	static plStruct a;

	if (!str)
	{
		printf("(null)");
		a.isPland = false;
		a.str = str;
		a.strln = 0;
		return a;
	}

	i =	strlen(str);

	a.str = str;
	a.strln = i;
	a.isPland = true;

	for(j = 0; j < i; j++)
	{
		if (j < i / 2 && str[j] != str[i - 1 - j])
		{
			a.isPland = false;
		}
	}

	if (i > 2) {
		if (i % 2 == 0) {
			// For strings with even length, move characters to make space for '--'
			for (j = i; j > i / 2; j--) {
				str[j + 1] = str[j];
			}
			str[i / 2] = '-';
			str[i / 2 + 1] = '-';
		} else {
			// For strings with odd length, move characters to make space for '-'
			for (j = i; j > i / 2 + 1; j--) {
				str[j + 1] = str[j];
			}
			str[i / 2 + 1] = '-';
		}
		str[i + 2] = '\0';
	}

	return (a);
}