plStruct is_palind_str(char *str)
{
	size_t i, j;
	static plStruct a;
	char *str2;

	if (!str)
	{
		printf("(null)");
		a.isPland = false;
		a.str = str;
		a.strln = 0;
		return a;
	}

	i =	strlen(str);
	str2 = malloc((i + 3) * sizeof(char)); // Extra space for '--' and null character
	if (!str2)
		exit(1);

	a.str = str;
	a.strln = i;
	a.isPland = true;

for(j = 0; j < i; j++)
{
	if (j == i / 2) {
		str2[j++] = '-';
		str2[j++] = '-';
	}
	str2[j] = str[j]; // Copy all characters to str2
	if (j < i / 2 && str[j] != str[i - 1 - j])
	{
		a.isPland = false;
	}
}
str2[j] = '\0';
	str2[j] = '\0'; // Don't forget the null character!

	a.str = str2;

	return (a);
}