/*
 * File: 103-python.c
 */

#include <Python.h>

void print_python_list(PyObject *list_object);
void print_python_bytes(PyObject *bytes_object);

/**
 * print_python_list - Prints basic info about Python lists.
 * @list_object: A PyObject list object.
 */
void print_python_list(PyObject *list_object)
{
	int size, allocation, i;
	const char *element_type;
	PyListObject *list = (PyListObject *)list_object;
	PyVarObject *var = (PyVarObject *)list_object;

	size = var->ob_size;
	allocation = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocation);

	for (i = 0; i < size; i++)
	{
		element_type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, element_type);
		if (strcmp(element_type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @bytes_object: A PyObject byte object.
 */
void print_python_bytes(PyObject *bytes_object)
{
	unsigned char i, size;
	PyBytesObject *bytes = (PyBytesObject *)bytes_object;

	printf("[.] bytes object info\n");
	if (strcmp(bytes_object->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)bytes_object)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)bytes_object)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)bytes_object)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

