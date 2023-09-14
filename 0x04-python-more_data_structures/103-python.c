#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints basic info about Python Obj bytes.
 * @p: A PyObject list object.
 */
void print_python_bytes(PyObject *p)
{
	int size, i, Bytes_to_print;
	char *buffer;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		size = ((PyVarObject *)(p))->ob_size;
		printf("  size: %d\n", size);
		buffer = ((PyBytesObject *)p)->ob_sval;
		printf("  trying string: %s\n", buffer);

		if (size < 10)
			Bytes_to_print = size + 1;
		else
			Bytes_to_print = 10;

		printf("  first %d bytes:", Bytes_to_print);

		for (i = 0; i < Bytes_to_print; i++)
			if (buffer[i] >= 0)
				printf(" %02x", buffer[i]);
			else
				printf(" %02x", 256 + buffer[i]);

		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
}
/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
