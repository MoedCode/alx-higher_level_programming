#include "lists.h"

/**
 *insert_node - Inserts integer to first node in a list
 *
 *@head: A pointer to list head
 *@number: integer  to be inserted
 *
 *Return: (NULL) on failure, (pointer) to the newNode mode
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *LIST = *head, *newNode;

	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number;

	if (!LIST || LIST->n >= number)
	{
		newNode->next = LIST;
		*head = newNode;
		return (newNode);
	}

	while (LIST && LIST->next && LIST->next->n < number)
		LIST = LIST->next;

	newNode->next = LIST->next;
	LIST->next = newNode;

	return (newNode);
}


