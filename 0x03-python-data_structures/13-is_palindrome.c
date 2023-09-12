#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * palindrome_rec - us recursion to otorate over list
 * @head: pointer to first node
 * @tail: pointer to tail norde
 *
 * Return: (1)id lists n values is palindrome,
 *(0) if  it not
 */

int palindrome_rec(listint_t **head, listint_t *tail)
{
	if (!tail)
		return (1);

	if (palindrome_rec(head, tail->next) == 1 && (*head)->n == tail->n)
	{
		(*head) = (*head)->next;
		return (1);
	}

	else
		return (0);
}


/**
 * is_palindrome - checks if the list is palindrome
 * @head: pointwr to first node
 * Return:(1)id lists n values is palindrome,
 *(0) if  it not
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	if ((*head)->next == NULL)
		return (1);

	return (palindrome_rec(head, *head));
}