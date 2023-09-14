#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - print some basic info about Python lists
 *and Python bytes objects.
 * @p: A PyObject list object.
 */
void print_python_bytes(PyObject *p)
{
	int  i, PRENRD_BYTES, SIZE;
	char *STRING;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		SIZE = ((PyVarObject *)(p))->ob_SIZE;
		printf("  SIZE: %d\n", SIZE);
		STRING = ((PyBytesObject *)p)->ob_sval;
		printf("  trying string: %s\n", STRING);

		if (SIZE < 10)
			PRENRD_BYTES = SIZE + 1;
		else
			PRENRD_BYTES = 10;

		printf("  first %d bytes:", PRENRD_BYTES);

		for (i = 0; i < PRENRD_BYTES; i++)
			if (STRING[i] >= 0)
				printf(" %02x", STRING[i]);
			else
				printf(" %02x", 256 + STRING[i]);

		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
}
/**
 * print_python_list -  print_python_list
 * @p: A function parameter .
 */
void print_python_list(PyObject *p)
{
	int SIZE, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	SIZE = var->ob_SIZE;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] SIZE of the Python List = %d\n", SIZE);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < SIZE; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
