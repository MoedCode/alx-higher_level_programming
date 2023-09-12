#include "lists.h"
#include <stdlib.h>

listint_t *reverse_list(listint_t *head) {
	listint_t *prev = NULL, *current = head, *next = NULL;
	while (current != NULL) {
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return prev;
}

int compare_lists(listint_t *head1, listint_t *head2) {
	while (head1 != NULL && head2 != NULL) {
		if (head1->n != head2->n)
			return 0;
		head1 = head1->next;
		head2 = head2->next;
	}
	return (head1 == NULL && head2 == NULL);
}

int is_palindrome(listint_t **head) {
	listint_t *slow = *head, *fast = *head, *prev_slow = NULL, *second_half = NULL;
	int res = 1;

	// If list is empty or has only one node
	if (*head != NULL && (*head)->next != NULL) {
		while (fast != NULL && fast->next != NULL) {
			prev_slow = slow;
			slow = slow->next;
			fast = fast->next->next;
		}

		if (fast != NULL) {
			slow = slow->next;
		}

		second_half = slow;
		prev_slow->next = NULL;

		second_half = reverse_list(second_half);

		res = compare_lists(*head, second_half);

		second_half = reverse_list(second_half);

		if (fast != NULL) {
			prev_slow->next = slow;
			slow->next = second_half;
		} else {
			prev_slow->next = second_half;
		}
	}

	return res;
}