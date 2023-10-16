#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdarg.h>
#include <unistd.h>
int _printf(const char *format, ...);
int print_format(char specifier, va_list ap);
int print_char(int c);
int main() {
  printf("Character:[%c]\n", 'H');
  _printf("Character:[%c]\n", 'H');
  _printf("Character:[%%]\n", 'H');
	putchar('#');
  _printf("%\n", 'H');

  return 0;
}
int _printf(const char *format, ...)
{
	va_list ap;
	int result = 0;
	int i = 0;
	va_start(ap, format);
	while (format[i] != '\0')
	{
		if (format[i] == '%') {
			/* Check if the next character is a valid format specifier */
			if (format[i + 1] != '\0') {
				result += print_format(format[i + 1], ap);
				/* Skip the format specifier*/
				i++;
			}
			else {
				/* Handle case where '%' is the last character in the format string*/

				write(1, &format[i], 1);
			}
		}
		else {
			write(1, &format[i], 1);
		}
		i++;
	}
	va_end(ap);
	return result;
}
int print_format(char specifier, va_list ap)
{
	int count;

	count = 0;
	if (specifier == 'c')
		count += print_char(va_arg(ap, int));
	else
		{

			// count += write(1, "%", 1);
			count += write(1, &specifier, 1);

		}
	return (count);
}
int print_char(int c)
{
	return (write(1, &c, 1));
}